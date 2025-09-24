# Task 2 - Exploratory Data Analysis (ML Internship)
# Requirements:
# pip install pandas numpy matplotlib seaborn plotly scikit-learn
#ignore this if they are already present.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("titanic.csv")

# Summary statistics
print("Summary Statistics:\n", df.describe(include="all"))

# Histograms for numerical columns
df.hist(figsize=(12, 8))
plt.suptitle("Histograms of Numeric Features")
plt.show()

# Boxplots for numeric columns
for col in ["Age", "Fare"]:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Pairplot for selected features
sns.pairplot(df[["Age", "Fare", "Pclass", "Survived"]], hue="Survived")
plt.show()

# Interactive plot (Plotly)
fig = px.scatter(df, x="Age", y="Fare", color="Survived",
                 title="Age vs Fare by Survival")
fig.show()

print("EDA complete. Check visualizations above.")

