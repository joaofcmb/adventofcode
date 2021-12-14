from collections import Counter

with open('in.txt') as f:
    [polymer, rules] = f.read().split('\n\n')
    polymer = list(polymer)
    rules = dict(tuple(r.split(' -> ')) for r in rules.splitlines())

    counters = dict([(k, Counter(list(k) + list(v))) for k, v in rules.items()])

    for s in range(39):
        next_counters = dict()
        for k, v in rules.items():
            next_counters[k] = counters[k[0] + v] + counters[v + k[1]] - Counter(v)
        counters = next_counters

    counter = Counter(polymer[0])
    for x, y in zip(polymer, polymer[1:]):
        counter += counters[x + y] - Counter(x)
    print(counter.most_common(1)[0][1] - counter.most_common()[-1][1])
