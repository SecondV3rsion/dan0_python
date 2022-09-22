#!/bin/python

import copy
import time

def find_name(d,l):
    im_za_klic = [(ime,st, ) for ime, st in d.items() if ime[0] == l] 
    return im_za_klic





def main():
    imenik = {"Ana":12321, "Boris":123213, "Anabel":21321,"Andrej":702134,"Jan":39122}
    crka = input("crka po kateri hoces iskat")
    print(find_name(imenik,crka))


if __name__ == "__main__":
    main()