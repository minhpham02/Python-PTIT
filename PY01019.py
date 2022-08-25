import math

for _ in range(int(input())):
    s1 = input()
    s2 = ""
    for i in range(len(s1)-1,-1,-1):
        s2 += s1[i]
    OK =True
    for i in range(0,len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            OK = False
            break
    print("YES" if OK else "NO")