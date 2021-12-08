import operator


def win(board):
    board_by_num_idx = [[num_list.index(num) for num in line] for line in board]
    board_by_num_idx_transposed = list(map(list, zip(*board_by_num_idx)))
    return min(*[max(line) for line in board_by_num_idx],
               *[max(line) for line in board_by_num_idx_transposed],
               # The below lines are counting diagonals which only later realized are being ignored.
               # Part 1 result is the same though, in Part 2 result is different
               max([line[i] for i, line in enumerate(board_by_num_idx)]),
               max([line[i] for i, line in enumerate(board_by_num_idx_transposed)]))


with open('in.txt') as f:
    nums, _, *boards = [x for x in f.read().splitlines()]
    num_list = [int(num) for num in nums.split(',')]
    board_list = [[]]
    for l in [[int(num) for num in line.split()] for line in boards]:
        if len(l) == 0:
            board_list.append([])
        else:
            board_list[-1].append(l)

    win_board, win_num_idx = min(zip(board_list, map(win, board_list)), key=operator.itemgetter(1))
    print(num_list[win_num_idx] * sum([x for line in win_board for x in line if x not in num_list[:win_num_idx+1]]))
