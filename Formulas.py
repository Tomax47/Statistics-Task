import math


# NO REPETITION :

# Placement
def placement(n, k):
    numerator = do_factorial(n)
    denominator = do_factorial((n - k))
    result = numerator / denominator

    return result


# Permutation
def permutation(number):
    result = do_factorial(number)

    return result


# Combination

def combination(n, k):
    numerator = do_factorial(n)
    denominator = do_factorial(k) * do_factorial((n - k))
    result = numerator / denominator

    return result


# WITH REPETITION

# Placement
def rep_placement(n, k):
    result = math.pow(n, k)

    return result


# Permutation
def rep_permutation(n, k):
    denominator = 1
    for i in k:
        denominator *= do_factorial(i)
    return do_factorial(n) // denominator


# Combination
def rep_combination(n, k):
    numerator = do_factorial(n + k - 1)
    denominator = do_factorial(k) * do_factorial(n - 1)
    return numerator // denominator


# Calculating the n!
def do_factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1

    return result
