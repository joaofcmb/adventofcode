points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

chars = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def score(line):
    stack = []
    for c in list(line):
        if c in chars.keys():
            stack.append(c)
        elif c != chars[stack.pop()]:
            return points[c]

    return 0


with open('in.txt') as f:
    lines = [x for x in f.read().splitlines()]
    print(sum(map(score, lines)))
