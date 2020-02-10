moja_lista = list()
print(dir(moja_lista))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

moja_lista.append(10)
print(moja_lista)

x = [1,2,4,6,3,7,9,5]
x1 = sorted(x)
print(x1)

x=[1,2,3]
y=x 
x.append(5)
print(x, y)
print(id(x),id(y))

y = x[:]
y=x.copy() 
x.append(5)
print(x, y)
print(id(x),id(y))

z = [1,2]
x = [1,2, z]
print(x) # [1, 2, [1, 2]]
import copy
y=copy.deepcopy(x)
print(y)
z.append(4)
print(x, y)

x = (4,12,1,100)
print(min(x))
print(max(x))
print(sum(x))

