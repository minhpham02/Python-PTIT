def solve(n):
    if len(s) < 3:
        return 'NO'
    i = 1
    while i < len(s) and n[i] > n[i-1]:
        i += 1
    while i < len(s) and n[i] < n[i-1]:
        i += 1
    return 'YES' if  len(n) == i else 'NO'

for t in range(int(input())):
    s = input()
    print(solve(s))