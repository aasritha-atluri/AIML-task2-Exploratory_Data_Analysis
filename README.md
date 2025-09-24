# Task 2 - Exploratory Data Analysis (ML Internship)

This repository contains my solution for **Task 2** of the ML Internship.  
The goal of this task is to perform **Exploratory Data Analysis (EDA)** on the Titanic dataset to understand its structure, relationships, and patterns using statistics and visualizations.

## Requirements
- Python 3.x must be installed on your system.
- Install dependencies before running:

```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn
```
## What I Did
- Loaded and explored the Titanic dataset.
- Generated summary statistics (mean, median, standard deviation, etc.).
- Created histograms and boxplots to visualize the distribution of numeric features.
- Built a correlation heatmap to study relationships between numerical variables.
- Used pairplots to visualize feature relationships by survival status.
- Created an interactive scatterplot using Plotly (Age vs Fare by Survival).
- Identified patterns, trends, and anomalies in the dataset.
- Drew feature-level inferences from the visualizations.

## Key Insights
- **Age**: Most passengers were between 20–40 years; children had relatively higher survival chances.  
- **Fare**: Distribution was skewed with outliers; higher fares were generally associated with higher survival.  
- **Pclass**: Strong negative correlation with Fare; passengers in 1st class paid more and had better survival rates.  
- **Survival**: Higher survival rate among females and first-class passengers.  

## Tools & Libraries
- **Python**
- **Pandas, NumPy** → Data handling and statistics  
- **Matplotlib, Seaborn** → Data visualization  
- **Plotly** → Interactive visualization  
- **Scikit-learn** → For consistency in ML workflows  

## How to Run
1. Clone this repository or download the files.
2. Make sure **Python 3.x** is installed.
3. Install dependencies (see Requirements).
4. Place the raw dataset (`Titanic-Dataset.csv`) in the same folder as `task2code.py`.
5. Run the script:

```bash
python task2code.py
```
6. Several plots and visualizations will be displayed (histograms, boxplots, heatmap, pairplot, scatterplot).
👉 Close any pop-up plot windows to allow the script to continue execution.
