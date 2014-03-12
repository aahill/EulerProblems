#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


i = 999
summation = 0
while i > 0:
    if i%3 and i%5 == 0:
        summation += i
    i-= 1

print summation
    
