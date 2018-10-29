#!/usr/bin/env python3
# usage : python3 transform.py ARGS file


from random import shuffle, choice; 
import sys, argparse
from dictionnaries import *

def traiteC(string:str)->str:
    'return the modified string w/ Cyrillic and Greek letters'
    nstr=''
    for j in range(len(string)):
        letter=string[j]
        shuffle(lisDico)
        for i in range(len(lisDico)):
            if letter in lisDico[i]:
                nstr+=lisDico[i][letter]
                break
        else:
            nstr+=letter
    return nstr

def traiteZ(string:str)->str:
    'retrun the string w/ zwj and zwnj'
    nstr=''
    for j in range(len(string)):
        letter=string[j]
        nstr+=letter
        try:
            if letter.isalpha() and string[j+1].isalpha:
                nstr+=choice(lisInvisible)
        except IndexError:
            pass
    return nstr

def traiteD(string:str)->str:
    'return the string with digits modified'
    nstr=''
    for letter in string:
        if letter in dicoDigits:
            nstr+=dicoDigits[letter]
        else:
            nstr+=letter
    return nstr

def traiteUnicode(string:str)->str:
    "return the string modified with any unicode similar character"
    nstr=""
    for letter in string:
        if letter in dicoUnicode:
            nstr+=choice(dicoUnicode[letter])
        else:
            nstr+=letter
    return nstr



if __name__=="__main__":

    parser=argparse.ArgumentParser(description="Print out the text file using different characters",  usage="Usage : python transform.py ARGS file", epilog="version 1.0")
    parser.add_argument('file', nargs="?", help="encoded in UTF-8")
    # group = parser.add_mutually_exclusive_group()
    parser.add_argument('-c', dest="c", default=False, help="Latin letters remplaced by Greek and Cyrillic letters",action="store_true")
    parser.add_argument('-z', dest="z", default=False, help="add zero width joiner/non-joiner",action="store_true")
    parser.add_argument('-d', dest="d", default=False, help="digits remplacement",action="store_true")
    parser.add_argument('--all', dest="allp", default=False, help="all parameters",action="store_true")
    parser.add_argument('--unicode', dest="unicode", default=False, help="all unicode confusable chars",action="store_true")
    args=parser.parse_args()
    
    if len(sys.argv)<3:
        parser.print_help()
        sys.exit(1)
    try:
        txt=open(args.file).read()
    except:
        print("Can't open '{}'".format(args.file))
        sys.exit(1)
    # print(args.__dict__)

    if args.unicode:
        txt=traiteUnicode(txt)
        print(txt)
        sys.exit(0)
    if args.allp:
        txt=traiteC(traiteD(traiteZ(txt)))
    else:
        if args.c:
            txt=traiteC(txt)
        if args.z:
            txt=traiteZ(txt)
        if args.d:
            txt=traiteD(txt)
    print(txt[:])