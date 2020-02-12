"""
Napisz funkcje max_difference ktora przyjmie liste liczb i zwroci najwieksza roznice pomiedzy nimi.
przyklad:
    max_difference([1,11,9,10,8]) ==10
"""
"""
def max_difference(lista):
    i, suma = 0,0
    while True:
        wartosc = input("Podaj ciag liczb, aby zakonczyc wpisywanie wpisz 'k' ")
        if wartosc == 'k':
            break
        i += 1 
        min_ =  min(int(wartosc))
        max_ =  max(int(wartosc))
        roznica = (max_ - min_)
    print(f"roznica {func.__name__}:",roznica)
    return roznica

max_difference() 
"""
#def foo():
    #return 10 

#wczesniej przygotowac trzeba liste 'lista' liczb
def max_difference(lista):
    if lista:
        return max(lista) - min(lista)
    return 0


#print(__name__)
if __name__ == "__main__": 
    print("wykonuje testy")
    assert max_difference([]) == 0
    assert max_difference([1]) == 0
    assert max_difference([1,2]) == 1
    print("jest ok")
