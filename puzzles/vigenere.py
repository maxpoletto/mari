#!/opt/local/bin/python

# Implements Vigenère cipher.

import argparse

tr = {}
def init():
    for i in range(0, 26): # a..z
        tr[chr(97+i)] = ""
        for j in range(0, 26):
            tr[chr(97+i)] += chr(97+(i+j)%26)

def Encrypt(cleartext, key):
    i = 0
    out = ""
    for c in cleartext:
        if c == ' ':
            out = out + ' '
            continue
        k = key[i]
        d = tr[k][ord(c)-97]
        out += d
        i = (i+1) % len(key)
    return out

def Decrypt(cyphertext, key):
    i = 0
    out = ""
    for c in cyphertext:
        if c == ' ':
            out = out + ' '
            continue
        k = key[i]
        s = tr[k]
        j = 0
        for c2 in s:
            if c2 == c:
                out += chr(97+j)
                break
            j = j+1
        i = (i+1) % len(key)
    return out

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', default='', help='Input cleartext or cyphertext')
parser.add_argument('-k', '--key', default='', help='Key')
parser.add_argument('-e', '--encrypt', default='yes', help='Encrypt yes/no')
args = parser.parse_args()

init()
if args.encrypt == "yes":
    print(Encrypt(args.text, args.key))
else:
    print(Decrypt(args.text, args.key))
