import bitarray
import statistics

from bitarray.util import ba2int

with open('in.txt') as f:
    byte_list = [byte for byte in f.read().splitlines()]
    byte_list_transposed = list(map(list, zip(*byte_list)))

    gamma = bitarray.bitarray(len(byte_list_transposed))
    for i, L in enumerate(byte_list_transposed):
        gamma[i] = bool(int(statistics.mode(L)))

    print(ba2int(gamma) * ba2int(~gamma))
