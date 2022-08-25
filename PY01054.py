t = int(input())

while t:
    t -= 1
    s = input()
    res = 1
    for i in range(0,len(s)):
        if int(s[i]) != 0: res = res * int(s[i])
    print(res)