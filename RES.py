import random
import time


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


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


def GenerateLargePrime(keySize=1024):
    while True:
        num = random.randrange(2**(keySize - 1), 2**(keySize))
        if num % 2 != 0 and num % 3 != 0:
            if isPrime(num):
                return num


def GenerateKey(KeySize=1024):
    p = GenerateLargePrime(KeySize)
    q = GenerateLargePrime(KeySize)
    n = p * q
    e = None
    while True:
        e = random.randrange(2 ** (KeySize - 1), 2 ** KeySize)
        if gcd(e, (p - 1) ** (q - 1)) == 1:
            break

    d = findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return publicKey, privateKey


print(GenerateKey())
