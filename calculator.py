"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

""" PUT signature here later"""

while True:
    math_line = raw_input("> ")
    split_input = math_line.split()

    operator = split_input[0]
    numbers_list = split_input[1:]
    print numbers_list
    # num1 = int(split_input[1])
    # num2 = int(split_input[2])

    if operator == "+":
        sum = add(numbers_list)
        print sum
    elif operator == "-":
        diff = subtract(numbers_list)
        print diff
    elif operator == "*":
        product = multiply(numbers_list)
        print product
    elif operator == "/":
        divved_value = divide(numbers_list)
        print divved_value
    elif operator == "square":
        for each_num in numbers_list:
            squared_value = square(each_num)
            print "The squared value of {} is {}.".format(each_num, squared_value)
    elif operator == "cube":
        for each_num in numbers_list:
            cubed_value = cube(each_num)
            print "The cubed value of {} is {}.".format(each_num, cubed_value)
    # elif operator == "pow":
    #     raised_value = power(num1,num2)
    #     print raised_value
    # elif operator == "%":
    #     remainder = mod(num1,num2)
    #     print remainder
    # else:
    #     print "Invalid Input!"
