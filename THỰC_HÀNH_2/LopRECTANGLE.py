class Rectangle:
    def __init__(self, length, width, colors):
        self.length = length
        self.width = width
        self.colors = colors
    
    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width
    
    def color(self):
        return self.colors.title()

try:
    if __name__ == '__main__':
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))

except:
    if int(arr[0]) <= 0 or int(arr[1]) <= 0:
        print("INVALID")
    else:    
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))