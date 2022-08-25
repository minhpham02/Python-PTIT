t = int(input())

while t:
    t -= 1
    s = input()
    Sum = 0
    for i in range(0,len(s)):
        Sum += int(s[i])
    if Sum % 3 == 0: print("YES")
    else: print("NO")