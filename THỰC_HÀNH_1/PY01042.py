def solve(str):
    for i in range(len(str)):
        if str[i] != '0' and str[i] != '1' and str[i] != '2':
            return "NO"
    return "YES"

for t in range(int(input())):
    print(solve(input()))