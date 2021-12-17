def is_valid(v):
    xi, yi = (0, 0)
    vx, vy = v

    while xi <= x2 and yi >= y1:
        xi += vx
        yi += vy

        if x1 <= xi <= x2 and y1 <= yi <= y2:
            return True

        vy -= 1
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
    return False


with open('in.txt') as f:
    x, y = f.read().split(': ')[1].split(', ')
    x1, x2 = map(int, x.split('=')[1].split('..'))
    y1, y2 = map(int, y.split('=')[1].split('..'))

    print(len(list(filter(is_valid, [(x, y) for x in range(1, x2 + 1) for y in range(y1, -y1)]))))
