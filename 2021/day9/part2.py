def get_basins(prev_start_idx, prev_sep_idx, prev_basins, widths, start_idx, sep_idx):
    prev = list(zip(prev_basins, prev_start_idx, prev_sep_idx))
    curr = list(zip(widths, start_idx, sep_idx))

    basins = []
    pi = ci = 0
    while pi < len(prev) and ci < len(curr):
        basin, p_start_i, p_sep_i = prev[pi]
        width, start_i, sep_i = curr[ci]

        while



    return []


with open('in.txt') as f:
    matrix = [x for x in f.read().splitlines()]

    prev_sep_idx = list(range(len(matrix[0])))
    prev_start_idx = [0] + prev_sep_idx[:-1]
    prev_basins = [0] * len(matrix[0])
    for i, line in enumerate(matrix):
        widths = list(map(len, line.split('9')))
        sep_idx = [sum(widths[0:i+1]) + len(widths[0:i+1]) - 1 for i in range(len(widths))]
        start_idx = [0] + sep_idx[:-1]
        basins, start_idx, sep_idx = get_basins(prev_start_idx, prev_sep_idx, prev_basins, widths, start_idx, sep_idx)
        # basins = [w + sum(
        #     [pb for (pb, p_start_i, psi) in zip(prev_basins, prev_start_idx, prev_sep_idx)
        #      if (start_si + 1 < psi <= si + 1) or (start_si + 1 < p_start_i <= si + 1)]
        # ) for (w, start_si, si) in zip(widths, start_idx, sep_idx)]

        print(widths)
        print(start_idx)
        print(sep_idx)
        print(basins)
        print()

        prev_sep_idx = sep_idx
        prev_start_idx = start_idx
        prev_basins = basins
