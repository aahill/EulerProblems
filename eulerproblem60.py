#The primes 3, 7, 109, and 673, are quite remarkable.
#By taking any two primes and concatenating them in any order the result will always be prime.
#For example, taking 7 and 109, both 7109 and 1097 are prime.
#The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from collections import defaultdict

def isPrime(n):
    """
    this method determines if a number is prime or not
    input: n -> an integer who's prime nature is to be determined
    output: true if n is prime, false if n is not prime
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            break
    return True

def getNextPrime(num):
    """
    this method gets the next largest prime number after num
    input -> num, an integer representing the number to get the next num of
    output -> an int containing the next largest prime number
    """
    foundPrime = False
    if num < 2:
        n = num + 1
    else:
        n = num + 2
    while foundPrime == False:
        if isPrime(n):
            foundPrime = True;
            return n
        else:
            n += 1
            
def concatsArePrime(x,y):
    """
    checks to see if the concatenations in any order are prime
    input -> x,y integers to be concatenated
    output -> true if the concatenations of the numbers are primes, otherwise false
    """
    concat1 = int(str(x)+str(y))
    concat2 = int(str(y)+str(x))
    if isPrime(concat1) and isPrime(concat2):
        return True
    else:
        return False

def generatePrimes(dictionary,numList,upperLimit):
    """
    generates prime numbers from 3 to a given upperLimit, finds the prime numbers
    that concatenate to form primes themselves, and appends them into a dictionary
    input ->
    dictionary, a dictionary to hold the primes,
    numList, an empty list to append prime
    upperLimit, an integer to determine the upper limit of the primes generation
    output -> a dictionary containing prime values 
    """
    upperLimit = upperLimit
    initialVal = 3
    while initialVal < upperLimit:
        i2 = 3
        while i2 < upperLimit:
            if concatsArePrime(initialVal,i2):
                numList.append(i2)
                try:
                    dictionary[initialVal].append(i2)
                except KeyError:
                    dictionary[initialVal] = [i2]
            i2 = getNextPrime(i2)
        initialVal = getNextPrime(initialVal)
        print initialVal
    print "primes generated"

def getKeyValues(dictionary,key):
    """
    gets the values of a key in a dictionary, and returns them in a list
    input ->
    dictionary, a dictionary
    key, the key for which to get the associated values
    output -> a list of values for the specified key
    """
    lis = dictionary[key]
    return lis 

def isValueKeyValue(dictionary,value,key):
    """
    checks to see if a given value is included in a dictionary key's values
    input:
    dictionary -> the dictionary to be checked
    value -> the value to be checked
    key -> the key the value will be checked under
    """
    if value in getKeyValues(dictionary,key):
        return True
    else:
        return False

def addAll(lis):
    """
    adds all the number in a list together
    input -> a list
    output -> an integer representing the combined numbers of the list
    """
    finalSum = 0
    for i in finalAnswer:
        finalSum += i
    return finalSum
        


def doProb(primes):
    """
    coding that solves Euler problem #60 through use of set intersection and
    a dictionary containing prime numbers and their concatanatable primes
    input -> primes, a dictionary of primes and their concatanatable primes
    output-> a list containing the first 5 primes to solve Euler Problem 60    
    """
    for key in numList:
        tempList = []
        li1 = getKeyValues(primes,key)
        for prime in li1:
            tempList.append(key)
            tempList.append(prime)
            li2 = getKeyValues(primes,prime)
            intersection = list(set(li1) & set(li2))
            if intersection >= 4 and len(tempList) < 6:
                for x in intersection:
                    li3 = intersection
                    li3.remove(x)
                    for m in li3:
                        if concatsArePrime(m,x): 
                            tempList.append(x)
                            tempList.append(m)                          
                            li3.remove(m)
                            for a in li3:
                                if concatsArePrime(a,m) and concatsArePrime(a,x):
                                    tempList.append(a)
                                    return tempList
                            if m in tempList:
                                tempList.remove(m)
                            if x in tempList:
                                tempList.remove(x)
                         
numList = []    
primeDict = {}
generatePrimes(primeDict,numList,9000)
finalAnswer = doProb(primeDict)
print 'the found primes are: ',finalAnswer
print 'the sum is: ',addAll(finalAnswer)


    
            
            
    
