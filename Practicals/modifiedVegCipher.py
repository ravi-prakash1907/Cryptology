## Requires Library
import numpy as np

## Modified Vigenere's Table
def vigenerTable():
  table = np.zeros(shape=(10,10), dtype='uint64')

  for n in range(10):
    row = []
    for i in range(10):
      row.append((i+n)%10)
    table[n] = row

  return table

## Encryption
def encrypt(message, key):
  textLen = len(message)
  keyLen = len(key)
  
  table = vigenerTable()

  cipherText = ""
  for pos in range(textLen):
    
    colNum = int(message[pos])
    rowNum = int(key[pos % keyLen])

    codeChar = table[colNum, rowNum]
    if (pos+1)%2 == 0:
      codeChar = table[codeChar, rowNum]
    
    cipherText += str(codeChar)
  return cipherText

## Decryption
def decrypt(cipherText, key):
  textLen = len(cipherText)
  keyLen = len(key)
  
  table = vigenerTable()

  message = ""
  for pos in range(textLen):
    rowNum = int(key[pos % keyLen])
    colVal = int(cipherText[pos])
    row = list(table[rowNum])

    plain = row.index(colVal)
    if (pos+1)%2 == 0:
      plain = row.index(plain)
    
    message += str(plain)
  
  return message


######################################################
######################################################


## IMPLEMENTATION
plainText = str(pow(10,16))
key = '0433'

# Encryption
cipherText = encrypt(plainText, key)
print("After Enctryption: \n \
1. Plaintext: {}\n 2. Key: {} \n\n\
=> Ciphertext: {}".format(plainText, key, cipherText))

# Decryption
message = decrypt(cipherText, key)
print("\n\nAfter Dectryption: \n \
1. Ciphertext: {}\n 2. Key: {} \n\n\
=> Retrieved Plaintext: {}".format(cipherText, key, message))

print("\n"+"="*40)
# Varification
print("\nWhether actual & retrived messages are same?", end="  ")
print('Yes' if plainText == message else 'No')
