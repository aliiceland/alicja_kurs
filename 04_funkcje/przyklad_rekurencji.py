lista = [1, 20, 30, 40]

def reku_print(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[0])
        reku_print(lista[1:])
reku_print(lista)
