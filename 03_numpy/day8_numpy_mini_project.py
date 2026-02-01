"""
📘 Day 8 – NumPy Mini Project: Student Performance Analysis

Objective:
- Analyze student performance using NumPy
- Practice axis-based operations
- Identify top performers
- Apply normalization for ML readiness

Dataset Description:
- Rows → Students
- Columns → Subjects
- Shape → (30 students × 7 subjects)
"""

import numpy as np

# --------------------------------------------------
# Dataset Creation
# Rows = students, Columns = subjects
# --------------------------------------------------

scores = np.array([
    [78,72,69,75,80,74,71],
    [85,81,79,82,88,83,80],
    [67,64,61,70,68,65,62],
    [92,89,90,88,94,91,89],
    [73,70,68,72,75,71,69],
    [88,85,84,86,90,87,85],
    [60,58,55,62,61,59,57],
    [79,76,74,78,82,77,75],
    [83,80,79,81,85,82,80],
    [69,66,64,68,70,67,65],
    [91,88,87,89,93,90,88],
    [74,72,70,73,76,74,71],
    [66,63,60,65,67,64,62],
    [87,84,82,85,89,86,84],
    [71,69,67,70,73,71,68],
    [95,92,94,91,96,93,92],
    [58,55,53,60,59,57,54],
    [81,78,76,80,83,79,77],
    [76,74,72,75,78,76,73],
    [84,82,80,83,87,84,81],
    [63,60,58,62,64,61,59],
    [89,86,85,87,91,88,86],
    [72,70,68,71,74,72,69],
    [65,62,60,64,66,63,61],
    [90,88,89,87,92,90,88],
    [77,75,73,76,79,77,74],
    [68,65,63,67,69,66,64],
    [86,83,82,84,88,85,83],
    [74,72,70,73,76,74,71],
    [82,80,78,81,85,82,79]
])

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------

print("\n====================== DATASET OVERVIEW =========================")
print(f"Total Students: {scores.shape[0]}")
print(f"Total Subjects: {scores.shape[1]}")

# --------------------------------------------------
# Student-wise Analysis
# Axis = 1 → Row-wise → Per student
# --------------------------------------------------

student_avg = scores.mean(axis=1)

print("\n====================== STUDENT-WISE ANALYSIS ======================")
for i, avg in enumerate(student_avg):
    print(f"Student {i:02d} → Average Score: {avg:.2f}")

# --------------------------------------------------
# Subject-wise Analysis
# Axis = 0 → Column-wise → Per subject
# --------------------------------------------------

subject_avg = scores.mean(axis=0)

print("\n====================== SUBJECT-WISE ANALYSIS ========================")
for i, avg in enumerate(subject_avg):
    print(f"Subject {i+1} → Average Score: {avg:.2f}")

# --------------------------------------------------
# Top Performer Identification
# --------------------------------------------------

top_idx = np.argmax(student_avg)

print("\n====================== TOP PERFORMER ================================")
print(f"Top Student Index: {top_idx}")
print(f"Top Student Average Score: {student_avg[top_idx]:.2f}")

# --------------------------------------------------
# Passing Analysis
# Criteria: Average score ≥ 50
# --------------------------------------------------

passed_mask = student_avg >= 50

print("\n====================== PASSING ANALYSIS ===============================")
print(f"Students Passed (Average ≥ 50): {np.sum(passed_mask)} / {scores.shape[0]}")

# --------------------------------------------------
# Normalization (Z-score)
# Used in ML preprocessing
# --------------------------------------------------

mean = scores.mean()
std = scores.std()
normalized_scores = (scores - mean) / std

print("\n====================== NORMALIZATION ===================================")
print("Mean after normalization (≈0):", normalized_scores.mean().round(4))
print("Std after normalization (≈1):", normalized_scores.std().round(4))

print("\n====================== THANK YOU ======================================\n")

# --------------------------------------------------
# End of File 03_numpy/day8_numpy_mini_project.py
