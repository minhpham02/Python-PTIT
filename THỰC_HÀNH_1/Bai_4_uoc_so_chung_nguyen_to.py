import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solve(a,b):
    tmp = math.gcd(a,b)
    s = str(tmp)
    cnt = sum(int(i) for i in s)
    return 'YES' if isPrime(cnt) else 'NO'

for t in range(int(input())):
    a, b = map(int,input().split())
    print(solve(a,b))