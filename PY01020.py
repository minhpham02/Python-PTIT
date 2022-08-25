t = int(input())
while(t > 0):
    a = str(input())
    b = len(a)
    if a[b-1] == '6' and a[b-2] == '8':   print("YES\n")
    else: print("NO\n")
    t -= 1