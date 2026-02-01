"""
📘 Day 6 – NumPy Basics: Arrays, Shapes & Vectorized Operations

What I learned today:
1️⃣ NumPy Arrays
   - Created arrays using np.array, np.zeros, and np.ones
   - Understood why NumPy arrays are faster than Python lists

2️⃣ Shapes & Dimensions
   - Worked with 2D arrays (matrices)
   - Used `.shape` to understand data structure

3️⃣ Vectorized Operations
   - Performed element-wise addition, subtraction, division
   - Used dot product for vector math
   - Learned how NumPy avoids loops (vectorization)

4️⃣ Data Normalization (Foundation for ML)
   - Calculated mean of data
   - Centered data using mean subtraction

Focus:
→ Thinking in arrays, not loops  
→ Understanding shapes before models  
→ Building ML-ready numerical intuition
"""

# --------------------------------------------------
# 1. Create NumPy Arrays
# --------------------------------------------------

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.zeros(5)
c = np.ones(5)

print("\n---------------------- NumPy Arrays -----------------------------\n")
print("Array a:", a)
print("Array b (zeros):", b)
print("Array c (ones):", c)

# --------------------------------------------------
# 2. Shape Practice
# --------------------------------------------------

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("\n---------------------- Matrix Shape -----------------------------\n")
print("Matrix:\n", matrix)
print("Shape of matrix:", matrix.shape)

# --------------------------------------------------
# 3. Vector Operations
# --------------------------------------------------

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("\n---------------------- Vector Operations -----------------------------\n")
print("Vector x:", x)
print("Vector y:", y)
print("Addition (x + y):", x + y)
print("Subtraction (x - y):", x - y)
print("Dot Product (x · y):", np.dot(x, y))
print("Division (x / y):", x / y)

# --------------------------------------------------
# 4. Simple Normalization
# --------------------------------------------------

data = np.array([10, 20, 30, 40, 50])

mean = data.mean()
normalized = data - mean

print("\n---------------------- Normalization -----------------------------\n")
print("Original Data:", data)
print("Mean:", mean)
print("Normalized Data:", normalized)

print("\n---------------------- Thank You -----------------------------\n")

# -------------------------------------------------------------------------------
# End of the File: 03_numpy/day6_practice.py

