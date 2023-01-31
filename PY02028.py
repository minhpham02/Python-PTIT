n, a = int(input()), []
cnt = 0
for i in range(n):
    a += [[j for j in input()]]
for i in range(n):
    for j in range(n):
        for k in range(j+1, n):
            if a[i][k] == a[i][j] == 'C': cnt += 1
            if a[j][i] == a[k][i] == 'C': cnt += 1
print(cnt)