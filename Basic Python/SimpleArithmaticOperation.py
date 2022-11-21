var_1 = float(input("Enter the First Variable: "))
var_2 = float(input("Enter the Second Variable: "))

sumOfVariable = var_1 + var_2
subOfVariable = var_1 - var_2
mulOfVariable = var_1 * var_2
if var_1 == 0 or var_2:
    print(ZeroDivisionError)
divOfVariable = var_1 / var_2
print('The sum of {0} and {1} is {2}'.format(var_1, var_2, sumOfVariable))
print('The subtraction of {0} and {1} is {2}'.format(var_1, var_2, subOfVariable))
print('The product of {0} and {1} is {2}'.format(var_1, var_2, mulOfVariable))
print('The division of {0} and {1} is {2}'.format(var_1, var_2, divOfVariable))
