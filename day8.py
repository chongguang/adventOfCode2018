with open("inputday8.txt") as f:
    content = f.readlines()

nbs = content[0].split(' ')
nbs = [int(x) for x in nbs]
print(nbs)

"""

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
"""

class Node:
    def __init__(self, start):
        self.p = start
        self.nb_children = nbs[start]
        self.nb_metadata = nbs[start + 1]
        self.values = []
        self.current_child = None

    def calculate_value(self):
        if self.nb_children == 0:
            v = 0
            for i in range(self.p + 2, self.p + 2 + self.nb_metadata):
                v =  v + nbs[i]
            end = self.p + 2 + self.nb_metadata
            return v, end
        else:
            self.p = self.p + 2
            while self.nb_children > 0:
                # create current child
                self.current_child = Node(self.p)
                # add current child's value to self.values[]
                value_and_p = self.current_child.calculate_value()
                self.values.append(value_and_p[0])
                # move self.p forward
                self.p = value_and_p[1]
                # self.nb_children --
                self.nb_children = self.nb_children - 1

            total_value = 0
            for i in range(self.p, self.p + self.nb_metadata):
                if nbs[i] <= len(self.values):
                    total_value = total_value + self.values[nbs[i] - 1]
            return total_value, self.p + self.nb_metadata


n = Node(0)

print(n.calculate_value())





