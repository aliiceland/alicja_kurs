"""
korzystajac z petli while wypisz dla 100 pierwszych liczb parzystych 
te liczb, jej kwadrat i szescian
"""
i = 0 
   
while i <= 100:
    if i % 2 == 0 or i == 33:
        print(f"{i:7},{i ** 2:7}, {i ** 3:7}")
    i += 1 

