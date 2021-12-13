import itertools
from collections import defaultdict

with open('in.txt') as f:
    [dots, folds] = f.read().split('\n\n')
    dots = set(tuple(map(int, dot.split(','))) for dot in dots.splitlines())
    folds = [fold.split()[-1].split('=') for fold in folds.splitlines()]
    folds = [(x, int(y)) for x, y in folds]

    print(dots)
    for fold_t, val in folds:
        if fold_t == 'x':
            for x, y in [(i, j) for i, j in dots if i > val]:
                dots.remove((x, y))
                dots.add((x - 2 * (x - val), y))
        elif fold_t == 'y':
            for x, y in [(i, j) for i, j in dots if j > val]:
                dots.remove((x, y))
                dots.add((x, y - 2 * (y - val)))

    for j in range(10):
        for i in range(50):
            if (i, j) in dots:
                print("#", end="")
            else:
                print(".", end="")
        print()
