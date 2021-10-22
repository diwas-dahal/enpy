import math


def TranspositionCipher(text, key):
    result = ""
    for i in range(key):
        result += text[i::key]
    return result


def DecryptTranspositionCipher(message, key):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


def DecryptTranspositionCipherBruteForce(text):
    result = []
    for i in range(len(text)):
        result.append([DecryptTranspositionCipher(text, i), i])
    return result
