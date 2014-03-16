#-*- coding: utf-8 -*-
#The sum of the squares of the first ten natural numbers is,

#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquares(n):
    summation = 0
    while n > 0:
        summation += n*n
        n -= 1
    return summation

def squareOfSum(n):
    output = 0
    while n > 0:
        output += n
        n -= 1
    output *= output
    return output

print squareOfSum(100)-sumOfSquares(100)
