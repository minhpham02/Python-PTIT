
t = int(input())
while t > 0:
    n = str(input())
    s = 0
    for i in n:
        if i == '4' or i == '7':
            s += 1

    if s == len(n):    print("YES")
    else:   print("NO") 
    t -= 1