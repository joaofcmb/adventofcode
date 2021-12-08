with open('in.txt') as f:
    cmd_list = [line.split() for line in f.read().splitlines()]
    aim = final_horizontal = final_depth = 0

    for cmd, val in cmd_list:
        if cmd == 'up':
            aim -= int(val)
        elif cmd == 'down':
            aim += int(val)
        else:
            final_horizontal += int(val)
            final_depth += aim * int(val)

    print(final_horizontal * final_depth)
