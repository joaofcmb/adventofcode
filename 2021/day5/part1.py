import re

import bitarray

with open('in.txt') as f:
    segments = [list(map(int, re.split(" -> |,", segment))) for segment in f.read().splitlines()]
    mapsize = max(x for segment in segments for x in segment) + 1
    linemap = [mapsize * [0] for _ in range(mapsize)]

    for x1, y1, x2, y2 in segments:
        if x1 == x2:
            if y1 <= y2:
                for y in range(y1, y2 + 1):
                    linemap[x1][y] += 1
            else:
                for y in range(y2, y1 + 1):
                    linemap[x1][y] += 1
        elif y1 == y2:
            if x1 <= x2:
                for x in range(x1, x2 + 1):
                    linemap[x][y1] += 1
            else:
                for x in range(x2, x1 + 1):
                    linemap[x][y1] += 1

    print(len(list(filter(lambda x: x > 1, [x for line in linemap for x in line]))))
