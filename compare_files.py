#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Define the Excel file names
prod_file = 'Production_code.xlsx'
qa_file = 'QA_code.xlsx'
compare_file = 'production_and_qa_code_compare.xlsx'

# Tab names to iterate over
tabs = ['master_file', 'join_file', 'detail_file']

# Function to compare two dataframes and return the comparison result along with a summary
def compare_dfs(df1, df2, key_columns, df1_name='Production', df2_name='QA'):
    # Identify matching and differing rows based on key columns
    df_combined = pd.merge(df1, df2, on=key_columns, how='outer', suffixes=('_prod', '_qa'), indicator=True)
    
    # Initiate a counter for value differences
    value_differences = 0
    
    # Check value differences in matching rows
    for index, row in df_combined.iterrows():
        if row['_merge'] == 'both':
            for col in df1.columns:
                if col not in key_columns and row[col + '_prod'] != row[col + '_qa']:
                    value_differences += 1
                    break  # Stop checking further columns once a difference is found
    
    # Generate summary statistics
    total_rows = df_combined.shape[0]
    matches = df_combined['_merge'] == 'both'
    only_df1 = df_combined['_merge'] == 'left_only'
    only_df2 = df_combined['_merge'] == 'right_only'
    summary = {
        'Total Rows': total_rows,
        'Matching Rows': matches.sum(),
        'Rows with Value Differences': value_differences,
        'Only in ' + df1_name: only_df1.sum(),
        'Only in ' + df2_name: only_df2.sum()
    }
    
    return df_combined, summary

# Initialize an empty DataFrame for the summary
summary_df = pd.DataFrame()

# Start comparing each tab and save the results
with pd.ExcelWriter(compare_file, engine='xlsxwriter') as writer:
    for tab in tabs:
        # Read data from each Excel file for the current tab
        df_prod = pd.read_excel(prod_file, sheet_name=tab)
        df_qa = pd.read_excel(qa_file, sheet_name=tab)
        
        # Define key columns for comparison based on the tab
        key_columns = ['mapping_id'] if tab != 'detail_file' else ['mapping_id', 'target_column']
        
        # Compare the dataframes and get summary
        df_compare, summary = compare_dfs(df_prod, df_qa, key_columns)
        
        # Write the comparison result to the new Excel file
        comparison_tab_name = f'{tab}_compare'
        df_compare.to_excel(writer, sheet_name=comparison_tab_name, index=False)
        
        # Accumulate summary data
        summary_df = summary_df.append(pd.DataFrame([summary], index=[tab]))
    
    # Write the summary data to the 'compare_summary' tab
    summary_df.to_excel(writer, sheet_name='compare_summary', index=True)

print("Comparison Excel file with summary tab has been created.")


# In[ ]:




