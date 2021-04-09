#Chudnovsky
from decimal import *

#Sets decimal to 25 digits of precision
getcontext().prec = 150

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)


def chudnovskyBig(n): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi
print ("\t\t\t Chudnovsky")
#\t\t\t Plouff \t\t Bellard 
for i in range(1,75):
    print ("No ",i, " ", chudnovskyBig(i))