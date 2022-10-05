import math

Prime = '2357'
unPrime = '014689'

def isPrime(n):
    if n < 2: 
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solve(str):
    if not isPrime(len(str)):
        return 'NO'
    return 'YES' if sum(str.count(i) for i in Prime) > sum(str.count(i) for i in unPrime) else 'NO'

for cases in range(int(input())):
    print(solve(input()))