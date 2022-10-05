n = int(input())
a = [[int(j) for j in input().split()] for i in range (n)]
k = int(input())
upper, lower = 0, 0
for i in range (n):
    for j in range (n):
        if j < n - i - 1:
            upper += a[i][j]
        elif j> n - i - 1:
            lower += a[i][j]
print('YES' if abs(upper - lower) <= k else 'NO')
print(abs(upper - lower))

