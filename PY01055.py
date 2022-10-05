def solve(str):
    if len(str) % 2 == 0 or str[0] != str[1]:
        return 'NO'
    for i in range(2, len(str),2):
        if str[i] != str[i-2]:
            return 'NO'
    return 'YES'

for i in range(int(input())):
    print(solve(input()))