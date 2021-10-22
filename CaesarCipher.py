import random


def CeasarCipher(text, symbolSet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    cipherSymbolSet = symbolSet
    result = ''

    # Generates a random key. Length of cipherSymbolSet  determines the thereshold
    key = random.randint(0, len(cipherSymbolSet))

    for i in text:
        if i != " ":
            indexOfLetter = cipherSymbolSet.find(i)
            # The modulus operator makes sure the index is less than the lenght of cipherSymbolSet
            indexOfLetter = (indexOfLetter + key) % len(cipherSymbolSet)
            result += cipherSymbolSet[indexOfLetter]
        else:
            result += " "
    return (result, key)


def CaesarCipherBruteForce(text, key=None, symbolSet='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'):
    if key is None:
        Value = {}
        for x in range(1, len(symbolSet) + 1):
            result = ""
            for i in text:
                if i != " ":
                    numberOfIndex = symbolSet.find(i)
                    numberOfIndex = (numberOfIndex - x) % len(symbolSet)
                    result += symbolSet[numberOfIndex]
                else:
                    result += " "
            Value[result] = x
        return Value
    else:
        result = ""
        for i in text:
            if i != " ":
                numberOfIndex = symbolSet.find(i) - key
                numberOfIndex = numberOfIndex % len(symbolSet)
                result += symbolSet[numberOfIndex]
            else:
                result += " "
        return result
