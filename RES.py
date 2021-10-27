import random
import time
import cryptomath


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
        if cryptomath.gcd(e, (p - 1) ** (q - 1)) == 1:
            break

    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    return publicKey, privateKey


print(GenerateKey())
