import math

def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

t = int(input())

while t:
    t -= 1
    s = input()
    res = 0
    for i in range(len(s)-4,len(s)):
        res = res*10 + int(s[i])
    print("YES" if isPrime(res) else "NO")