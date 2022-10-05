
isPrime = [1] * int(1e6+7)
isPrime[0] = isPrime[1] = 0
for i in range(1000):
    if isPrime[i]:
        for j in range(i*i, int(1e6+7), i):
            isPrime[j] = 0

for case in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n - 5):
        if isPrime[i] and isPrime[i+6]:
            if isPrime[i+2] or isPrime[i+4]:
                cnt += 1
    print(cnt)