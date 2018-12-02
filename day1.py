with open("inputday1.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
content = [int(x) for x in content]

totalChanges = len(content)


def sum(frequency=0, pos=0, fSet=set()):
    while frequency not in fSet:
        fSet.add(frequency)
        if pos == totalChanges:
            pos = 0
        print(content[pos])
        frequency = frequency + content[pos]
        pos = pos + 1
    return frequency


res = sum(frequency=0, pos=0, fSet=set())

print(res)