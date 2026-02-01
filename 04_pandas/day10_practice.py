"""
📘 Day 10 – Pandas Data Cleaning & GroupBy Analysis

What I learned today:
1️⃣ Handling Missing Data
   - Detected missing values in DataFrames
   - Used `fillna()` with mean imputation

2️⃣ Data Cleaning
   - Removed duplicate rows using `drop_duplicates()`
   - Ensured dataset consistency

3️⃣ GroupBy Analysis
   - Grouped data using categorical columns
   - Applied aggregate functions (mean, max, min)
   - Compared performance across groups

Focus:
→ Cleaning real-world data before analysis  
→ Using groupby for analytical insights  
→ Building ML-ready datasets
"""

# --------------------------------------------------
# Sample Dataset
# --------------------------------------------------

import pandas as pd

data = {
    "student": ["A", "B", "C", "D", "E"],
    "score":   [85, None, 78, 90, 32],
    "passed":  [True, True, True, True, False]
}

df = pd.DataFrame(data)

print("\n---------------------- Original DataFrame -----------------------------\n")
print(df)

# --------------------------------------------------
# 1. Handling Missing Data
# --------------------------------------------------

df["score"] = df["score"].fillna(df["score"].mean())

print("\n---------------------- After Handling Missing Data -----------------------------\n")
print(df)

# --------------------------------------------------
# 2. Remove Duplicates
# --------------------------------------------------

df = df.drop_duplicates()

print("\n---------------------- After Removing Duplicates -----------------------------\n")
print(df)

# --------------------------------------------------
# 3. GroupBy Analysis
# --------------------------------------------------

result = df.groupby("passed")["score"].agg(["mean", "max", "min"])

print("\n---------------------- GroupBy Analysis (Passed vs Failed) -----------------------------\n")
print(result)

print("\n---------------------- Thank You -----------------------------\n")

# End of the File: 04_pandas/day10_practice.py