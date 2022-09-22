#!/bin/python

import time as t
a = 54
b = 82

print("Sestevek je:" + str(a+b))

if a>b:
    print("a je vecji od b")
elif a<b:
    print("b vecji od a")
else:
    print("noben pogoj ni izpolnjen")

while True:
    a += 1
    print("a: " + str(a))
    #t.sleep(0.1)
    if a>b:
        break


vhod = input("vnesi najlubjso stevilko")
print("tvoja stevilka je:" + str(vhod))