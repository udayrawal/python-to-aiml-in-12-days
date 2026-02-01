"""
📘 Day 11 – Pandas EDA Mini Project with Feature Engineering

Objective:
- Perform Exploratory Data Analysis (EDA)
- Handle missing values
- Engineer new features (total, average, pass/fail)
- Identify top and weak performing students

Dataset:
- Rows represent students
- Columns represent subject scores
"""

import pandas as pd

# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

data = {
    "student": [f"S{i}" for i in range(1, 31)],

    "math": [78, 45, 62, None, 90, 55, 67, 88, 72, 60,
             85, None, 49, 91, 73, 68, 54, 80, None, 66,
             77, 59, 82, 44, 95, 70, 58, None, 64, 86],

    "science": [85, 50, None, 70, 92, 60, 74, 89, 78, None,
                88, 65, 52, 94, None, 71, 57, 83, 69, 76,
                81, None, 86, 48, 96, 73, 61, 79, None, 90],

    "english": [88, 40, 55, 65, None, 58, 70, None, 75, 62,
                84, 60, None, 91, 68, 73, 56, None, 64, 71,
                79, 59, 85, None, 93, 67, 60, 74, None, 88],

    "physics": [80, None, 60, 68, 91, 57, 72, 86, None, 64,
                83, 69, 50, 92, 66, None, 55, 79, 70, 75,
                None, 58, 84, 46, 94, 71, 62, None, 67, 89],

    "chemistry": [76, 48, None, 66, 89, 54, 69, None, 73, 61,
                  82, 67, None, 90, 65, 70, 53, None, 68, 74,
                  78, 56, 83, None, 92, 69, 59, 72, None, 87],

    "computer": [82, 55, 65, None, 93, 60, 71, 88, 76, None,
                 85, 68, 58, 94, None, 73, 62, 81, 69, 77,
                 None, 64, 86, 52, 96, 74, 66, None, 70, 90],

    "statistics": [75, None, 58, 64, 88, 52, None, 84, 70, 61,
                   80, 66, None, 89, 63, 68, 50, None, 65, 72,
                   76, 54, 81, None, 91, 67, 57, 73, None, 86]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 2. Initial EDA
# --------------------------------------------------

print("\n================ DATASET OVERVIEW ================\n")
print(df.head())
print("\nShape:", df.shape)
print("\nInfo:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# 3. Handling Missing Values (Mean Imputation)
# --------------------------------------------------

subjects = ["math", "science", "english", "physics",
            "chemistry", "computer", "statistics"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# --------------------------------------------------
# 4. Feature Engineering
# --------------------------------------------------

# Total score across all subjects
df["total"] = df[subjects].sum(axis=1)

# Average score
df["average"] = df["total"] / len(subjects)

# Pass/Fail condition
df["passed"] = df["average"] >= 50

print("\n================ FEATURE ENGINEERED DATA ================\n")
print(df.head())

# --------------------------------------------------
# 5. GroupBy Analysis
# --------------------------------------------------

group_result = df.groupby("passed")[subjects].mean()

print("\n================ GROUPBY ANALYSIS (PASSED VS FAILED) ================\n")
print(group_result)

# --------------------------------------------------
# 6. Top & Weak Student Identification
# --------------------------------------------------

top_student = df.loc[df["average"].idxmax()]
weak_student = df.loc[df["average"].idxmin()]

print("\n================ TOP STUDENT ================\n")
print(top_student)

print("\n================ WEAK STUDENT ================\n")
print(weak_student)

print("\n================ THANK YOU ================\n")

# ------------------------------------------------------------------------------------------

# End of the File: 04_pandas/day11_practice.py