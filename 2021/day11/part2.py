with open('in.txt') as f:
    matrix = [list(map(int, list(x))) for x in f.read().splitlines()]
    size = sum(map(len, matrix))

    for s in range(1000):
        flashes = 0
        matrix = [[x + 1 for x in line] for line in matrix]

        current_flashes = [(i, j, x) for i, line in enumerate(matrix) for j, x in enumerate(line) if x > 9]
        while len(current_flashes) > 0:
            i, j, flash = current_flashes.pop()
            flashes += 1

            adjacent_coords = [
                (i-1, j - 1), (i - 1, j), (i - 1, j + 1),
                (i, j - 1), (i, j), (i, j + 1),
                (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)
            ]
            for (n, m) in adjacent_coords:
                if n < 0 or m < 0 or n >= len(matrix) or m >= len(matrix[n]):
                    continue

                matrix[n][m] += 1
                if matrix[n][m] == 10:
                    current_flashes.append((n, m, matrix[n][m]))

        matrix = [[0 if x > 9 else x for x in line] for line in matrix]

        if flashes >= size:
            print(s+1)
            break



