with open("inputday10.txt") as f:
    content = f.readlines()


class Point:
    def __init__(self, input_string):
        split = input_string.split('<')
        position = split[1]
        xy = position.split('>')[0].split(', ')
        self.px = int(xy[0])
        self.py = int(xy[1])
        velocity = split[2].split('>')[0].split(', ')
        self.vx = int(velocity[0])
        self.vy = int(velocity[1])

    def move(self):
        self.px = self.px + self.vx
        self.py = self.py + self.vy


points = [Point(x) for x in content]

for i in range(1, 10831):
    for p in points:
        p.move()

    x_set = set()
    y_set = set()
    for p in points:
        x_set.add(p.px)
        y_set.add(p.py)

    x_min = min(x_set)
    x_max = max(x_set)
    y_min = min(y_set)
    y_max = max(y_set)
    x_diff = x_max - x_min
    y_diff = y_max - y_min

    if len(y_set) <= 10:
        print(i)
        matrix = [['.' for x in range(0, y_diff+1)] for y in range(0, x_diff+1)]
        for p in points:
            matrix[p.px-x_min][p.py-y_min] = '#'

        for row in matrix:
            print(row)
