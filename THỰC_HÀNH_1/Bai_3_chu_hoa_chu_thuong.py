s = str(input())
a = 0 
b = 0
for i in s:
    if i.islower(): a += 1
    else: b += 1
if a >= b :  print(s.lower())
else : print(s.upper())