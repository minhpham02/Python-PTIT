import math

def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def solve(str):
    num = int(str[-1:-5:-1][::-1])
    return 'YES' if isPrime(num) else 'NO'

for case in range(int(input())):
    print(solve(input()))