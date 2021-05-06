def vigenere(key, message):
    encrytxt = ""
    #check if key has only letters
    if not key.isalpha():
        print("ERROR: Key must only contain letters")
        exit()
    #remove all white spaces and capitalize key and message
    message = ''.join(message.split())
    key = key.upper()
    message = message.upper()

    if len(message) <= len(key):
        for i in range(0, len(message)):
            keyChar = ord(key[i])
            msgChar = ord(message[i])
            if not message[i].isalpha():
                encrytxt += chr(msgChar)
            else:
                msgChar = msgChar + (keyChar-65)
                encrytxt += chr(msgChar)
        pass
    else:
        #match key and message length
        key = repeat_to_length(key, len(message))
        #print(key)
        #print(message)
        for i in range(0, len(message)):
            keyChar = ord(key[i])
            msgChar = ord(message[i])
            if not message[i].isalpha():
                encrytxt += chr(msgChar)
            else:
                msgChar = msgChar + (keyChar-65)
                encrytxt += chr(msgChar)


    return encrytxt

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]
