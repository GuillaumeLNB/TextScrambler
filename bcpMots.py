#!/usr/bin/env python3
# usage : python3 CyrillicLetters.py
# les clefs sont en latin

from random import shuffle, choice; 
import sys, argparse
from dictionnaries import *
from transform import *

if __name__=="__main__":

    # parser=argparse.ArgumentParser(description="Récrit le texte en utilisant d'autres codes de carctères et/ou les zwj-zwnj")
    # parser.add_argument('file', nargs="?", help="fichier")
    # parser.add_argument('-c', dest="c", default=False, help="Cyrillic : mettre l'option si on ne veut pas",action="store_true")
    # parser.add_argument('-z', dest="z", default=False, help="zero width joiner/non-joiner",action="store_true")
    # parser.add_argument('-d', dest="d", default=False, help="other digits",action="store_true")
    # parser.add_argument('--all', dest="allp", default=False, help="all parameters",action="store_true")
    # args=parser.parse_args()
    # try:
    #     txt=open(args.file).read()
    # except:
    #     print("Impossible d'ouvrir le fichier '{}'".format(args.file))
    #     sys.exit(1)
    # # print(args.__dict__)

    # if len(sys.argv)<3:
    #     parser.print_help()
    #     sys.exit(1)


    # if args.allp:
    #     txt=traiteC(traiteD(traiteZ(txt)))
    # else:
    #     if args.c:
    #         txt=traiteC(txt)
    #     if args.z:
    #         txt=traiteZ(txt)
    #     if args.d:
    #         txt=traiteD(txt)
    # print(txt[:])
    mot=sys.argv[1]
    lis=[]
    # while True:
    for _ in range (1000):
        mot=traiteC(mot)
        mot=traiteZ(mot)
        if mot not in lis: 
            lis.append(mot)
            print(mot)
            # if input()=="":
            #     continue
            # else:
            #     break

    # pprint(lis)