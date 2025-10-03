# Ubuntu-Inspired Data Analysis: Exploring the Iris Dataset
# This script loads, analyzes, and visualizes the classic Iris dataset using pandas and matplotlib.
# It embodies the spirit of Ubuntu by sharing insights from a communal dataset contributed to the public domain.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For enhanced styling (optional, but improves aesthetics)
import numpy as np
from urllib.error import URLError
import warnings
warnings.filterwarnings('ignore')  # Suppress minor warnings for cleaner output

# Set style for better-looking plots
plt.style.use('seaborn-v0_8')  # Requires seaborn; fallback to default if not installed
sns.set_palette("husl")

# Task 1: Load and Explore the Dataset
print("=== Task 1: Loading and Exploring the Iris Dataset ===")

# URL for the Iris dataset (publicly available from UCI ML Repository)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# Column names for the dataset
columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

try:
    # Load the dataset using pandas
    df = pd.read_csv(url, names=columns)
    print("Dataset loaded successfully!")
    print(f"Dataset shape: {df.shape}")
    
    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Explore structure: data types and missing values
    print("\nData types:")
    print(df.dtypes)
    
    print("\nMissing values:")
    print(df.isnull().sum())
    
    # Clean the dataset (Iris has no missing values, but check and handle if any)
    if df.isnull().sum().sum() > 0:
        print("\nCleaning missing values...")
        df = df.dropna()  # Drop rows with missing values
        print(f"Dataset shape after cleaning: {df.shape}")
    else:
        print("\nNo missing values found. Dataset is clean.")
    
except URLError as e:
    print(f"Error loading dataset from URL: {e}")
    print("Please ensure you have internet access or download the file manually.")
    # Fallback: Create a small sample dataset if loading fails
    print("Using a sample Iris dataset as fallback.")
    data = {
        'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4, 4.6, 5.0, 4.4, 4.9],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1],
        'petal_length': [1.4, 1.4, 1.3, 1.5, 1.4, 1.7, 1.4, 1.5, 1.3, 1.5],
        'petal_width': [0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1],
        'species': ['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa']
    }
    df = pd.DataFrame(data)
    print(f"Sample dataset shape: {df.shape}")
    print(df.head())

# Task 2: Basic Data Analysis
print("\n=== Task 2: Basic Data Analysis ===")

# Compute basic statistics for numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
print("\nBasic statistics for numerical columns:")
print(df[numerical_cols].describe())

# Perform grouping: Mean of numerical columns by species
print("\nMean values of numerical features by species:")
grouped = df.groupby('species')[numerical_cols].mean()
print(grouped)

# Identify patterns or interesting findings
print("\n=== Findings and Observations ===")
print("1. The Iris dataset contains measurements of sepal and petal dimensions for three species: Setosa, Versicolor, and Virginica.")
print("2. Setosa species has the smallest petal dimensions on average, making it easily distinguishable.")
print("3. Virginica tends to have the largest sepal and petal lengths, indicating size-based clustering.")
print("4. There is low variance in Setosa measurements, suggesting uniformity within the species.")
print("5. Petal length shows the most differentiation across species, useful for classification.")

# Task 3: Data Visualization
print("\n=== Task 3: Data Visualizations ===")

# Ensure we have enough data for full visualizations (use full dataset if loaded)
if len(df) < 10:  # If fallback sample, note limitation
    print("Note: Using sample data; visualizations are illustrative.")

# 1. Line Chart: Trends over sample index (simulating a sequence or trend in measurements)
plt.figure(figsize=(10, 6))
sample_index = range(len(df))
plt.plot(sample_index[:50], df['sepal_length'][:50], marker='o', label='Sepal Length Trend')  # First 50 samples for clarity
plt.title('Line Chart: Trend in Sepal Length Over Sample Index')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 2. Bar Chart: Comparison of average petal length across species
plt.figure(figsize=(8, 6))
species_means = df.groupby('species')['petal_length'].mean()
species_means.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Bar Chart: Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8, 6))
plt.hist(df['sepal_width'], bins=20, edgecolor='black', alpha=0.7, color='purple')
plt.title('Histogram: Distribution of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 4. Scatter Plot: Relationship between sepal length and petal length
plt.figure(figsize=(8, 6))
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['petal_length'], c=colors.get(species, 'gray'), label=species, alpha=0.7)
plt.title('Scatter Plot: Sepal Length vs. Petal Length by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print("\nAll visualizations generated successfully!")
print("This analysis highlights the Iris dataset's utility in demonstrating species differentiation through floral measurements.")
print("In the spirit of Ubuntu, this shared dataset fosters collaborative learning in data science.")