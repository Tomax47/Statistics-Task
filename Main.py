import Formulas


def switch(formula, repetition):
    if repetition == "n":
        if formula == "1":
            n = int(input("n = "))
            k = int(input("k = "))
            result = Formulas.placement(n, k)
            print("Result = " + str(result))

        elif formula == "2":
            n = int(input("n = "))
            result = Formulas.permutation(n)
            print("Result = " + str(result))

        elif formula == "3":
            n = int(input("n = "))
            k = int(input("k = "))
            result = Formulas.combination(n, k)
            print("Result = " + str(result))

        else :
            print("Invalid input!")

    elif repetition == "y":
        if formula == "1":
            n = int(input("n = "))
            k = int(input("k = "))
            result = Formulas.rep_placement(n, k)
            print("Result = " + str(result))

        elif formula == "2":
            n = int(input("n = "))
            k = int(input("k = "))
            result = Formulas.rep_permutation(n, k)
            print("Result = " + str(result))

        elif formula == "3":
            n = int(input("n = "))
            k = int(input("k = "))
            result = Formulas.rep_combination(n, k)
            print("Result = " + str(result))

        else:
            print("Invalid input!")


formula = input("Please choose a formula\n1- Placement \n2- Permutation\n3- Combination\n> ")
repetition = input("Is repetition allowed [y|n]? ")

switch(formula, repetition)
