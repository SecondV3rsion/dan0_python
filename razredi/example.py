


class Pravokotnik(object):
    barva = "rdeca"
    def __init__(self, a, b):
        print("sem nov pravokotnik")
        self.a = a
        self.b = b

    def __del__(self):
        print("brisem pravokotnik")

    def ploscina(self):
        return self.a * self.b

    def obseg(self):
        return 2*self.a + 2*self.b

class Kvadrat(Pravokotnik):
    def __init__(self, a):
        super(Kvadrat,self).__init__(a, a)

if __name__ == "__main__":
    prav1 = Pravokotnik(5.0, 4.0)
    prav2 = Pravokotnik(6.0, 2.0)
    kv1 = Kvadrat(4.0)
    print(kv1.ploscina())

    print(prav1.ploscina())
    print(prav1.obseg())