# 🐜 Sandwich Ant Attraction Analysis

This project explores whether different types of sandwiches attract ants differently, based on factors like bread type, topping, and presence of butter. The analysis was conducted as part of the MSc Data Science application project for TU Dortmund (Winter Semester 2025/2026).

## 📁 Dataset

- **File**: `sandwich.csv`
- **Variables**:
  - `antCount`: Number of ants observed
  - `bread`: Type of bread (Whole Grain, Multi Grain, Rye, White)
  - `topping`: Sandwich topping (Ham and gherkins, Peanut butter, Yeast spread)
  - `butter`: Butter used (yes/no)

## 📊 Objective

To determine:
- If bread type, topping, and butter have a significant effect on ant attraction
- Which combination attracts the most ants

## 🧪 Methodology

- Descriptive Statistics
- Visualization (Boxplots, Violin plots, Interaction plots)
- Full Factorial ANOVA using Python
- Assumption checks (Shapiro–Wilk test, residual plots)

## 🛠️ Tools & Libraries

- Python 3
- pandas
- matplotlib
- seaborn
- statsmodels
- scipy

## 📂 Files

- `sandwich.csv` – Dataset
- `sandwich_analysis_report.py` – Full Python script to reproduce analysis
- `report.pdf` – Final 10-page written report (optional to add)

## 📷 Output Plots

Saved automatically by the script:
- `boxplot_bread.png`
- `boxplot_topping_butter.png`
- `interaction_bread_butter.png`
- `interaction_topping_butter.png`
- `violinplot_topping_butter.png`
- `residuals_histogram.png`
- `residuals_qqplot.png`

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/sandwich-ant-analysis.git
   cd sandwich-ant-analysis
