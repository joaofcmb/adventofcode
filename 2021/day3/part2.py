import bitarray
import statistics

from bitarray.util import ba2int


def oxygen_rating(bl, i):
    if len(bl) == 1:
        return ba2int(bitarray.bitarray(bl[0]))

    modes = statistics.multimode(list(zip(*bl))[i])
    msbit = modes[0] if len(modes) == 1 else '1'

    return oxygen_rating([byte for byte in bl if byte[i] == msbit], i + 1)


def c02_rating(bl, i):
    if len(bl) == 1:
        return ba2int(bitarray.bitarray(bl[0]))

    modes = statistics.multimode(list(zip(*bl))[i])
    lsbit = '1' if len(modes) == 1 and modes[0] == '0' else '0'

    return c02_rating([byte for byte in bl if byte[i] == lsbit], i + 1)

with open('in.txt') as f:
    byte_list = [byte for byte in f.read().splitlines()]
    byte_list_transposed = list(map(list, zip(*byte_list)))

    print(oxygen_rating(byte_list, 0) * c02_rating(byte_list, 0))
