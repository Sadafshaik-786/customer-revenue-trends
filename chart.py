# chart.py
# Customer Analytics: Monthly Revenue Trend Analysis
# Email: 23f3002689@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")  # Larger fonts for presentations

# Generate synthetic monthly revenue data
np.random.seed(42)
months = pd.date_range(start="2024-01-01", end="2024-12-31", freq="MS")
segments = ["Retail", "Corporate", "Online"]

data = []
for segment in segments:
    base = np.random.uniform(80, 120) * 1000
    seasonal_pattern = [
        np.sin((i / 12) * 2 * np.pi) * np.random.uniform(0.05, 0.15) 
        for i in range(12)
    ]
    revenue = [base * (1 + sp) + np.random.normal(0, 3000) for sp in seasonal_pattern]
    for m, r in zip(months, revenue):
        data.append({"Month": m, "Segment": segment, "Revenue": r})

df = pd.DataFrame(data)

# Create the lineplot
plt.figure(figsize=(8, 8))  # For 512x512 pixels at dpi=64
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    hue="Segment",
    marker="o",
    palette="Set2",
    linewidth=2.5
)

# Customize chart
plt.title("Monthly Revenue Trends by Customer Segment (2024)", fontsize=18, fontweight="bold")
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue (USD)", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Save exactly 512x512 pixels
plt.savefig("chart.png", dpi=64)  # Removed bbox_inches to avoid trimming
plt.close()
