a, K, N = map(int,input().split())

n = int(N / K) + 1

tmp = -1
for i in range(1,n):
    b = i * K - a
    if b > 0:
        print(b, end = ' ')
        tmp = 1
if tmp == -1: print("-1")
