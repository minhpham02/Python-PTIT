import math
Prime = '2357'
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def solve(str):
    for i in range(0,len(str)):
        if not isPrime(i) and str[i] in Prime or isPrime(i) and str[i] not in Prime:
            return 'NO'
    return 'YES'

for case in range(int(input())):
    print(solve(input()))