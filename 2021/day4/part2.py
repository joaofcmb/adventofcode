import operator


def win(board):
    board_by_num_idx = [[num_list.index(num) for num in line] for line in board]

    return min(*[max(line) for line in board_by_num_idx],
               *[max(line) for line in list(map(list, zip(*board_by_num_idx)))])


with open('in.txt') as f:
    nums, _, *boards = [x for x in f.read().splitlines()]
    num_list = [int(num) for num in nums.split(',')]
    board_list = [[]]
    for l in [[int(num) for num in line.split()] for line in boards]:
        if len(l) == 0:
            board_list.append([])
        else:
            board_list[-1].append(l)

    last_win_board, last_win_num_idx = max(zip(board_list, map(win, board_list)), key=operator.itemgetter(1))
    print(num_list[last_win_num_idx] *
          sum([x for line in last_win_board for x in line if x not in num_list[:last_win_num_idx + 1]]))
