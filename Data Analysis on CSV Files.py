import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file
df = pd.read_csv("sales_data.csv")   # ensure file is in same folder

# 2. Display first 5 rows
print("First 5 rows of data:")
print(df.head())

# 3. Basic info
print("\nDataFrame Info:")
print(df.info())
print("\nShape of DataFrame:", df.shape)

# 4. Group by Product and calculate total sales
product_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:\n", product_sales)

# 5. Group by Region and calculate total sales
region_sales = df.groupby("Region")["Sales"].sum()
print("\nTotal Sales by Region:\n", region_sales)

# 6. Visualization
plt.figure(figsize=(8,5))
product_sales.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar", color="orange", edgecolor="black")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# 7. Filter rows - Example: sales > 1000
high_sales = df[df["Sales"] > 1000]
print("\nRows with Sales > 1000:\n", high_sales)