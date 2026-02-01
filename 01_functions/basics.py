# # 1. Max of two numbers

# def max_of_two(a, b):
#     if a > b:
#         return a 
#     return b 


# def sum_of_list(lst):
#     total = 0
#     for i in lst:
#         total += i 
#     return total 


# def count_vowels(s):
#     count = 0 
#     for ch in s.lower():
#         if ch in "ashiseshdsjjhksdlkhwkcbnsdu":
#             count += 1 
#     return count 


# def is_prime(n):
#     if n <= 1:
#         return False 
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True



def change(x):
    x = x + 10
    return x 

a = 5 
b = change(a)
print(a, b) 

# -------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# # End of the File: 01_functions/basics.py