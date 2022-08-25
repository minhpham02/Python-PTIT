import math

def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0: return False
    return True

t = int(input())

while t:
    t -= 1
    s = input()
    Sum = 0
    for i in range(0,len(s)):
        Sum += int(s[i])
    if isPrime(Sum):    print("YES")
    else: print("NO")