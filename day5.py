with open("inputday5.txt") as f:
    content = f.readlines()

suit = list(content[0])
#suit = ['d', 'a', 'b', 'A', 'c', 'C', 'a', 'C', 'B', 'A', 'c', 'C', 'c', 'a', 'D', 'A']
suit = [x for x in suit if x != 'p' and x != 'P']
suit = [ord(x) for x in suit]

print(suit)


left = 0

while left < len(suit)-1:
    if left < 0:
        left = 0
    right = left + 1
    if abs(suit[left] - suit[right]) == 32:
        del suit[left:left+2]
        left = left - 1
    else:
        left = left + 1


print(len(suit))


