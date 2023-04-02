n = input()
s1 = 0
s2 = 0
for i in n:
    if i == '3':
        s1 += 1
    if i == '5':
        s2 += 1
s = s1 + s2
if s == 3 or s == 5:
    print('YES')
else:
    print('NO')    
