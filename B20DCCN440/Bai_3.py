for t in range(int(input())):
    n = input()
    s = 1
    for i in range(0,len(n)):
        if i % 2 == 0 and n[i] != '0':
            s *= int(n[i])
    print(s)