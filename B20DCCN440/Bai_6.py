
t = int(input())
while t > 0:
        a = input().split()
        b = input().split()
        tmp1 = 0
        tmp2 = 0
        for i in range(len(a)):    
            tmp1 += (int(a[i] - int(b[i]))  * int(a[i] - int(b[i])))
            tmp2 += int(a[i] - intb[i])
        tmp1 = sqrt(tmp1)
        tmp1 = round(tmp1,2)
        print('{:.2f}'.format(tmp1,tmp2))
        t -= 1

