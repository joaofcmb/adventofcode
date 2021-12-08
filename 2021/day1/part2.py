with open('in.txt') as f:
    L = [int(x) for x in f.read().splitlines()]
    sum3_L = [x + y + z for x, y, z in zip(L, L[1::], L[2::])]
    print(len([x for x in zip(sum3_L, sum3_L[1::]) if x[1] > x[0]]))
