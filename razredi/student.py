class Student():
    def __init__(self,vpisna_st,ime,letnik,ocene={}):
        self.ime = ime
        self.letnik = letnik
        self.ocene = ocene
        self.vpisna_st = vpisna_st
        print(self)

    def oceni(self, predmet, ocena):
        self.ocene[predmet] = ocena

    def napreduj(self):
        self.letnik += 1

        



class Fakulteta():

    def __init__(self,spisek_studentov={}):
        self.spisek_stud = spisek_studentov

    def vpis(self,ime,vpisna_st):
        self.spisek_stud[vpisna_st] = ime
    
    def izpis(self,vpisna_st):
        self.spisek_stud.pop(vpisna_st)


if __name__ == "__main__":
    
    ul = Fakulteta()
    print(ul.spisek_stud)
    ul.vpis("Andrej", 1323113)
    ul.vpis("jan", 453522)
    ul.vpis("erik", 345345)
    ul.vpis("matej", 34534543)
    print(ul.spisek_stud)
    ul.izpis(345345)
    print(ul.spisek_stud)
    
    
    st = Student(112321,"Jan",1)
    st.oceni("ee","7")
    print(st.ocene)
    print(st.letnik)
    st.napreduj()
    print(st.letnik)

    





    
