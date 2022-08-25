def gcd(a,b):
    c = int(a)
    d = int(b)
    while d != 0:
        n = c % d
        c = d
        d = n
    return c

t = int(input())

while t:
    t -= 1
    s = input()
    tmp = ""
    for i in range(len(s)-1,-1,-1):
        tmp += s[i]
    if gcd(s,tmp) == 1:  print("YES")
    else: print("NO")