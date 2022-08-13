# python prework assignment
# by Yoon Hwa Jeong

# Qustion 1

from re import I
from tkinter import N


def hello_name(user_name):
    print(f"hello_{user_name}!")


# Question 2

def first_odds():
    for i in range(100):
        if i % 2 != 0:
            return i

# Question 3


def max_num_in_list(a_list):
    max_num = None
    for i in a_list:
        if max_num is None or i > max_num:
            max_num = i
    print(max_num)

# Qustion 4

def is_leap_year(a_year):
    boolean = False
    if a_year % 4 == 0:
        if a_year % 100 != 0 or a_year % 400 != 0:
            boolean = True
        else:
            boolean = False
    return boolean

# Question 5???

def is_consecutive(a_list):
    for i,j in a_list:
        if j == i+1:
            boolean = True
        else:
            boolean = False
print(is_consecutive)


