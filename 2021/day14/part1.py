from collections import Counter

with open('in.txt') as f:
    [polymer, rules] = f.read().split('\n\n')
    polymer = list(polymer)
    rules = dict(tuple(r.split(' -> ')) for r in rules.splitlines())

    for s in range(10):
        new_polymer = [polymer[0]]
        for (i, x), y in zip(enumerate(polymer), polymer[1:]):
            new_polymer += [rules[x + y], y]
        polymer = new_polymer

    counter = Counter(polymer)
    print(counter.most_common(1)[0][1] - counter.most_common()[-1][1])
