####rot#en#und#decryption############################################################################################

def encrypt_rot(n, message):
    txt=""
    ls = []
    for letter in message:
        if str(letter).isdigit():
            ls.append(letter)
        if 65 <= ord(letter) <= 90:
            newLetter = ord(letter) - int(n)
            if newLetter >= 65:
                ls.append(chr(newLetter))
            else:
                newLetter = chr(91 - (65 - newLetter))
                ls.append(newLetter)
        elif 97 <= ord(letter) <= 122:
            newLetter = ord(letter) - int(n)
            if newLetter >= 97:
                ls.append(chr(newLetter))
            else:
                newLetter = chr(123 - (97 - newLetter))
                ls.append(newLetter)
    for element in ls:
        txt+=element

    return txt
