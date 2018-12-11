import numpy

size = 300
serial_number = 9810


def power_level(x, y, s_number):
    rack_id = x + 10
    tmp = (rack_id * y + s_number) * rack_id
    digit = 0
    if tmp > 99:
        digit = int(tmp / 100) % 10
    return digit - 5


matrix = numpy.zeros(shape=(size + 1, size + 1))

for i in range(1, size+1):
    for j in range(1, size+1):
        matrix[i][j] = power_level(i, j, serial_number)


def sum3x3(x, y, s):
    sum = 0
    for i in range(x, x+s):
        for j in range(y, y+s):
            sum += matrix[i][j]
    return sum


sum_matrix = numpy.zeros(shape=(size - 1, size - 1))

max_sum = 0
max_x = 0
max_y = 0

for i in range(1, size-3):
    for j in range(1, size-3):
        sum = sum3x3(i, j, 3)
        sum_matrix[i][j] = sum
        if sum > max_sum:
            max_sum = sum
            max_x = i
            max_y = j

print(max_sum)
print(max_x)
print(max_y)


# q2
cumul_matrix = numpy.zeros(shape=(size + 1, size + 1))
cumul_matrix[1][1] = matrix[1][1]

for i in range(2, size + 1):
    cumul_matrix[i][1] = matrix[i][1] + cumul_matrix[i-1][1]
    cumul_matrix[1][i] = matrix[1][i] + cumul_matrix[1][i-1]


for i in range(2, size + 1):
    for j in range(2, size + 1):
        cumul_matrix[i][j] = matrix[i][j] + cumul_matrix[i-1][j] + cumul_matrix[i][j-1] - cumul_matrix[i-1][j-1]


max_x_2 = 0
max_y_2 = 0
max_sum_2 = 0
max_size_2 = 0

for s in range(1, size+1):
    for x in range(1, size+1-s):
        for y in range(1, size+1-s):
            sum = cumul_matrix[x+s][y+s] - cumul_matrix[x][y+s] - cumul_matrix[x+s][y] + cumul_matrix[x][y]
            if sum > max_sum_2:
                max_sum_2 = sum
                max_x_2 = x + 1
                max_y_2 = y + 1
                max_size_2 = s

print(max_x_2, max_y_2, max_size_2)

