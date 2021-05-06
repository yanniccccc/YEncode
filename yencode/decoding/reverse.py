####REVERSE###########################################################################################################

def reverse(message):
    txt=""
    ls = []
    message = message.lower()
    for i in range(len(message)-2,-1,-1):
        txt += message[i]
    return txt
