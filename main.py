import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

# Load data
data = pd.read_csv("data/sales_data.csv")

# Handle missing values
data.fillna(0, inplace=True)

# --- Analysis ---
# Total sales per product
sales_per_product = data.groupby("Product")["Sales"].sum()

# Best-selling product
best_product = sales_per_product.idxmax()

# Total and average sales
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()

# Print results
print(f"Total Sales: {total_sales}")
print(f"Average Sales: {average_sales}")
print(f"Best-Selling Product: {best_product}")

# --- Bar Chart ---
plt.figure(figsize=(8,6))
sales_per_product.plot(kind="bar", color="skyblue")
plt.title("Sales by Product")
plt.ylabel("Total Sales")
plt.xlabel("Product")
plt.savefig("charts/sales_by_product.png")
plt.close()

# --- Line Chart (Monthly Sales Trend) ---
monthly_sales = data.groupby("Month")["Sales"].sum()
plt.figure(figsize=(8,6))
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month")
plt.savefig("charts/monthly_sales_trend.png")
plt.close()

# --- Pie Chart ---
plt.figure(figsize=(6,6))
sales_per_product.plot(kind="pie", autopct='%1.1f%%')
plt.title("Product Sales Distribution")
plt.ylabel("")
plt.savefig("charts/product_distribution_pie.png")
plt.close()
