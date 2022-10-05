def check(s1,s2):
    for i in range(1,len(s1)):
        tmp1  = abs(ord(s1[i]) - ord(s1[i-1]))
        tmp2  = abs(ord(s2[i]) - ord(s2[i-1]))
        if tmp1 != tmp2:
            return 'NO'
    return 'YES'


for case in range(int(input())):
    str = input()
    print(check(str, str[::-1]))