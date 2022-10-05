import math

def isPrime(n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def solve(str):
    s = sum(int(i) for i in str)
    if not isPrime(s):
        return 'NO'
    for i in range(0,len(str)):
        if i % 2 == 0 and int(str[i]) % 2 != 0 or i % 2 != 0 and int(str[i]) % 2 == 0:
            return 'NO'
        return 'YES'  

for case in range(int(input())):
    print(solve(input()))