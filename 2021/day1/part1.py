with open('in.txt') as f:
    L = [int(x) for x in f.read().splitlines()]
    print(len([x for x in zip(L, L[1::]) if x[1] > x[0]]))
