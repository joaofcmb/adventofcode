import itertools

with open('in.txt') as f:
    cmd_list = [line.split() for line in f.read().splitlines()]

    def is_horizontal_cmd(x): return x[0] == 'forward'

    final_horizontal = sum(int(x[1]) for x in filter(is_horizontal_cmd, cmd_list))
    final_depth = sum(
        int(x[1]) if x[0] == 'down' else -int(x[1]) for x in itertools.filterfalse(is_horizontal_cmd, cmd_list)
    )
    print(final_horizontal * final_depth)
