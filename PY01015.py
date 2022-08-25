t = int(input())

while t:
    s = str(input())
    OK = True
    for i in range(len(s) - 1):
        if s[i] > s[i+1]:
            OK = False
            break
    print("YES" if OK else "NO")
    t -= 1