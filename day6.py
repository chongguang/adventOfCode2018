import numpy

with open("inputday6.txt") as f:
    content = f.readlines()

points = [x.strip() for x in content]


def parse(s, i):
    t = s.split(', ')
    return int(t[1]), int(t[0]), i


points = [parse(points[i], i) for i in range(0, len(points))]

size = 400


edge_map = numpy.zeros(shape=(size, size))


def mark(x, y):
    dist_list = []
    for p in points:
        dist_list.append(abs(p[0] - x) + abs(p[1] - y))

    v = dist_list.index(min(dist_list))
    dist_list.sort()
    if dist_list[0] == dist_list[1]:
        v = -1
    return v


for i in range(0, size):
    for j in range(0, size):
        edge_map[i][j] = mark(i, j)


count_map = {}
for i in range(0, size):
    for j in range(0, size):
        if edge_map[i][j] not in count_map:
            count_map[edge_map[i][j]] = 1
        else:
            count_map[edge_map[i][j]] = 1 + count_map[edge_map[i][j]]

"""
for r in edge_map:
    print(r)
"""

boarder_set = set(edge_map[0]) | set(edge_map[size-1])
print(boarder_set)
for i in range(0, len(edge_map)):
    boarder_set.add(edge_map[i][0])
    boarder_set.add(edge_map[i][size-1])

print(boarder_set)

for i in boarder_set:
    count_map.pop(i)

print(count_map)


count_map_2 = numpy.zeros(shape=(size, size))


def total_dist(x, y):
    d = 0
    for p in points:
        d = d + abs(p[0] - x) + abs(p[1] - y)
    return d


print(total_dist(0, 0))


surface = 0
for i in range(0, size):
    for j in range(0, size):
        if total_dist(i, j) < 10000:
            surface = surface + 1

print(surface)
