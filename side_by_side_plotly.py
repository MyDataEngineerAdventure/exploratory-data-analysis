#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to generate a range of dates
def generate_dates(start_year, end_year):
    return [f"{month:02d}-{year}" for year in range(start_year, end_year+1) for month in range(1, 13)]

# Generating dates from January 2013 to May 2024
dates = generate_dates(2013, 2024)
dates = dates[:-7]  # Remove months after May 2024

# Random data generation
np.random.seed(0)  # Seed for reproducibility
data = {
    'date': dates,
    'source': np.random.choice(['source1', 'source2', 'source3', 'source4', 'source5'], size=len(dates)),
    'product': np.random.choice(['productA', 'productB', 'productC', 'productD', 'productE', 'productF'], size=len(dates)),
    'number_of_accounts': np.random.randint(50, 500, size=len(dates))
}

# Create DataFrame
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2['number_of_accounts'] = df2['number_of_accounts'] * np.random.uniform(0.8, 1.2, size=len(dates))  # Slightly different numbers for comparison

# Creating a subplot with 1 row and 2 columns
fig = make_subplots(rows=1, cols=2, subplot_titles=("DataFrame 1", "DataFrame 2"))

# Adding traces for df1
fig.add_trace(
    go.Scatter(x=df1['date'], y=df1['number_of_accounts'], mode='lines+markers', name='DF1'),
    row=1, col=1
)

# Adding traces for df2
fig.add_trace(
    go.Scatter(x=df2['date'], y=df2['number_of_accounts'], mode='lines+markers', name='DF2'),
    row=1, col=2
)

# Updating layout if necessary
fig.update_layout(title_text="Comparison of DataFrames", height=600, width=1200)

# Export to HTML file
fig.write_html("comparison_plot.html")

print("The plot has been saved as 'comparison_plot.html'.")


# In[6]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to generate a range of dates
def generate_dates(start_year, end_year):
    return [f"{month:02d}-{year}" for year in range(start_year, end_year+1) for month in range(1, 13)]

# Generating dates from January 2013 to May 2024
dates = generate_dates(2013, 2024)
dates = dates[:-7]  # Remove months after May 2024

# Random data generation
np.random.seed(0)  # Seed for reproducibility
data = {
    'date': dates,
    'source': np.random.choice(['source1', 'source2', 'source3', 'source4', 'source5'], size=len(dates)),
    'product': np.random.choice(['productA', 'productB', 'productC', 'productD', 'productE', 'productF'], size=len(dates)),
    'number_of_accounts': np.random.randint(50, 500, size=len(dates))
}

# Create DataFrame
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2['number_of_accounts'] = df2['number_of_accounts'] * np.random.uniform(0.8, 1.2, size=len(dates))  # Slightly different numbers for comparison

# Unique sources and products
sources = ['source1', 'source2', 'source3', 'source4', 'source5']
products = ['productA', 'productB', 'productC', 'productD', 'productE', 'productF']

# Creating the main figure
rows_needed = len(sources) * len(products)  # Calculate the number of rows needed
fig = make_subplots(rows=rows_needed, cols=2, subplot_titles=[f"{s} {p}" for s in sources for p in products for _ in (1, 2)])

current_row = 1
for source in sources:
    for product in products:
        # Filter data for current source and product
        filtered_df1 = df1[(df1['source'] == source) & (df1['product'] == product)]
        filtered_df2 = df2[(df2['source'] == source) & (df2['product'] == product)]

        # Adding traces to the appropriate subplot
        fig.add_trace(
            go.Scatter(x=filtered_df1['date'], y=filtered_df1['number_of_accounts'], mode='lines+markers', name='DF1'),
            row=current_row, col=1
        )
        fig.add_trace(
            go.Scatter(x=filtered_df2['date'], y=filtered_df2['number_of_accounts'], mode='lines+markers', name='DF2'),
            row=current_row, col=2
        )
        
        current_row += 1  # Move to the next row for the next subplot

# Updating layout if necessary
fig.update_layout(title_text="Comprehensive Comparison by Source and Product", height=3000, width=1200)

# Export to HTML file
fig.write_html("comprehensive_comparison_plot.html")

print("The comprehensive plot has been saved as 'comprehensive_comparison_plot.html'.")


# In[7]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Function to generate a range of dates
def generate_dates(start_year, end_year):
    return [f"{month:02d}-{year}" for year in range(start_year, end_year+1) for month in range(1, 13)]

# Generating dates from January 2013 to May 2024
dates = generate_dates(2013, 2024)
dates = dates[:-7]  # Remove months after May 2024

# Random data generation
np.random.seed(0)  # Seed for reproducibility
data = {
    'date': dates,
    'source': np.random.choice(['source1', 'source2', 'source3', 'source4', 'source5'], size=len(dates)),
    'product': np.random.choice(['productA', 'productB', 'productC', 'productD', 'productE', 'productF'], size=len(dates)),
    'number_of_accounts': np.random.randint(50, 500, size=len(dates))
}

# Create DataFrame
df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data)
df2['number_of_accounts'] = df2['number_of_accounts'] * np.random.uniform(0.8, 1.2, size=len(dates))  # Slightly different numbers for comparison

# Unique sources and products
sources = ['source1', 'source2', 'source3', 'source4', 'source5']
products = ['productA', 'productB', 'productC', 'productD', 'productE', 'productF']

# Creating the main figure
rows_needed = len(sources) * len(products)  # Calculate the number of rows needed
fig = make_subplots(rows=rows_needed, cols=2, subplot_titles=[f"{s} {p}" for s in sources for p in products for _ in (1, 2)])

current_row = 1
for source in sources:
    for product in products:
        # Filter data for current source and product
        filtered_df1 = df1[(df1['source'] == source) & (df1['product'] == product)]
        filtered_df2 = df2[(df2['source'] == source) & (df2['product'] == product)]

        # Adding traces to the appropriate subplot
        fig.add_trace(
            go.Scatter(x=filtered_df1['date'], y=filtered_df1['number_of_accounts'], mode='lines+markers', name='DF1', showlegend=False),
            row=current_row, col=1
        )
        fig.add_trace(
            go.Scatter(x=filtered_df2['date'], y=filtered_df2['number_of_accounts'], mode='lines+markers', name='DF2', showlegend=False),
            row=current_row, col=2
        )
        
        current_row += 1  # Move to the next row for the next subplot

# Applying the simple_white theme
fig.update_layout(template="plotly_white", title_text="Comprehensive Comparison by Source and Product", height=3000, width=1200)

# Export to HTML file
fig.write_html("comprehensive_comparison_plot.html")

print("The comprehensive plot has been saved as 'comprehensive_comparison_plot.html'.")


# In[ ]:




