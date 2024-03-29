import math

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        print ("1 " if isPrime(a[i][j]) else "0 ", end='')
    print()

