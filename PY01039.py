def check(s):
    for i  in range(2,len(s)):
        if  s[i] != s[i-2]:  
            return "NO"
    return "YES"

for case in range(int(input())):
    print(check(input()))