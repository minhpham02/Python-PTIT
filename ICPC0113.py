
import math

def isPrime(n):
    if n < 2:
         return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for case in range(int(input())):
    n = int(input())
    true = []
    for i in range(13,n):
        s = str(i)
        if int(s[::-1]) < n and s != s[::-1] and isPrime(int(s)) and isPrime(int(s[::-1])) and s not in true:
            print(s, s[::-1], end = ' ')
            true += [s, s[::-1]]
    print()
