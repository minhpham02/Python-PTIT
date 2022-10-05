import math

def isPrime(n):
    if n < 2 :
        return False
    for i in range(2,int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

for case in range(int(input())):
    s = input()
    s1, s2 = int(s[:3]), int(s[-1:-4:-1][::-1])
    print('YES' if isPrime(s1) and isPrime(s2) else 'NO')