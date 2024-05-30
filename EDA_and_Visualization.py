#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random
import plotly.express as px
import plotly.io as pio

def create_sample_dataframe(num_records=100):
    np.random.seed(42)  # For reproducible random results

    data = {
        'accountnumber': np.random.randint(100000, 999999, size=num_records),
        'balance': np.random.uniform(500.0, 20000.0, size=num_records),
        'rate': np.random.uniform(1.5, 18.0, size=num_records),
        'creditCardType': np.random.choice(['Visa', 'MasterCard', 'Amex', 'Discover'], size=num_records),
        'creditLimit': np.random.randint(1000, 20000, size=num_records),
        'Utilization': np.random.uniform(0, 100, size=num_records),
        'originationState': np.random.choice(['NY', 'CA', 'TX', 'FL', 'PA', 'IL', 'OH'], size=num_records),
        'numberOfDaysOpen': np.random.randint(30, 5000, size=num_records),
        'RewardsType': np.random.choice(['Cash Back', 'Points', 'Travel', 'None'], size=num_records)
    }

    df = pd.DataFrame(data)
    return df


# In[3]:


def generate_eda_html(df, output_html='eda_output.html'):
    pio.templates.default = "simple_white"  # Set default theme for plotly

    toc = '<div class="toc"><h4>Table of Contents</h4><ul>'
    html_string = '''
    <html>
    <head>
        <title>Exploratory Data Analysis Report</title>
        <link href="https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i" rel="stylesheet">
        <style>
            body { font-family: 'Roboto', sans-serif; margin: 0; font-size: 16px; color: #333; }
            header { background-color: #2a2a2a; color: #f8f9fa; text-align: center; padding: 20px 0; font-size: 24px; }
            .toc { position: fixed; left: 0; top: 90px; width: 200px; height: calc(100% - 90px); background-color: #f8f9fa; border-right: 1px solid #ccc; padding: 20px; box-sizing: border-box; overflow: auto; }
            #content { margin-left: 220px; padding: 20px; }
            h1 { color: #2a2a2a; border-bottom: 2px solid #ececec; padding-bottom: 5px; margin-top: 20px; }
            h4 { margin-bottom: 10px; color: #444; }
            ul { list-style-type: none; padding: 0; }
            li { margin-bottom: 5px; }
            a { text-decoration: none; color: #337ab7; font-weight: 500; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
    <header>Exploratory Data Analysis: CreditCard Dataset</header>
    <div id="content">
    '''

    # Generate content for each column in the dataframe
    for column in df.columns:
        toc += f'<li><a href="#{column}">{column}</a></li>'
        html_string += f'<h1 id="{column}">{column} - Analysis</h1>'

        if df[column].dtype == 'object' or df[column].dtype.name == 'category':
            value_counts = df[column].value_counts().reset_index()
            value_counts.columns = [column, 'count']
            fig = px.bar(value_counts, x=column, y='count',
                         labels={column: 'Category', 'count': 'Frequency'}, title=f'Categorical Analysis: {column}')
            html_string += fig.to_html(full_html=False, include_plotlyjs='cdn')
        else:
            fig1 = px.histogram(df, x=column, title=f'Numerical Analysis: {column} - Histogram')
            fig2 = px.box(df, x=column, title=f'Numerical Analysis: {column} - Box Plot')
            html_string += fig1.to_html(full_html=False, include_plotlyjs='cdn')
            html_string += fig2.to_html(full_html=False, include_plotlyjs='cdn')

    toc += '</ul></div>'
    html_string = toc + html_string + '</div></body></html>'

    # Save the HTML file
    with open(output_html, 'w') as file:
        file.write(html_string)

    return f'EDA report generated and saved to {output_html}'


# In[4]:


# Usage example:
df = create_sample_dataframe()
result_message = generate_eda_html(df)
print(result_message)


# In[ ]:




