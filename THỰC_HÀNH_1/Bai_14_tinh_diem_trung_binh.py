n = int(input())
a = [float(i) for i in input().split()]
x, y = min(a), max(a)
s,cnt = 0, 0
for i in a:
    if i != x and i != y:
        s += i
        cnt += 1
print('{:.2f}'.format(s/cnt))
