class Student:
    def __init__(self, id, name, clas):
        self.id = id
        self.name = name
        self.clas = clas
    
    def getScore(self, s):
        res = 10 - s.count('v') * 2 - s.count('m')
        self.status = '0 KDDK' if res == 0 else res
    
    def __str__(self):
        return f'{self.id} {self.name} {self.clas} {self.status}'


student = []
t = int(input())
for __ in range(t):
    student += [Student(input(), input(), input())]
for __ in range(t):
    id, s = [i for i in input().split()]
    for i in student:
        if i.id == id:
            i.getScore(s)
            break
print(*student, sep='\n')