import heapq
import itertools


def five(line):
    five_lines = []
    for offset in range(5):
        five_lines.append([9 if elem + offset == 9 else (elem + offset) % 9 for elem in line])
    return five_lines


def within_bounds(coords):
    return 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[coords[0]])


with open('in.txt') as f:
    matrix = [list(map(int, list(x))) for x in f.read().splitlines()]
    five_matrix = [five(line) for line in matrix]

    matrix = []
    for i in range(5):
        matrix += [list(itertools.chain(*five(five_matrix[li][i]))) for li in range(len(five_matrix))]

    distances = [[10000000 for _ in l] for l in matrix]
    distances[0][0] = 0

    visited = set()
    queue = []
    heapq.heappush(queue, (0, (0, 0)))
    while len(queue) > 0:
        _, (i, j) = heapq.heappop(queue)
        visited.add((i, j))

        for x, y in filter(within_bounds, [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]):
            if (x, y) not in visited and distances[x][y] > distances[i][j] + matrix[x][y]:
                distances[x][y] = distances[i][j] + matrix[x][y]
                heapq.heappush(queue, (distances[x][y], (x, y)))

    print(distances[-1][-1])
