"""
napisz kod ktory bedzie przyjmowal od uzytkownika liczby (input) 
Jesli wpiszemy k - to zakonczy dzialanie petli i wypisze srednia z liczb
"""


i, suma = 0,0
while True:
    wartosc = input("Podaj ciag liczb, aby zakonczyc wpisywanie wpisz 'k' ")
    if wartosc == 'k':
        break
    i += 1 
    suma += int(wartosc)

print(f"srednia wartos wynosi: {suma / 1:.2f} ")