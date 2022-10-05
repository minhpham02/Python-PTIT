n = int(input())
a = [[int(j) for j in input().split()] for i in range (n)]
k = int(input())
upper, lower = 0, 0
for i in range (n):
    for j in range (n):
        if i < j:
            lower += a[i][j]
        elif i > j:
            upper += a[i][j]
print('YES' if abs(upper - lower) <= k else 'NO')
print(upper, lower, end = " ")