with open("inputday2.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
ids = [x.strip() for x in content]

print(ids)


def count_times(id):
    occurrence = {}
    for char in id:
        if char in occurrence:
            occurrence[char] = occurrence[char] + 1
        else:
            occurrence[char] = 1
    res = []
    if 2 in occurrence.values():
        res.append(2)
    if 3 in occurrence.values():
        res.append(3)
    return res


times = map(count_times, ids)


def checksum(times):
    n2 = 0
    n3 = 0
    for t in times:
        if 2 in t:
            n2 = n2 + 1
        if 3 in t:
            n3 = n3 + 1
    return n2 * n3


print(checksum(times))


def nb_diff(s1, s2):
    length = len(s1)
    nb = 0
    for i in range(0, length-1):
        if s1[i] != s2[i]:
            nb = nb + 1
    return nb


nb_ids = len(ids)
x = 0
y = 1

while nb_diff(ids[x], ids[y]) > 1 and x <= nb_ids - 2 and y <= nb_ids - 1 :
    if y == nb_ids - 1:
        x = x + 1
        y = x + 1
    else:
        y = y +1

print(ids[x])
print(ids[y])


