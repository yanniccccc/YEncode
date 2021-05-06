def decrypt_rot(n, message):
    txt=""
    ls = []
    for letter in message:
        if str(letter).isdigit():
            ls.append(letter)
        if 65 <= ord(letter) <= 90:
            newLetter = ord(letter) + int(n)
            if newLetter <= 90:
                ls.append(chr(newLetter))
            else:
                print(newLetter)
                newLetter = chr(64 + newLetter % 90)
                ls.append(newLetter)
        elif 97 <= ord(letter) <= 122:
            newLetter = ord(letter) + int(n)
            if newLetter <= 122:
                ls.append(chr(newLetter))
            else:
                newLetter = chr(96 + newLetter % 122)
                ls.append(newLetter)
    for element in ls:
        txt+=element

    return txt
