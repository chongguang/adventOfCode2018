with open("inputday7.txt") as f:
    content = f.readlines()

points = [x.split(' ') for x in content]
points = [(x[1], x[7]) for x in points]

starts = set()
ends = set()

for p in points:
    starts.add(p[0])
    ends.add(p[1])


queue = list(starts.difference(ends))
queue.sort()
print(queue)

end_elements = list(ends.difference(starts))
print(end_elements)


prerequisites = dict()
for p in points:
    if p[1] not in prerequisites:
        prerequisites[p[1]] = [p[0]]
    else:
        prerequisites[p[1]].append(p[0])


order = []
while len(queue) > 0:
    elem = queue.pop(0)
    order.append(elem)
    if elem not in end_elements:
        for key in prerequisites:
            if elem in prerequisites[key]:
                prerequisites[key].remove(elem)
                if len(prerequisites[key]) == 0:
                    if key not in end_elements:
                        queue.append(key)
        queue.sort()


print(''.join(order) + end_elements[0])