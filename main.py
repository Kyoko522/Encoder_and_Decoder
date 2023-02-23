def main():
    userinput = int(input("""\nWhat do you want to do:
1. Encode a message
2. Decode a message
"""))
    if userinput == 1:
        Secret_Messages_encryption()
    elif userinput == 2:
        Secret_Messages_decryption()
def Secret_Messages_encryption():
    text = input("Enter your text to Encrypt: ")
    encodedText = ""
    shiftvalue = int(input("Enter your encryption key number (1-26): "))
    shiftvalue = shiftvalue%6
    # this list interates throught the string (str) text and stores each character as the variable text
    for letter in text:
        numOfLetter = ord(letter)
        encodedNumOfLetter = numOfLetter + shiftvalue

        if ord(letter) >= 65 and ord(letter)<=90:
            if encodedNumOfLetter > 90:
                encodedNumOfLetter -= 26
            elif encodedNumOfLetter > 122:
                encodedNumOfLetter -= 26
            encodedText += chr(encodedNumOfLetter)
        elif ord(letter) >= 97 and ord(letter)<= 122:
            if encodedNumOfLetter > 90 and encodedNumOfLetter < 97:
                encodedNumOfLetter -= 26
            elif encodedNumOfLetter > 122:
                encodedNumOfLetter -= 26
            encodedText += chr(encodedNumOfLetter)
        else:
            encodedText += letter

    print ("The encrypted message is: "+ encodedText)
    main()
def Secret_Messages_decryption():
    text = input("Enter your text to decrypt: ")
    decodedText = ""
    shiftvalue = int(input("Enter your encryption key number (1-26): "))
    shiftvalue = shiftvalue % 6
    # this list interates throught the string (str) text and stores each character as the variable text
    for letter in text:
        numOfLetter = ord(letter)
        decodedNumOfLetter = numOfLetter - shiftvalue

        if ord(letter) >= 65 and ord(letter)<=90:
            if decodedNumOfLetter > 65 and decodedNumOfLetter <= 60:
                decodedNumOfLetter += 26
            elif decodedNumOfLetter > 97:
                decodedNumOfLetter += 26
            decodedText += chr(decodedNumOfLetter)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            if decodedNumOfLetter > 65 and decodedNumOfLetter <= 60:
                decodedNumOfLetter += 26
            elif decodedNumOfLetter < 97:
                decodedNumOfLetter += 26
            decodedText += chr(decodedNumOfLetter)
        else:
            decodedText += letter

    print("The encrypted message is: " + decodedText)
    main()

if __name__ == "__main__":
    main()