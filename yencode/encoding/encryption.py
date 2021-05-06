import os
import string
import codecs
from rot import encrypt_rot
from atbash import atbash
from reverse import reverse
from vigenere import vigenere

encrytxt=""
flag = os.environ["flag"]
cleartxt = os.environ["sentence"]
key = os.environ["key"]

if flag == "--help":
    pass
elif flag == "rot":
    for i in range(1, 26):
        encrytxt += "Rot"+ str(i) + ":  " + encrypt_rot(i, cleartxt) + "\n"
elif "rot" in flag:
    num = flag.split("rot")
    if 1 <= int(num[1]) <= 25:
        encrytxt = encrypt_rot(num[1], cleartxt)
    else:
        print("error: please only use rot encryption in the range of 1 to 25.")
    #encrytxt = codecs.encode(cleartxt, 'rot_13')

elif flag == "atbash":
    encrytxt = atbash(cleartxt)
elif flag == "reverse":
    encrytxt = reverse(cleartxt)
elif flag == "vigenere-chiffre" or flag == "vc" or flag == "vigenere":
    encrytxt = vigenere(key, cleartxt)
else:
    print("argument not found")


print(encrytxt)


