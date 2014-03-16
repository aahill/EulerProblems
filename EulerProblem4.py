#A palindromic number reads the same both ways. The largest palidrome made from the
#product of two 2-digit numbers is 9009 = 91x99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def getNextPalindrome(num):
    #in the interest of manipulating the overall number of digits, the next palindrome is constructed as a string,
    #and converted and returned as an integer 
    nextNum = ''
    #case for if the number contains an even number of digits
    if len(str(num)) %2 == 0:
        # if middle values > 1, subtract from both values
        if int(str(num)[(len(str(num))/2)-1]) > 1 and int(str(num)[(len(str(num))/2)]) > 1:
            for i in range(0,(((len(str(num)))/2)-1)):
                nextNum += str(num)[i]
            for i in range((((len(str(num)))/2)-1),(((len(str(num)))/2)+1)):
                nextNum += str(int(str(num)[i]) - 1)
            for i in range((((len(str(num)))/2)+ 1),len(str(num))):
                nextNum += str(num)[i]
            return int(nextNum)
    # if middle values = 1, subtract leftmost value
        if len(str(num)) %2 == 0 and int(str(num)[(len(str(num))/2)-1]) == 1 and int(str(num)[(len(str(num))/2)]) == 1:
            for i in range(0,(((len(str(num)))/2)-1)):
                    nextNum += str(num)[i]
            nextNum += '9'
            for i in range((((len(str(num)))/2)+ 1),len(str(num))):
                    nextNum += str(num)[i]
            return int(nextNum)
    #case for if the number contains an odd number of digits
    if len(str(num)) %2 != 0:
        if int(str(num)[((len(str(num)))/2)]) > 0:
            for i in range(0,((len(str(num))/2))):
               nextNum += str(num)[i]
            nextNum+= str((int(str(num)[((len(str(num)))/2)]))-1)
            for i in range(((len(str(num))/2)+1),len(str(num))):
                nextNum += str(num)[i]
            return int(nextNum)
        #the case for if the middle digit is 0 
        if int(str(num)[((len(str(num)))/2)]) == 0:
            # all digits from 0 to the mid-length -1 are kept as-is
            for i in range (0,(len(str(num))/2)-1):
                nextNum+= str(num)[i]
            # the digit before the midlength is subtracted by 1
            nextNum+= str(int((str(num))[((len(str(num))/2))-1])-1)
            # the middle digit is appended as a 9
            nextNum+='9'
            # to keep the number a palindrome, the following number is the same as the digit at 1 minus the midlength
            nextNum += str(int((str(num)[((len(str(num)))/2)+1]))-1)
            # the following digits are kept as is
            for i in range((len(str(num))/2)+2,(len(str(num)))):
                nextNum += str(num)[i]
            return int(nextNum)

#999*999 = 998001, the largest palindrome smaller then this is 997799
upperBoundry = 997799
#100*100 = 1000, the smallest palindrome larger then this is 1001
lowerBoundry = 1001

i = upperBoundry
returnValue1 = 0
#gets the palindromes factors, determines if any factors are three digit numbers, and if so,
#divides the palindrome by the factor. if the following number is also three-digits long,
#the palindrome is returned.
while i > lowerBoundry and returnValue1 == 0:
    n = factors(i)
    for facs in n:
        if len(str(facs)) == 3:
            if len(str(i/facs)) == 3:
                returnValue1 = facs
                print 'the largest palindrome created by two three-digit nums is: ',i,',',' which is created by ',returnValue1,' and ', i/returnValue1
                break
    i = getNextPalindrome(i)
                                                                              
