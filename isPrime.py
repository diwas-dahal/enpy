import random
import time


def isPrime(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s//2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)

        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

# For small primes (2 <= num <= 100 billion) [Execution Time : 0.0009484291076660156]


def PrimeLL(num):
    for i in range(2, int((num ** 0.5) + 1)):
        if num % i == 0:
            return False
    return True
