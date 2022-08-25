import math

def gcd(a,b):
    while b != 0:
        k = a % b
        a = b
        b = k
    return a

t = int(input())

while t:
    n = int(input())
    k = 0
    for i in range(1,n+1):
        if gcd(i,n) == 1:
            k += 1
    if k < 2: 
        print("NO")
    else:    
        OK = True
        for i in range(2,int(math.sqrt(k))+1):
            if k % i == 0:  
                OK = False
                break
        print("YES" if OK else "NO")
    t -= 1