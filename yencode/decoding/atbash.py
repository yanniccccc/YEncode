####ATBASH###########################################################################################################

def atbash(message):
    nmLetter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    backLetter = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
    txt=""
    ls = []
    message = message.lower()
    for letter in message:
        if str(letter).isdigit() or letter == " ":
            ls.append(letter)
        for i in range(0, 26):
            if nmLetter[i] == letter:
                ls.append(backLetter[i])
    for element in ls:
        txt+=element

    return txt

