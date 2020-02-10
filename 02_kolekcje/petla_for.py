"""
mamy zadana liste np. x = [1,2,3,4,6,7,-51,8,13,17,18,34,-6] 
chcemy zliczyc ile bylo dodatnich a ile ujemnych
wypisz osobne sumy liczb dodatnich i ujemnych
"""

x = [1,2,3,4,6,7,-51,8,13,17,18,34,-6] 
ujemne, suma_ujemne, dodatnie, suma_dodatnie = 0,0,0,0 
x1 = sorted(x)
print(x1)

for el in x:
    if el < 0:
        ujemne += 1
        suma_ujemne +=el
    else:
        dodatnie += 1
        suma_dodatnie +=el
print(f"""
ujemnych {ujemne}
dodatnich {dodatnie}
suma ujemnych {suma_ujemne}
suma dodatnich {suma_dodatnie}
""")

