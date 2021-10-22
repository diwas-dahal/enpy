
def TranspositionCipher(text, key):
    result = ""
    for i in range(key):
        result += text[i::key]
    return result


def DecryptTranspositionCipher(text, key):
    # original Index == (IndexOfLetter * key) % length of message
    result = [''] * len(text)
    for i in text:
        letterIndex = text.find(i)
        originalIndex = (letterIndex * key) % len(text)
        text = list(text)
        text[letterIndex] = "!"
        text = "".join(text)
        result[originalIndex] = i
    return "".join(result)


def DecryptTranspositionCipherBruteForce(text):
    for i in range(len(text)):
        print(DecryptTranspositionCipher(text, i), i)
