# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
import math
import time
start_time = time.time()
largeNumber = 600851475143

def prime(n):
    if (n == 2):
        return True
    else:
        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if (n % i == 0):
                return False
        return True

# 7.10111284256
# def largestPrimeFactor(n):
#     primeFactor = 1
#     for i in range(2, int(math.ceil(math.sqrt(n)))):
#         if (prime(i)):
#             if (n % i == 0):
#                 if primeFactor < i:
#                     primeFactor = i
#     return primeFactor

# 7.30380606651
def largestPrimeFactor(n):
    primeFactor = int(math.ceil(math.sqrt(n)))
    i = primeFactor
    flag = 0
    while (flag == 0):
        if (prime(i)):
            if (n % i == 0):
                if i < primeFactor:
                    primeFactor = i
                    flag = 1
        i = i-1
    return primeFactor


print "Largest Factor : ", largestPrimeFactor(largeNumber)
print "Execution time : ", (time.time() - start_time)
