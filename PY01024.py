import math

t = int(input())

while t:
    t -= 1
    s = input()
    n = len(s)
    res = int(s[n-1])
    OK = True
    for i in range(n-1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            OK = False
            break
        res += int(s[i])
    if res % 10 != 0:   OK = False
    print("YES" if OK else "NO")
    