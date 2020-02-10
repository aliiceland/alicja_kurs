print(len("Alicja"))

# pobierz napis od uzytkownika - przy pomocy input\
# wypisz dluglosc napisu/ 
# zmien napis na liczbe - co gdy sie nie da, 
# wypisz kwadrat tej liczby

napis = input("wpisz slowo:")
print("dlugosc znakow",len(napis))
print(napis.isnumeric())

if napis.isnumeric():
    print(int(napis)**2)

try: 
    liczba = int(napis)
except ValueError:
    pass
