
#!/bin/python

import time

def main():
    l1 = [1, 3, 3, 5, 6, 6, 3]

    for i in l1:
        print(i)

    l2 =[vred for vred in l1 if vred > 5]
    print (l2)

    d1 = {1:"a", 2:"b", 3:"c", 4:"d"}
    for _,v in d1.items():
        print(v)
        

    try:
        d0 = 1/0    
    except Exception as e:
        print(e)
    finally:
        print("finsished")

    try:
        while True:
            print("neki")
            time.sleep(1)
    except KeyboardInterrupt:
        print("exiting...")        


if __name__ == "__main__":
    main()