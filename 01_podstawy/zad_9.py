"""
z podanych w petli liczb wybierz najmniejsza i najwieksza, k konczy petle

x= none
"""

i = 0
m = None
mx = None 


while True:
    x = input("Podaj ciag liczb, aby zakonczyc wpisywanie wpisz 'k' ")
    if x == 'k':
        break
    x=int(x)
    if m is None or x < m:
        m=x 
    if mx is None or x > mx: 
        mx = x
print(f"najmniejsza liczba: {m:.2f},najwieksza liczba: {mx:.2f}  ")