"""
DAY 2 – FUNCTIONS (CONTROL & CLARITY)

QUESTIONS COVERED TODAY:
1. Power function with default arguments
2. Finding minimum and maximum together
3. Counting occurrences using keyword arguments
4. Normalize a list (mean-based normalization)

WHAT I LEARNED TODAY:
- How default arguments give control and flexibility
- How keyword arguments improve clarity
- How a function can return multiple values
- How variable scope works inside functions
- Why pure functions are important for ML-style thinking
"""

# --------------------------------------------------
# 1. Power Function (Default Arguments)
# --------------------------------------------------

def power(base, exp=2):
    """
    Returns base raised to the power exp.
    Default exponent is 2 (square).
    """
    return base ** exp


# --------------------------------------------------
# 2. Min and Max of a List (Multiple Returns)
# --------------------------------------------------

def min_max(lst):
    """
    Returns minimum and maximum value from a list.
    """
    if len(lst) == 0:
        return None, None

    minimum = lst[0]
    maximum = lst[0]

    for i in lst:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i

    return minimum, maximum


# --------------------------------------------------
# 3. Count Occurrences (Keyword Arguments)
# --------------------------------------------------

def count_occurrences(lst, target):
    """
    Counts how many times target appears in lst.
    """
    count = 0
    for i in lst:
        if i == target:
            count += 1
    return count


# --------------------------------------------------
# 4. Normalize a List (Pure Function)
# --------------------------------------------------

def normalize_list(lst):
    """
    Normalizes values by subtracting the mean.
    """
    if len(lst) == 0:
        return []

    mean = sum(lst) / len(lst)
    normalized = []

    for x in lst:
        normalized.append(x - mean)

    return normalized


# --------------------------------------------------
# SELF TESTING (OPTIONAL)
# --------------------------------------------------

if __name__ == "__main__":
    print("Power:", power(5))
    print("Power custom:", power(2, 3))

    mn, mx = min_max([10, 5, 20, 3])
    print("Min:", mn, "Max:", mx)

    print("Count:", count_occurrences(lst=[1, 2, 2, 3, 2], target=2))
    print("Normalized:", normalize_list([10, 20, 30]))