# ==========================================================
# Domino's Pizza Sales Analysis
# Week 1 Internship Project
# ==========================================================

# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns
pd.set_option('display.max_columns', None)

# Load datasets
order_details = pd.read_csv("Dataset/order_details.csv")
pizzas = pd.read_csv("Dataset/pizzas.csv")
pizza_types = pd.read_csv("Dataset/pizza_types.csv", encoding="latin1")

print("✅ Datasets Loaded Successfully!\n")

print("========== ORDER DETAILS ==========")
print(order_details.head())

print("\n========== PIZZAS ==========")
print(pizzas.head())

print("\n========== PIZZA TYPES ==========")
print(pizza_types.head())


# ==========================================================
# DATASET OVERVIEW
# ==========================================================

def dataset_overview(df, name):
    print("\n" + "=" * 60)
    print(f"{name.upper()} DATASET")
    print("=" * 60)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nShape (Rows, Columns):")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

# Display overview
dataset_overview(order_details, "Order Details")
dataset_overview(pizzas, "Pizzas")
dataset_overview(pizza_types, "Pizza Types")


# ==========================================================
# DATA QUALITY CHECK
# ==========================================================

def data_quality(df, name):
    print("\n" + "=" * 60)
    print(f"DATA QUALITY CHECK - {name.upper()}")
    print("=" * 60)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

# Check each dataset
data_quality(order_details, "Order Details")
data_quality(pizzas, "Pizzas")
data_quality(pizza_types, "Pizza Types")


# ==========================================================
# SUMMARY STATISTICS
# ==========================================================

