"""
Napisz funkcje silnia ktora rekurencyjnie policzy silnie dla zadanej liczby

5! = 5 * 4! = 5*4*3! = 5*4*3*2*1*0! = 5*4*3*2*1*1
"""

n = 5

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)
print(silnia(6))