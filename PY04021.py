
class Time:
    def __init__(self, id, name, timeBegin, timeEnd):
        self.id = id
        self.name = name
        self.timeBegin = timeBegin
        self.timeEnd = timeEnd
        self.Caculation_time()
    
    def Caculation_time(self):
        begin = self.timeBegin.split(':')
        end =  self.timeEnd.split(':')
        self.hours = int(end[0]) - int(begin[0])
        self.minutes = int(end[1]) - int(begin[1])
        if self.minutes < 0:
            self.hours -= 1
            self.minutes += 60
        self.total_time = f'{self.hours} gio {self.minutes} phut'

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + self.total_time

print(*sorted([Time(input(),input(),input(),input()) for i in range(int(input()))], key = lambda x: (-x.hours, -x.minutes)), sep = '\n')

