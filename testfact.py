# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 10:43:04 2023

@author: crazy
"""

'''
# Recursive Fibonacci

def fibonacci(n):
    # base case
    if n == 0 or n == 1:
        return n
    # recursive case
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    # error case
    else:
        print("Fibonacci numbers begin at 0.")
        return
    
print(fibonacci(47))
''' 

# Fibonacci w. memoization

list_Fib = [None] * 1000
list_Fib[0] = 0
list_Fib[1] = 1

def memo_fib(n):
    if list_Fib[n] is not None:
        return list_Fib[n]          # return the memoized value
    else:
        list_Fib[n] = memo_fib(n-1) + memo_fib(n-2) #calculate the value and memoize it
        return list_Fib[n]
    
print(memo_fib(999))