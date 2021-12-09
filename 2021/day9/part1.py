def line_low_points(low_idxs, j, line):
    return [line[i] for i in low_idxs if is_col_low(i, j, line[i])]


def is_col_low(i, j, point):
    if j == 0:
        return point < matrix[j+1][i]
    elif j == len(matrix) - 1:
        return point < matrix[j-1][i]
    else:
        return point < matrix[j+1][i] and point < matrix[j-1][i]


def is_line_low(i, line):
    if i == 0:
        return line[i] < line[i+1]
    elif i == len(line) - 1:
        return line[i] < line[i-1]
    else:
        return line[i] < line[i-1] and line[i] < line[i+1]


with open('in.txt') as f:
    matrix = [list(map(int, list(x))) for x in f.read().splitlines()]

    line_low_idxs = [[i for i in range(len(line)) if is_line_low(i, line)] for line in matrix]
    low_points = [p for (i, line) in enumerate(matrix) for p in line_low_points(line_low_idxs[i], i, line)]

    print(sum(p+1 for p in low_points))
