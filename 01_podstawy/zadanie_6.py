x, y = 10, 40

if x<=10 and y<=10:
    print("Jestes w lewym dolnym rogu")
elif x<=10 and y >10 and y < 90:
    print("Jestes w dolnej krawedzi")
elif x<=10 and y >= 90:
    print("Jestes w prawym dolnym rogu")
elif x > 10 and x < 90 and y<= 10:
    print("Jestes w lewej krawedzi")
elif x>= 90 and y<= 10:
    print("Jestes w lewym gornym rogu")
elif x>= 90 and y >10 and y <= 90:
    print("Jestes w gornej krawedzi")
elif x>= 90 and y >= 90:
    print("Jestes w prawym gornym rogu")
elif x >10 and x < 90 and y >= 90:
    print("Jestes w prawej krawedzi")
else: print("Jestes poza tarcza")
