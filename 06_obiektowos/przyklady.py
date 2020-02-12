class Czlowiek:
    gatunek = "Homo Sapiens"

    def __init__(self, imie):
        self.imie = imie

    @property
    def dlugosc_imienia(self):
        return len(self.imie)

    def __str__(self):
        return f"<Osoba {self.imie}>"
#dziedziczenie
class Pracownik(Czlowiek):

    def __init__(self, imie, stawka):
        super().__init__(imie)
        self.stawka = stawka 

c1=Czlowiek("Alicja")
c2=Czlowiek("Pawel")
#c1.imie = "Alicja"
print(type(c1))
print(c1.imie)
print(c2.imie)
print(c2.gatunek)

Czlowiek.gatunek = "Homo Australopitekus"
print(c2.gatunek)

print(c2.dlugosc_imienia)
print(c1)

#metody

pracownik = Pracownik("alicja",100)

print(pracownik)

