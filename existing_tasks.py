import Formulas

def no_repetition_formula(n, m, k):
    numerator = Formulas.combination(m, k)
    denominator = Formulas.combination(n, k)
    probability = numerator / denominator

    print(str(numerator)+"/"+str(denominator))
    return probability


def with_repetition_formula(n, m, k, r):
    numerator = Formulas.rep_combination(m, r) * Formulas.rep_combination((n - m), (k - r))
    denominator = Formulas.rep_combination(n, k)
    probability = numerator / denominator

    print(str(numerator) + "/" + str(denominator))
    return probability


# Task №1
# Formula > P() = C(k,m) / C(k,n) > No Repetition

no_repetition_formula(15, 10, 3)

# print(no_repetition_formula(15, 10, 3))

print()

# Task №2
# Formula > P(A) = C(r,m) * C(k-r, n-m)/C(k,n) > With repetition

with_repetition_formula(25, 10, 8, 3)

# print(with_repetition_formula(25, 10, 8, 3))