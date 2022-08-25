s = input()

res = 0

tmp = ""

for i in range(len(s)-1,-1,-1):
    res += 1
    tmp = s[i] + tmp
    if res % 3 == 0 and i > 0:
        tmp = "," + tmp
        res = 0
print(tmp)    

    