import functools
import operator
from functools import lru_cache


@lru_cache(maxsize=None)
def basin_size(x, y):
    count = 0
    stack = [(x, y)]

    while len(stack) > 0:
        i, j = stack.pop()
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or matrix[i][j] == 9:
            continue
        else:
            matrix[i][j] = 9
            count += 1
            stack.append((i-1, j))
            stack.append((i+1, j))
            stack.append((i, j-1))
            stack.append((i, j+1))

    return count

def low_idxs(l_low_idxs, j, line):
    return [i for i in l_low_idxs if is_col_low(i, j, line[i])]


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
    basin_sizes = [basin_size(i, j) for (i, line) in enumerate(matrix) for j in low_idxs(line_low_idxs[i], i, line)]
    print(functools.reduce(operator.mul, sorted(basin_sizes, reverse=True)[0:3]))
