n = int(input())
a, i, kt = [], 1, 0
while len(a) < n :
    x = [int(x) for x in input().split()]
    a += x
while i < a[n-1]:
    if a.count(i) != 1:
        print(i)
        kt = 1
    i += 1
if kt == 0:
    print('Excellent!')
    