#!/usr/bin/env python
# coding: utf-8

# ## Generate Dummy Data

# In[1]:


import pandas as pd
import numpy as np
import random

def generate_car_data(num_rows=1000):
    # Seed for reproducibility
    np.random.seed(42)

    # Sample data
    makes = ['Toyota', 'Honda', 'Ford', 'Tesla', 'Chevrolet']
    models = ['Model A', 'Model B', 'Model C', 'Model D', 'Model E']
    fuel_types = ['Petrol', 'Diesel', 'Electric', 'Hybrid']
    colors = ['White', 'Black', 'Red', 'Blue', 'Silver']
    is_imported_options = [True, False]

    # Generating DataFrame
    df = pd.DataFrame({
        'Car ID': np.arange(1, num_rows + 1),
        'Make': np.random.choice(makes, num_rows),
        'Model': np.random.choice(models, num_rows),
        'Year': np.random.randint(1990, 2023, size=num_rows),
        'Engine Size (L)': np.round(np.random.uniform(1.0, 5.0, size=num_rows), 2),
        'Fuel Type': np.random.choice(fuel_types, num_rows),
        'Mileage (km)': np.random.randint(0, 300000, size=num_rows),
        'Price': np.random.randint(5000, 80000, size=num_rows),
        'Color': np.random.choice(colors, num_rows),
        'Is Imported': np.random.choice(is_imported_options, num_rows)
    })

    return df


# In[2]:


df = generate_car_data()


# In[3]:


df.head()


# # Define a function to calculate EDA metrics for each column

# In[4]:


def eda_summary(df):
    eda_df = pd.DataFrame({
        'column_name': df.columns,
        'number_of_distinct_values': [df[col].nunique() for col in df.columns],
        'count_of_null': [df[col].isnull().sum() for col in df.columns],
        'count_of_not_null': [df[col].notnull().sum() for col in df.columns],
        'percentage_of_null': [df[col].isnull().mean() * 100 for col in df.columns],
        'percentage_of_not_null': [df[col].notnull().mean() * 100 for col in df.columns],
        'top_5_values': [df[col].value_counts().head(5).index.tolist() for col in df.columns]
    })
    return eda_df

# Apply the function to the DataFrame
eda_results = eda_summary(df)
eda_results.head(20)


# In[ ]:




