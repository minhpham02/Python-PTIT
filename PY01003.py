for case in range(int(input())):
    str = ' '.join(input()).split()
    for i in range(len(str) - 1, 0, -1):
        if str[i] >= '5':
            str[i-1] = chr(ord(str[i-1]) + 1)
        str[i] = '0'
    if str[0] > '9':
        str[0] = '10'
    print(''.join(str))

