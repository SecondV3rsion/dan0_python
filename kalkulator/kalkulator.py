#!/bin/python

from ast import While
import time as t


while True:
    rac_ope = input("vnesi racunsko operacijo ( + , - , * , / ) ")
    print("izbrali ste " + str(rac_ope))
    print(type(rac_ope))
    print(rac_ope is not "/")

    while (rac_ope is not "+") and (rac_ope is not '-') and (rac_ope is not '*') and (rac_ope is not '/'):
        print("neznani operator. Izberi se enkrat")
        rac_ope = input("vnesi racunsko operacijo ( + , - , * , / )") 
    


    st1 = input("vnesi prvo stevilko")
    st2 = input("vnesi drugo stevilko")

    if rac_ope is '+':
        print("Rezultat vasih stevil je: " + str(st1 + st2))
    elif rac_ope is '-':
        print("Rezultat vasih stevil je: " + str(st1 - st2))
    elif rac_ope is '*':
        print("Rezultat vasih stevil je: " + str(st1 * st2))
    elif rac_ope is '/':
        print("Rezultat vasih stevil je: " + str(st1 / st2))
    else:
        print("Napacen vnos racusnke operacije")
