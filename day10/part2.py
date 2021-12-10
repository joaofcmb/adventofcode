import functools
import statistics

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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
            return -1

    s = 0
    for x in stack[::-1]:
        s *= 5
        s += points[chars[x]]
    return s


with open('in.txt') as f:
    lines = [x for x in f.read().splitlines()]
    print(statistics.median_high(filter(lambda x: x > -1, map(score, lines))))
