t = int(input())

while t:
    t -= 1
    s = input()
    i = 0
    while True:
        res = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            res += 1
            i += 1
        print("{}{}".format(res,s[i]),end = '')
        i += 1
        if i == len(s): 
            break
    print()