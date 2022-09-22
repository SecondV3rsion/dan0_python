#!/bin/python

import copy

def main():
    """
    
    #list / seznam
    test = 1
    l1 = [1, "Bostjan" , True, 0.004, test, [1, 2, 0.4]]
    print(l1[2])
    #dodajanje
    l1[2] = "False"
    print(l1[2])
    l1.append(1111)
    print(l1)
    l1.pop()
    print(l1)
    l1.insert(3,"asdas")
    l1.remove(1)
    print(l1.index("asdas"))

    #dictionary / slovar
    d1 = {"ABC": 123, 17:"sedemnajst"}
    print(d1["ABC"])

    d1["nova vredsnot"] = 1231

     #tuple
    t1 = (1, 7 ,4,)
    print(t1)
    """

    l1 = [1, 2, 4]

    l2 = copy.deepcopy(l1)
    l2.append(7)
    print(l1)
    print(l2)



if __name__ == "__main__":
    main()