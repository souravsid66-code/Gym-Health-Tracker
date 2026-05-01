"""Sales analysis using numpy and pandas library"""
import pandas as pd
import numpy as np

# 1. Dummy Sales Data banana
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Laptop', 'Mouse'],
    'Quantity': [2, 10, 5, 8, 1, 15],
    'Price_Per_Unit': [50000, 500, 8000, 1500, 52000, 450]
}

# Pandas DataFrame mein convert karna
df = pd.DataFrame(data)

# 2. Total Sales nikalna (NumPy ka use karke logic lagana)
# Har row ke liye: Quantity * Price_Per_Unit
df['Total_Revenue'] = df['Quantity'] * df['Price_Per_Unit']

print("--- Hamara Sales Data ---")
print(df)

# 3. Task: Sabse zyada revenue kis product se aaya?
top_product = df.groupby('Product')['Total_Revenue'].sum().sort_values(ascending=False)

print("\n--- Product wise Total Kamayi ---")
print(top_product)

# Task 1: Filter products with Quantity more than 5
filtered_df = df[df['Quantity'] > 5]

print("\n--- Products jinki Quantity 5 se zyada hai ---")
print(filtered_df)

# Task 2: 10% Discount dena
# Formula: Total_Revenue - (Total_Revenue * 0.10) ya sirf Total_Revenue * 0.9
df['Discounted_Price'] = df['Total_Revenue'] * 0.9

print("\n--- Data with 10% Discount Column ---")
print(df)