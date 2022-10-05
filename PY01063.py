for case in range(int(input())):
    s, num = input(), input()
    cnt = 0 
    index = s.find(num)
    while index != -1:
        cnt += 1
        index = s.find(num,index + len(num))
    print(cnt)
