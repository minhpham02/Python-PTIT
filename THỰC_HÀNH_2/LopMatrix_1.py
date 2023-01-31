from tkinter import N


class Matrix:
    def __init__(self, n, m, a):
        self.n = n
        self.m = m
        self.a = a

    def mult(self):
        tmp = []
        for i in range(self.n):
            tmp += [[0]*self.n]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    tmp[i][j] += self.a[i][k]*self.a[j][k]
        return Matrix(self.n, self.n, tmp)
    def __str__(self):
        for i in self.a:
            print(*i)
        return ''

if __name__ == '__main__': 
    for t in range(int(input())):
        n, m = [int(i) for i in input().split()]
        ip = []
        
        MaTran = Matrix(n, m, ip)
        print(MaTran.mult())
