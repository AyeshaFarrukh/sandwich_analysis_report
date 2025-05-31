import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

# Load dataset
df = pd.read_csv("sandwich.csv")

# --- Descriptive Stats ---
print("Summary Statistics:")
print(df.describe())

# --- Boxplot: Ant Count by Bread ---
plt.figure(figsize=(8, 6))
df.boxplot(column="antCount", by="bread", grid=False)
plt.title("Distribution of Ant Counts by Bread Type")
plt.suptitle("")
plt.xlabel("Bread Type")
plt.ylabel("Ant Count")
plt.tight_layout()
plt.savefig("boxplot_bread.png")

# --- Boxplot: Topping and Butter ---
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
df.boxplot(column="antCount", by="topping", grid=False)
plt.title("Ant Count by Topping")
plt.xlabel("Topping")
plt.ylabel("Ant Count")

plt.subplot(1, 2, 2)
df.boxplot(column="antCount", by="butter", grid=False)
plt.title("Ant Count by Butter")
plt.xlabel("Butter")
plt.tight_layout()
plt.savefig("boxplot_topping_butter.png")

# --- Interaction Plots ---
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.pointplot(data=df, x="bread", y="antCount", hue="butter", ci="sd", dodge=True)
plt.title("Interaction: Bread × Butter")
plt.xlabel("Bread")
plt.ylabel("Mean Ant Count")
plt.tight_layout()
plt.savefig("interaction_bread_butter.png")

plt.figure(figsize=(10, 6))
sns.pointplot(data=df, x="topping", y="antCount", hue="butter", ci="sd", dodge=True)
plt.title("Interaction: Topping × Butter")
plt.xlabel("Topping")
plt.ylabel("Mean Ant Count")
plt.tight_layout()
plt.savefig("interaction_topping_butter.png")

# --- Violin Plot ---
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x="topping", y="antCount", hue="butter", split=True)
plt.title("Violin Plot: Topping × Butter")
plt.xlabel("Topping")
plt.ylabel("Ant Count")
plt.tight_layout()
plt.savefig("violinplot_topping_butter.png")

# --- ANOVA ---
model = ols('antCount ~ C(bread) * C(topping) * C(butter)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Table:")
print(anova_table)

# --- Residual Checks ---
# Shapiro-Wilk test
shapiro_test = stats.shapiro(model.resid)
print("\nShapiro-Wilk Test:")
print(shapiro_test)

# Histogram of residuals
plt.figure(figsize=(10, 4))
sns.histplot(model.resid, kde=True)
plt.title("Histogram of Residuals")
plt.xlabel("Residual")
plt.tight_layout()
plt.savefig("residuals_histogram.png")

# Q-Q plot
sm.qqplot(model.resid, line='s')
plt.title("Q-Q Plot of Residuals")
plt.tight_layout()
plt.savefig("residuals_qqplot.png")
