s = input()
tmp = 0
while len(s) > 1: 
    s = str(sum((ord(i)-ord('0')) for i in s))
    tmp += 1
print(tmp)