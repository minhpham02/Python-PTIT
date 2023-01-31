s = '0123456789ABCDEF'
with open('DATA.in', 'r') as f:
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        num = int(f.readline(),2)
        res = ''
        while num:
            res += s[num%n]
            num //= n
        print(res[::-1])