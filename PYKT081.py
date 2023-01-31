def check(n):
    for i in n:
        if not i.isdigit() or int(i) > 255 or int(i) < 0:
            return False
    return len(n) == 4

for t in range(int(input())):
    print("YES" if check(input().split(".")) else "NO")