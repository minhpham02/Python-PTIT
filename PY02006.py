def solve():
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    b = sorted([int(i) for i in input().split()])
    print('YES' if solve() else 'NO')
