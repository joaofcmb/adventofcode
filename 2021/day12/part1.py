from collections import defaultdict

with open('in.txt') as f:
    raw_edges = [x.split('-') for x in f.read().splitlines()]

    edges = defaultdict(list)
    for [a, b] in raw_edges:
        edges[a].append(b)
        edges[b].append(a)

    stack = [['start']]
    paths = 0
    while len(stack) > 0:
        path = stack.pop()
        if path[-1] == 'end':
            paths += 1
            continue

        neighbors = edges[path[-1]]
        for n in neighbors:
            if n.isupper() or n not in path:
                stack.append(path + [n])

    print(paths)
