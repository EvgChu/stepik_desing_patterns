class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def draw_point(p):
    print(".", end='')

#---------------

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


if __name__ == "__name__":
    rs = [
        Rectangle(1,1,10,10),
        Rectangle(3,3,10,10),
    ]