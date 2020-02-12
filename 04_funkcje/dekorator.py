import time

def zmierz_czas(func):
    def wrapper(*args, **kwargs): #args - tupper, kwergs - slowa kluczowa, wrapper - opakowanie
        start = time.time()
        result = func(*args, **kwargs)
        print(f"czas wykoniania {func.__name__}:",time.time() - start)
        return result
    
    return wrapper

def dane():
    return [i for i in range(100000)]
dane = zmierz_czas(dane)

@zmierz_czas #dekorator - funkcja zmieniajace dzialanie wczesniej zdefiniowanej funkcji
def do_kwadratu(lista):
    return [x**2 for x in lista]
#do_kwadratu = zmierz_czas(do_kwadratu)

d = dane()

do_kwadratu(d)


"""
def dane():
    return [i for i in range(100000)]
start = time.time()
dane()
print(time.time() - start)
"""