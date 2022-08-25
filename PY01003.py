t = int(input())

while t:
    t -= 1
    n = int(input())
    m = n % 10
    if m < 5:   print(n - m)
    else: print(n + 10 - m)
