alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    ans = ''
    while a > 0:
        ans += alpha[a%b]
        a //= b
    print(ans[::-1]) 