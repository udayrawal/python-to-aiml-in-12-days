"""
🏁 FINAL DAY PROJECT – Student Performance Analysis Pipeline (50 Students)

What this project demonstrates:
- Pandas for tabular data handling
- NumPy for numerical computation
- Data cleaning (missing value handling)
- Feature engineering (total, average, pass/fail)
- OOP-based pipeline design
- ML-ready structured output

This file represents the culmination of the learning journey.
"""

import pandas as pd
import numpy as np


# --------------------------------------------------
# STEP 1: LOAD DATA
# --------------------------------------------------

def load_data():
    """
    Loads raw student data into a Pandas DataFrame.
    Dataset contains 50 students and 3 subjects.
    """
    data = {
        "student": [f"S{i}" for i in range(1, 51)],

        "math": [
            78, 45, None, 88, 60, 72, 91, None, 55, 67,
            84, 76, None, 59, 93, 68, 74, None, 62, 80,
            71, None, 90, 66, 58, 85, None, 77, 69, 92,
            64, 73, None, 88, 70, 61, 95, None, 79, 68,
            82, None, 75, 60, 89, 66, None, 72, 91, 84
        ],

        "science": [
            85, None, 55, 90, 65, 74, 88, None, 60, 70,
            83, None, 68, 57, 94, 72, None, 66, 61, 80,
            73, None, 91, 69, 59, 86, None, 78, 71, 92,
            65, 74, None, 89, 67, 62, 96, None, 81, 70,
            84, None, 76, 63, 90, 68, None, 75, 93, 87
        ],

        "english": [
            88, 40, 60, None, 58, 71, 85, None, 62, 69,
            81, 74, None, 55, 92, 66, None, 63, 59, 78,
            70, None, 89, 67, 60, 83, None, 75, 68, 91,
            64, 72, None, 87, 69, 61, 94, None, 79, 66,
            82, None, 73, 58, 88, 65, None, 71, 90, 85
        ]
    }

    return pd.DataFrame(data)


# --------------------------------------------------
# STEP 2: CLEAN DATA
# --------------------------------------------------

def clean_data(df):
    """
    Handles missing values using column-wise mean imputation.
    This is a standard preprocessing step in EDA & ML pipelines.
    """
    for col in ["math", "science", "english"]:
        df[col] = df[col].fillna(df[col].mean())

    return df


# --------------------------------------------------
# STEP 3: FEATURE ENGINEERING (NumPy)
# --------------------------------------------------

def add_features(df):
    """
    Creates new features using NumPy for performance:
    - total score
    - average score
    - pass/fail classification
    """
    scores = df[["math", "science", "english"]].values  # Convert to NumPy array

    total = np.sum(scores, axis=1)
    average = total / scores.shape[1]

    df["total"] = total
    df["average"] = average
    df["passed"] = df["average"] >= 50

    return df


# --------------------------------------------------
# STEP 4: PIPELINE CLASS (OOP DESIGN)
# --------------------------------------------------

class StudentPipeline:
    """
    End-to-end pipeline that:
    - loads data
    - cleans data
    - engineers features
    """

    def __init__(self):
        self.df = None

    def run(self):
        self.df = load_data()
        self.df = clean_data(self.df)
        self.df = add_features(self.df)
        return self.df


# --------------------------------------------------
# STEP 5: EXECUTION
# --------------------------------------------------

if __name__ == "__main__":
    pipeline = StudentPipeline()
    final_data = pipeline.run()

    print("\n================ FINAL ML-READY DATA =================\n")
    print(final_data.head(10))  # Show first 10 rows

    print("\nDataset Shape:", final_data.shape)
    print("\nPassed Students:", final_data["passed"].sum())
    print("Failed Students:", (~final_data["passed"]).sum())

    print("\n================ THANK YOU =================\n")


# ----------------------------------------------------------------------------------------

# End of the File: projects/day12_pipeline.py