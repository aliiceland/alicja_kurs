a = (1, 2, 'a', 'c', 1)
b = tuple()

print(type(a))
print(dir(a))

print(a.count(1))
print(a.count('a'))
print(a.count('d'))

print(a.index(1))
print(a.index('c'))
if 'h' in a:
    print(a.index('h'))

print(a[1]) 


a = (1, 2)
b = (3, 4)
print(a + b)

