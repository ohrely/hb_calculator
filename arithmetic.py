def add(list_nums):
    total = 0
    for each_num in list_nums:
        numint = int(each_num)
        total += numint
    return total

def subtract(list_nums):
    total = int(list_nums[0])
    list_nums = list_nums[1:]
    for each_num in list_nums:
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
    list_nums = list_nums[1:]
    for each_num in list_nums:
        numint = float(each_num)
        total /= numint
    return total

def square(each_num):
    return int(each_num)**2

def cube(each_num):
    return int(each_num)**3

def power(list_nums):
    base = int(list_nums[0])
    list_nums = list_nums[1:]
    for each_num in list_nums:
        base = base**int(each_num)
    return base

def mod(list_nums):
    rem = int(list_nums[0])
    list_nums = list_nums[1:]
    for each_num in list_nums:
        rem = rem % int(each_num)
    return rem