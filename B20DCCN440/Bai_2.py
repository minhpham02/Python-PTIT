for t in range(int(input())):
    n = input()
    m = len(n) - 1
    while int(n[m]) >= int(n[m-1]) and m > 0:
        m -= 1
    while int(n[m]) <= int(n[m-1]) and m > 0:
        m -= 1
    if m == 0 and len(n) == 8:
        print('YES')
    else:
        print('NO') 