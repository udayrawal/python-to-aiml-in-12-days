"""
📘 Day 9 – Pandas Fundamentals & DataFrame Operations

What I learned today:
1️⃣ Creating DataFrames
   - Built a DataFrame from a Python dictionary
   - Understood column-based data structure

2️⃣ Filtering Data
   - Applied conditional filtering on DataFrames
   - Selected rows based on column conditions

3️⃣ Adding New Columns
   - Created derived columns using logical conditions
   - Stored boolean results directly in DataFrame

4️⃣ Basic Statistical Operations
   - Calculated mean, maximum, and minimum values
   - Performed column-wise analysis using Pandas

Focus:
→ Working with tabular data efficiently  
→ Preparing datasets for analysis and ML  
→ Understanding Pandas as a higher-level data tool over NumPy
"""

# --------------------------------------------------
# 1. Create DataFrame
# --------------------------------------------------

import pandas as pd

data = {
    "student": ["A", "B", "C", "D", "E"],
    "score":   [85, 92, 78, 90, 88]
}

df = pd.DataFrame(data)

print("\n---------------------- Original DataFrame -----------------------------\n")
print(df)

# --------------------------------------------------
# 2. Filter Passed Students
# --------------------------------------------------

passed = df[df["score"] >= 50]

print("\n---------------------- Passed Students -----------------------------\n")
print(passed)

# --------------------------------------------------
# 3. Add Result Column
# --------------------------------------------------

df["result"] = df["score"] >= 50

print("\n---------------------- DataFrame with Result Column -----------------------------\n")
print(df)

# --------------------------------------------------
# 4. Basic Statistics
# --------------------------------------------------

mean_score = df["score"].mean()
max_score = df["score"].max()
min_score = df["score"].min()

print("\n---------------------- Basic Statistics -----------------------------\n")
print("Mean Score:", mean_score)
print("Max Score:", max_score)
print("Min Score:", min_score)

print("\n---------------------- Thank You -----------------------------\n")

# -----------------------------------------------------------------------------
# End of the File: 04_pandas/day9_practice.py

