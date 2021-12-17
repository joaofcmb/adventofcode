with open('in.txt') as f:
    x, y = f.read().split(': ')[1].split(', ')
    x1, x2 = map(int, x.split('=')[1].split('..'))
    y1, y2 = map(int, y.split('=')[1].split('..'))

    print(sum(range(abs(y1))))
