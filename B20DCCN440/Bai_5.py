from math import sqrt
from math import pow

for t in range(int(input())):
    a = []
    b = []
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    d = 0
    s = 0
    for i in range(len(a)):
        d += pow((a[i] - b[i]),2)
        s += (a[i]*b[i])
    h = round(sqrt(d),2)
    print('{:.2f}'.format(h), s, end = " ")
    print()
