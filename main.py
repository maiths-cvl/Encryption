# ask you to enter the  you want to encrypt
text = str(input("Enter the  you want to encrypt : "))
key = str(input("Enter the key : "))

keyList = key.split(",")

count = len(keyList)

try:
    for i in range(len(keyList)):
        keyList[i] = int(keyList[i])
except IOError:
    print('Something aint right : ' + IOError)
finally:
    pass

for i in range(len(keyList)):
    while keyList[i] > 26:
        keyList[i] - 26

print(keyList)

#set to lower case everything in the 

text = text.lower()

textList = []

# alphabet dictionaries
#alpahbetCaps = {' ' : 0,'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
KeysAlphabetLower = {' ' : 0, 'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
ValuesAlphabetLower = {0 : ' ', 1 : 'a', 3 : 'c', 2 : 'b', 5 : 'e', 4 : 'd', 7 : 'g', 6 : 'f', 9 : 'i', 8: 'h', 11: 'k', 10 : 'j', 13 : "m", 12 : 'l', 15 : 'o', 14 : 'n', 17 : 'q', 16 : 'p', 19 : 's', 18 : 'r', 21 : 'u', 20 : 't', 23 : 'w', 22 : 'v', 25: 'y', 24 : 'x', 26: 'z'}

for i in range(len(text)):
    textList.append(text[i])

def encryption(word):
    for i in range(len(ValuesAlphabetLower)):
        if ValuesAlphabetLower[i] == word:
            print("i found it : " + str(i))
            break


encryption(textList[0])