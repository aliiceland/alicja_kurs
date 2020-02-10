"""
napisz program ktory wypisze tabliczke mnozenia NxN
np n=3

    0 1 2 3 
0   0 0 0 0 
1   0 1 2 3 
2   0 2 6 6
3   0 3 6 9 

"""

print("A", end=" ")
print("B")
print()
print("C")



y = list(range(0,4))
print("     ", end = "")
print (y)
print ()
list (y)
for el in y:
     for x in y:
         print (f"{x*el:3}", end="")
     print()   

print() 
print() 

N=10
print("     ", end = "")
for i in range(N+1):
    print (f"{i:4}", end="")
print ()
print ()
for i in range(N+1):
    print(f"{i:<5}", end="")
    for j in range(N+1):
        print (f"{i*j:4}",end="")
    print()


