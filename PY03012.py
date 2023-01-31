class student:
    def __init__(self, name, *a):
        self.name = name
        self.total = int(a[0])
        self.submit = int(a[1])

    def get_name(self):
        return self.name

    def get_total(self):
        return self.total

    def get_submit(self):
        return self.submit

    def __str__(self):
        return f'{self.name} {self.total} {self.submit}\n'    

students = []

for t in range(int(input())):
    students += [student(input(), *input().split())]
students.sort(key = lambda x: (x.get_total(), x.get_submit(), x.get_name()))
print(*students)


