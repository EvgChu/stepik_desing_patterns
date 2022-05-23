import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)

# код ниже руками не трогать:
coords = [11,12, 21,22]
line1 = Line(Point(coords[0], coords[1]),
             Point(coords[2], coords[3]))
line2 = line1.deep_copy()
line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

print(f'{line2.start.x} {line2.start.y} {line2.end.x} {line2.end.y}')