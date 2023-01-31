
from math import sqrt


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:  return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
for i in list(dict.fromkeys(a)):
    if isPrime(i):
        print(i, a.count(i))
 