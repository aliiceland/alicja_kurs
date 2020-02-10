"""
napisz kod sprawdzajacy czy podana liczba jest 
- podzielna przez 2, podzielna przez 3, wieksza niz 15 lub jest to liczba 11 
"""
a = 90 
wynik = a % 2 == 0 and a % 3 == 0 and (a > 15 or a == 11)
print(wynik)

