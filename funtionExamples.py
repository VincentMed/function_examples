# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:13:37 2022

@author: Vincent Medrano
"""

'''
Examples of functions
'''

def my_function():
    print("Hello From My Function!")

#call the function    
my_function()

#------------------------------------

#function has two args
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    
my_function_with_args("Vincent", "a Merry fucking christmas")

#-----------------------------------

def sum_two_numbers(a, b):
    #return a + b
    return a + b

#Returns 15
sum_two_numbers(10, 5)

#---------------------------------------

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

#----------------------------------------

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

