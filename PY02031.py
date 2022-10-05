import math

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

n,m = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
for i in range(n):
    for j in range(m):
        if isPrime(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
print(a)

