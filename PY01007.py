import math

t = int(input())

while t > 0:

    N, X, M = list(map(float, input().split()))
    X = X/100
    K = math.log(M/N,1+X)
    if K == int(K) :
        print(int(K))
    else :
        print(int(K)+1)
    t -= 1
