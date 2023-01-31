class student:
    def __init__(self, name, *congacon):
        self.__name = name
        self.__total = int(congacon[0])
        self.__submit = int(congacon[1])
    
    def get_name(self):
        return self.__name
    
    def get_total(self):
        return self.__total
    
    def get_submit(self):
        return self.__submit
    
    def __str__(self):
        return f'{self.__name} {self.__total} {self.__submit}\n'    

students = []    
for i in range(int(input())):
    students += [student(input(), *input().split())]
    
students.sort(key=lambda ele: (-ele.get_total(), ele.get_submit(), ele.get_name()))

print(*students)