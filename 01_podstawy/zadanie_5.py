"""
napisz kod ktory na podstawie wprowadzinych wymiarow opakowania (prostopadloscian) 
obliczy i sprawdzi czyobjetosc jest wieksza od jednego litra ( w cm, 1l = 1000 cm3)
V= a*b*h
"""

a=10
b=12
h=8 

objetosc = a * b* h 

if objetosc > 1000:
    print("Objetosc wieksza niz 1L")
else: print("Objetosc mniejsza niz 1L")

a, b, h = 100, 12, 8

objetosc = a * b* h 

if objetosc > 1000:
    print("Objetosc wieksza niz 1L")
elif objetosc > 2000: # elif -> dodanie kolejnego rozdzielnego warunku, moznaa dodawac ich duzo
    print("Objetosc wieksza niz 2L")
else: print("Objetosc mniejsza niz 1L")

