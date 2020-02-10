x = [1,3,5,77,8,3]

i = 0 
while i < len(x):
    print(x[i])
    i += 1

print("-"*40)

for el in x:
    print(el)

for el in enumerate(x):
    print(el)

for i, el in enumerate(x):
    print(el)
