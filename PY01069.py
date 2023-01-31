def solve(str):
    s, m = 0, 1
    OK = False
    for i in range(0,len(str)):
        if i % 2 != 0:
            s += int(str[i])
        else:
            if int(str[i]):
                OK = True
                m *= int(str[i])
    if OK == False:
        m = 0
    print(m, s, end=" ")
    print()

for t in range(int(input())):
    solve(input())