from math import gcd

class PhanSo:
    def __init__(self, a):
        self.tu = int(a[0])
        self.mau = int(a[1])

    def RutGon(self):
        GCD = gcd(self.tu,self.mau)
        self.tu //= GCD
        self.mau //= GCD

    def __str__(self):
        self.RutGon()
        return f'{self.tu}/{self.mau}'

if __name__ == '__main__':
	PS = PhanSo(input().split())
print(PS)