"""
DAY 1 – FUNCTIONS (FOUNDATION)

QUESTIONS COVERED TODAY:
1. Average of a list
2. Reverse a string
3. Factorial of a number
4. Palindrome check

WHAT I LEARNED TODAY:
- How to define and call functions
- Difference between print() and return
- How function execution flow works
- How to break a problem into input → logic → output
- Writing clean, reusable logic using functions
"""

# --------------------------------------------------
# 1. Average of a List
# --------------------------------------------------

def average_of_list(lst):
    if len(lst) == 0:
        return 0

    total = 0
    for i in lst:
        total += i

    return total / len(lst)


# --------------------------------------------------
# 2. Reverse a String
# --------------------------------------------------

def reverse_string(s):
    reversed_str = ""
    for ch in s:
        reversed_str = ch + reversed_str
    return reversed_str


# --------------------------------------------------
# 3. Factorial of a Number
# --------------------------------------------------

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# --------------------------------------------------
# 4. Palindrome Check
# --------------------------------------------------

def is_palindrome(s):
    s = s.lower()
    reversed_s = ""

    for ch in s:
        reversed_s = ch + reversed_s

    return s == reversed_s


# --------------------------------------------------
# TESTING (Optional – for self-check)
# --------------------------------------------------

if __name__ == "__main__":
    print("Average:", average_of_list([10, 20, 30]))
    print("Reverse:", reverse_string("Python"))
    print("Factorial:", factorial(5))
    print("Palindrome:", is_palindrome("Madam"))