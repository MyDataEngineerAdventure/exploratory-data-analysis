# -*- coding: utf-8 -*-
"""car_data_dummy_generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HeS9JOZGj3sVhSOXvxjZOGzLy8Rzxm_2
"""

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

# Generate the car data
car_df = generate_car_data()

df.head()
