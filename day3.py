import numpy

with open("inputday3.txt") as f:
    content = f.readlines()

fix_size = 1000


class Claim:
    def __init__(self, claim_string):
        infos = claim_string.split(' ')
        id = infos[0].split('#')[1]
        start = infos[2].split(',')
        left_start = start[0]
        top_start = start[1].split(':')[0]
        size = infos[3].split('x')
        width = size[0]
        height = size[1]
        self.id = id
        self.left = int(left_start)
        self.top = int(top_start)
        self.right = int(width) + self.left
        self.bottom = int(height) + self.top
        self.size = int(width) * int(height)


claims = [Claim(x.strip()) for x in content]

matrix = numpy.zeros(shape=(fix_size, fix_size))

for c in claims:
    for x in range(c.left, c.right):
        for y in range(c.top, c.bottom):
            matrix[x][y] = matrix[x][y] + 1


nb = 0

for x in range(0, fix_size):
    for y in range(0, fix_size):
        if matrix[x][y] > 1:
            nb = nb + 1

print(nb)

for c in claims:
    count = 0
    for x in range(c.left, c.right):
        for y in range(c.top, c.bottom):
            if matrix[x][y] == 1.0:
                count = count + 1

    if count == c.size:
        print(c.id)


