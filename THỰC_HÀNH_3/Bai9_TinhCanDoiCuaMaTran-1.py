n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]
k = int(input())
s1, s2 = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            s1 += a[i][j]
        elif i > j:
            s2 += a[i][j]
print('YES' if abs(s1 - s2) <= k else 'NO')
print(abs(s1 - s2))