print("\n")
print("=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

print(order_details.describe())
print(pizzas.describe())


# ==========================================================
# DATASET INFORMATION
# ==========================================================

def dataset_info(df, name):
    print("\n" + "=" * 70)
    print(f"{name.upper()} DATASET INFORMATION")
    print("=" * 70)

    print(f"\nShape (Rows, Columns): {df.shape}")

    print("\nColumn Names:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

# Display information for all datasets
dataset_info(order_details, "Order Details")
dataset_info(pizzas, "Pizzas")
dataset_info(pizza_types, "Pizza Types")


# ==========================================================
# DATA QUALITY CHECK
# ==========================================================

def check_quality(df, name):

    print("\n" + "=" * 70)
    print(f"{name.upper()} DATA QUALITY")
    print("=" * 70)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Records:")
    print(df.duplicated().sum())

# Check every dataset
check_quality(order_details, "Order Details")
check_quality(pizzas, "Pizzas")
check_quality(pizza_types, "Pizza Types")


# ==========================================================
# SUMMARY STATISTICS
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY STATISTICS")
print("=" * 70)

print("\nOrder Details")
print(order_details.describe())

print("\nPizzas")
print(pizzas.describe())


# ==========================================================
# DATA CLEANING
# ==========================================================

def clean_dataset(df, name):

    print("\n" + "=" * 70)
    print(f"CLEANING {name.upper()} DATASET")
    print("=" * 70)

    # Remove duplicate rows
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        df.drop_duplicates(inplace=True)
        print(f"Removed {duplicates} duplicate rows.")
    else:
        print("No duplicate rows found.")

    # Check missing values
    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("No missing values found.")
    else:
        print("\nMissing Values:")
        print(missing)

    return df

# Clean each dataset
order_details = clean_dataset(order_details, "Order Details")
pizzas = clean_dataset(pizzas, "Pizzas")
pizza_types = clean_dataset(pizza_types, "Pizza Types")

#MERGE  DATASETS
pizza_sales = pd.merge(
    order_details,
    pizzas,
    on="pizza_id",
    how="left"
)

pizza_sales = pd.merge(
    pizza_sales,
    pizza_types,
    on="pizza_type_id",
    how="left"
)

#VERIFY MERGE
print("\nMerged Dataset")
print(pizza_sales.head())

print("\nShape of Merged Dataset:")
print(pizza_sales.shape)

# ==========================================================
# FEATURE ENGINEERING
# Create Revenue Column
# ==========================================================

pizza_sales["Revenue"] = pizza_sales["quantity"] * pizza_sales["price"]

print("\nRevenue column created successfully!")

print(pizza_sales[["quantity", "price", "Revenue"]].head())

#EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================================
# BUSINESS QUESTION 1
# Which pizzas are ordered the most?
# ==========================================================

top_pizzas = (
    pizza_sales
    .groupby("name")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Best Selling Pizzas")
print(top_pizzas.head(10))

# ==========================================================
# Visualization
# Top 10 Best Selling Pizzas
# ==========================================================

plt.figure(figsize=(12,6))

top_pizzas.head(10).plot(
    kind='bar',
    color='cornflowerblue',
    edgecolor='black'
)

plt.title("Top 10 Best Selling Pizzas", fontsize=16, weight='bold')
plt.xlabel("Pizza Name", fontsize=12)
plt.ylabel("Quantity Sold", fontsize=12)

plt.xticks(rotation=35, ha='right')

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/top_10_best_selling_pizzas.png")

plt.show()


# ==========================================================
# BUSINESS QUESTION 2
# Which Pizza Category is Most Popular?
# ==========================================================

category_sales = (
    pizza_sales
    .groupby("category")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPizza Sales by Category")
print(category_sales)

plt.figure(figsize=(8,6))

category_sales.plot(
    kind='bar',
    color='mediumseagreen',
    edgecolor='black'
)

plt.title("Total Quantity Sold by Pizza Category", fontsize=16, weight='bold')
plt.xlabel("Category")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=0)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/category_sales.png")

plt.show()

# ==========================================================
# BUSINESS QUESTION 3
# Which Pizza Size is Most Popular?
# ==========================================================

size_sales = (
    pizza_sales
    .groupby("size")["quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantity Sold by Pizza Size")
print(size_sales)
# ==========================================================
# Visualization
# Quantity Sold by Pizza Size
# ==========================================================

plt.figure(figsize=(8,5))

size_sales.plot(
    kind="bar",
    color="tomato",
    edgecolor="black"
)

plt.title("Quantity Sold by Pizza Size", fontsize=16, weight="bold")
plt.xlabel("Pizza Size")
plt.ylabel("Quantity Sold")

plt.xticks(rotation=0)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/pizza_size_sales.png")

plt.show()

# ==========================================================
# BUSINESS QUESTION 4
# What is the Revenue of Each Pizza Category?
# ==========================================================

category_revenue = (
    pizza_sales
    .groupby("category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Pizza Category")
print(category_revenue)
# ==========================================================
# Visualization
# Revenue by Pizza Category
# ==========================================================

plt.figure(figsize=(8,6))

category_revenue.plot(
    kind="bar",
    color="royalblue",
    edgecolor="black"
)

plt.title("Revenue by Pizza Category", fontsize=16, weight="bold")
plt.xlabel("Pizza Category")
plt.ylabel("Revenue ($)")

plt.xticks(rotation=0)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/revenue_by_category.png")

plt.show()

# ==========================================================
# BUSINESS QUESTION 5
# Top 10 Revenue Generating Pizzas
# ==========================================================

top_revenue_pizzas = (
    pizza_sales
    .groupby("name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 Revenue Generating Pizzas")
print(top_revenue_pizzas.head(10))
# ==========================================================
# Visualization
# Top 10 Revenue Generating Pizzas
# ==========================================================

plt.figure(figsize=(10,6))

top_revenue_pizzas.head(10).sort_values().plot(
    kind="barh",
    color="darkorange",
    edgecolor="black"
)

plt.title("Top 10 Revenue Generating Pizzas", fontsize=16, weight="bold")
plt.xlabel("Revenue ($)")
plt.ylabel("Pizza Name")

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/top_10_revenue_pizzas.png")

plt.show()


# ==========================================================
# BUSINESS QUESTION 6
# Correlation Between Numerical Columns
# ==========================================================

correlation = pizza_sales[["quantity", "price", "Revenue"]].corr()

print("\nCorrelation Matrix")
print(correlation)
# ==========================================================
# Visualization
# Correlation Heatmap
# ==========================================================

plt.figure(figsize=(6,5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="YlGnBu",
    linewidths=0.5
)

plt.title("Correlation Heatmap", fontsize=16, weight="bold")

plt.tight_layout()

plt.savefig("graphs/correlation_heatmap.png")

plt.show()

# ==========================================================
# BUSINESS QUESTION 7
# Quantity Distribution
# ==========================================================

print("\nQuantity Distribution")
print(pizza_sales["quantity"].describe())
# ==========================================================
# Visualization
# Quantity Distribution
# ==========================================================

plt.figure(figsize=(8,5))

plt.hist(
    pizza_sales["quantity"],
    bins=10,
    color="mediumseagreen",
    edgecolor="black"
)

plt.title("Distribution of Quantity Sold", fontsize=16, weight="bold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig("graphs/quantity_distribution.png")

plt.show()

# ==========================================================
# BUSINESS QUESTION 8
# Revenue Distribution
# ==========================================================

print("\nRevenue Distribution")
print(pizza_sales["Revenue"].describe())

# ==========================================================
# Visualization
# Revenue Distribution
# ==========================================================

plt.figure(figsize=(7,5))

sns.boxplot(
    y=pizza_sales["Revenue"],
    color="skyblue"
)

plt.title("Revenue Distribution", fontsize=16, weight="bold")
plt.ylabel("Revenue ($)")

plt.tight_layout()

plt.savefig("graphs/revenue_distribution_boxplot.png")

plt.show()
