def add(list_nums):
    total = 0
    for each_num in list_nums:
        numint = int(each_num)
        total += numint
    return total

def subtract(list_nums):
    total = int(list_nums[0])
    for each_num in list_nums:
        if each_num == list_nums[0]:
            pass
        else:
            numint = int(each_num)
            total -= numint
    return total

def multiply(list_nums):
    total = 1
    for each_num in list_nums:
        numint = int(each_num)
        total *= numint
    return total

def divide(list_nums):
    total = int(list_nums[0])
    for each_num in list_nums:
        if each_num == list_nums[0]:
            pass
        else:
            numint = float(each_num)
            total /= numint
    return total

def square(each_num):
    return int(each_num)**2

def cube(each_num):
    return int(each_num)**3

def power(num1, num2):
    return num1**num2

def mod(num1, num2):
    return num1%num2
