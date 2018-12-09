with open("inputday8.txt") as f:
    content = f.readlines()

nbs = content[0].split(' ')
nbs = [int(x) for x in nbs]
print(nbs)


children_stack = [9]
metadata_stack = [11]

pointer = 2
metadata_sum = 0


while pointer < len(nbs) and len(children_stack) > 0:
    if nbs[pointer] == 0:
        nb = nbs[pointer + 1]
        for i in range(pointer + 2, pointer + 2 + nb):
            metadata_sum = metadata_sum + nbs[i]
        pointer = pointer + 2 + nb
        children_stack[0] = children_stack[0] - 1
        while len(children_stack) > 0 and children_stack[0] == 0:
            children_stack.pop(0)
            nb_metadata = metadata_stack.pop(0)
            for i in range(pointer, pointer + nb_metadata):
                metadata_sum = metadata_sum + nbs[i]
            pointer = pointer + nb_metadata
            if len(children_stack) > 0:
                children_stack[0] = children_stack[0] - 1
    else:
        children_stack = [nbs[pointer]] + children_stack
        metadata_stack = [nbs[pointer+1]] + metadata_stack
        pointer = pointer + 2


print(metadata_sum)





