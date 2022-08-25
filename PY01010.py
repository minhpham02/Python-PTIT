t = int(input())
while t > 0:
    n = str(input())
    a = len(n)
    if n[0] == n[a-2] and n[1] == n[a-1]:   print("YES")
    else: print("NO")
    t -= 1