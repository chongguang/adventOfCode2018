input = "##.##.##..#..#.#.#.#...#...#####.###...#####.##..#####.#..#.##..#..#.#...#...##.##...#.##......####."
#input = "#..#.#..##......###...###"

with open("inputday12.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

transformations = {}
for c in content:
    sp = c.split(' => ')
    transformations[sp[0]] = sp[1]

print(transformations)


def transform(input_string, start_index):
    output_string = ""
    start_index -= 5
    input_string = "....." + input_string + "....."
    for i in range(2, len(input_string) - 2):
        key = input_string[i-2: i+3]
        if key in transformations:
            output_string += transformations[key]
        else:
            output_string += '.'
    output_string = input_string[:2] + output_string + input_string[-2:]
    while output_string[0] == '.':
        output_string = output_string[1:]
        start_index += 1
    while output_string[len(output_string)-1] == '.':
        output_string = output_string[:-1]
    return output_string, start_index


def calculate_sum(start_index, input):
    sum = 0
    for i in range(0, len(input)):
        if input[i] == '#':
            sum += i + start_index
    return sum


start_index = 0
iteration = 1100
sum_list = []
for i in range(0, iteration):
    res = transform(input, start_index)
    input = res[0]
    start_index = res[1]
    sum = calculate_sum(start_index, input)
    sum_list.append(sum)

print(sum_list)


for i in range(0, iteration-1):
    sum_list[i] = sum_list[i+1] - sum_list[i]

sum = 0
iter = 50000000000
for i in range(0, len(input)):
    if input[i] == '#':
        sum += iter - 100 + i
print(sum)








