import sys
import cryptomath
import random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""


def GetKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return keyA, keyB


def CheckKeys(keyA, keyB):
    if keyA == 1:
        return False
    if keyB == 0:
        return False
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        return False
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        return False
    return True


def AffineCipherEncrypt(message=""""A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""):
    key = random.randint(196, 1000000000)
    n = GetKeyParts
    while not CheckKeys(n):
        key = random.randint(196, 1000000000)
    cipher = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symIndex = SYMBOLS.find(symbol)
            cipher += SYMBOLS[(symIndex * n[0] + n[1]) % len(SYMBOLS)]
        else:
            cipher += symbol
    return cipher


print(AffineCipherEncrypt())
