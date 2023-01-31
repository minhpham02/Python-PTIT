class Student:
    def __init__(selt,name, birth, score):
        selt.name = name
        selt.birth = birth
        selt.score = sum(score)

    def __str__(selt):
        return f'{selt.name} {selt.birth} {selt.score}'

if __name__ == '__main__':
    print(Student(input(),input(),[float(input()), float(input()), float(input())]))
