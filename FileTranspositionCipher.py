import TranspositionCipher
import os
import sys
import time
import random


def encryptFile(filePath=None):
    if not os.path.exists(filePath):
        print("The file does not exist.")
        sys.exit()

    fileObject = open(filePath, 'r')
    fileContent = fileObject.read()
    fileObject.close()

    fileObject = open(filePath, 'w')
    startTime = time.time()
    key = random.randint(2, len(fileContent) + 2)
    encryptedContent = TranspositionCipher.TranspositionCipher(
        fileContent, key)
    fileObject.write(encryptedContent)

    totalTime = round(time.time() - startTime, 2)
    fileObject.close()

    print("File successfully encrypted.")
    print(f"Encryption Time: {totalTime}")
    print(
        f"The file was encrypted using TranspositionCipher. The key used for encryption was {key}")


def RemoveNonLetters(text):
    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
    lettersOnly = []
    for symbol in text:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly.append(symbol)
    return ''.join(lettersOnly)


def isEnglish(message):
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = None
        dictionaryFile.close()

    message = message.upper()
    message = RemoveNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0

    matches = 0
    for words in possibleWords:
        if words in englishWords:
            matches += 1
    percentage = float(matches / len(possibleWords))
    wordsMatch = percentage * 100 >= 20
    numletters = len(RemoveNonLetters(message))
    messageLetterPercentage = (float(numletters) / len(message)) * 100
    lettersMatch = messageLetterPercentage >= 80
    return wordsMatch and lettersMatch


def decryptFileBruteForce(filePath=None):
    if not os.path.exists(filePath):
        print("The file does not exist.")
        sys.exit()

    fileObject = open(filePath, 'r')
    fileContent = fileObject.read()
    fileObject.close()

    decryptedContent = TranspositionCipher.DecryptTranspositionCipherBruteForce(
        fileContent)
    for x in decryptedContent:
        print(x[1])
        if isEnglish(x[0]):
            print("file decrypted")
            print(f"Possible key : {x[1]}")
            fileObject = open(filePath, 'r')
            fileObject.write(x[0])
            fileObject.close()
            sys.exit()


def decryptFile(filePath, key):
    print("Verifying  File Location ....")
    if not os.path.exists(filePath):
        print("The file does not exist.")
        sys.exit()
    print("File's location verified")

    print("Reading File's content...")
    fileObject = open(filePath, 'r')
    fileContent = fileObject.read()
    fileObject.close()

    print("Decrypting File ...")
    decryptedContent = TranspositionCipher.DecryptTranspositionCipher(
        fileContent, key)
    fileObject = open(filePath, 'w')
    fileObject.write(decryptedContent)
    fileObject.close()

    print("File decrypted Succesfully")
    print(f"Key : {key}")
