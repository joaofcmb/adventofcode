def within_bounds(coords):
    return 0 <= coords[0] < len(matrix) and 0 <= coords[1] < len(matrix[coords[0]])


with open('in.txt') as f:
    matrix = [list(map(int, list(x))) for x in f.read().splitlines()]
    distances = [[10000000 for _ in l] for l in matrix]

    distances[0][0] = 0

    stack = [(0, 1), (1, 0)]
    while len(stack) > 0:
        i, j = stack.pop()
        for x, y in filter(within_bounds, [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]):
            if distances[x][y] > distances[i][j] + matrix[x][y]:
                distances[x][y] = distances[i][j] + matrix[x][y]
                stack.append((x, y))
            elif distances[i][j] > distances[x][y] + matrix[i][j]:
                distances[i][j] = distances[x][y] + matrix[i][j]
                stack.append((i, j))

    print(distances[-1][-1])
