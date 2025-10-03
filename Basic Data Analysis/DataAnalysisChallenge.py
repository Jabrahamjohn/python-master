import pandas as pd

import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'sales_data.csv'
data = pd.read_csv(file_path)

# Calculate total revenue
total_revenue = data['Revenue ($)'].sum()

# Find the best-selling product
best_selling_product = data.groupby('Product')['Quantity Sold'].sum().idxmax()
best_selling_quantity = data.groupby('Product')['Quantity Sold'].sum().max()

# Identify the day with the highest sales
highest_sales_day = data.groupby('Date')['Revenue ($)'].sum().idxmax()
highest_sales_revenue = data.groupby('Date')['Revenue ($)'].sum().max()

# Save the results to a new file
summary = (
    f"Total Revenue: ${total_revenue:,.2f}\n"
    f"Best-Selling Product: {best_selling_product} ({best_selling_quantity} units sold)\n"
    f"Highest Sales Day: {highest_sales_day} (${highest_sales_revenue:,.2f})\n"
)

with open('sales_summary.txt', 'w') as file:
    file.write(summary)

# Print the insights
print(summary)

# Bonus: Visualize sales trends
plt.figure(figsize=(10, 6))
data.groupby('Date')['Revenue ($)'].sum().plot(kind='bar', color='skyblue')
plt.title('Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_trends.png')
plt.show()