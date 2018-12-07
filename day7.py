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

"""
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


order.append(end_elements[0])



print(''.join(order))
print(order)
"""


def char2time(c):
    return ord(c) - 4


timer = 0
nb_workers = 5
workers = [0] * nb_workers
position = ['#'] * nb_workers

print(workers)
print(prerequisites)
print(queue)


while len(queue) > 0 or sum(workers) > 0:
    # if there are available workers, queue sort and queue => workers
    queue.sort()
    while 0 in workers and len(queue) > 0:
        e = queue.pop(0)
        ind = workers.index(0)
        workers[ind] = char2time(e)
        position[ind] = e

    # time ++
    for i in range(0, nb_workers):
        if workers[i] > 0:
            if workers[i] == 1:
                retire = position[i]
                for key in prerequisites:
                    if retire in prerequisites[key]:
                        prerequisites[key].remove(retire)
            workers[i] = workers[i] - 1
    timer = timer + 1

    # prerequisites => queue if there are available workers
    temp = []
    for k, v in prerequisites.items():
        if len(v) == 0:
            temp.append(k)
    for t in temp:
        prerequisites.pop(t)
        queue.append(t)


print(timer)
