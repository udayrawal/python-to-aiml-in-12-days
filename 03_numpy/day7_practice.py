"""
📘 Day 7 – NumPy Operations: Broadcasting, Axis & Masking

What I learned today:
1️⃣ Broadcasting
   - Applied scalar operations directly on arrays
   - Understood how NumPy expands values without loops

2️⃣ Axis-Based Operations
   - Used axis=1 for row-wise computations
   - Used axis=0 for column-wise computations
   - Practiced sum and mean across dimensions

3️⃣ Masking & Filtering
   - Created boolean masks using conditions
   - Filtered arrays using masks
   - Used inverted masks (~) for complementary conditions

Focus:
→ Writing loop-free numerical code  
→ Thinking in dimensions and axes  
→ Preparing data efficiently for ML pipelines
"""

# --------------------------------------------------
# 1. Broadcasting with Scalar
# --------------------------------------------------

import numpy as np

data = np.array([10, 20, 30])

print("\n---------------------- Broadcasting with Scalar -----------------------------\n")
print("Original Data:", data)
print("Scaled Data (data * 2):", data * 2)
print("Shifted Data (data + 5):", data + 5)
print("Inverted Data (data - 15):", data - 15)
print("Halved Data (data / 2):", data / 2)

# --------------------------------------------------
# 2. Row & Column Operations (Axis)
# --------------------------------------------------

matrix = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("\n---------------------- Row & Column Operations -----------------------------\n")
print("Original Matrix:\n", matrix)

row_sums = matrix.sum(axis=1)
print("Sum of each row:", row_sums)

col_means = matrix.mean(axis=0)
print("Mean of each column:", col_means)

# --------------------------------------------------
# 3. Masking & Filtering
# --------------------------------------------------

scores = np.array([55, 70, 85, 40, 90, 65])
passed = scores >= 60

print("\n---------------------- Masking & Filtering -----------------------------\n")
print("Scores:", scores)
print("Passed Mask (scores >= 60):", passed)
print("Passed Scores:", scores[passed])
print("Failed Scores:", scores[~passed])

# --------------------------------------------------

print("\n---------------------- Thank You -----------------------------\n")

# -----------------------------------------------------------------------------
# End of the File: 03_numpy/day7_practice.py