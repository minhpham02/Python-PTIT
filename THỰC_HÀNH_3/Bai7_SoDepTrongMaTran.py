n, m = [int(i) for i in input().split()]
Max, Min, kt, ok = 0, 10**6, 0, 0 
a = [[0]]*n 
for i in range(n):
    a[i] = [int(j) for j in input().split()]
    Max = max(max(a[i]),Max)
    Min = min(min(a[i]),Min)
for i in range(n):
    for j in range(m):
        if a[i][j] == Max - Min:
            if kt == 0:
                ok = 1
                print(a[i][j])
                kt = 1
            print('Vi tri [',i,'][',j,']', sep='')
if ok == 0: print('NOT FOUND')
