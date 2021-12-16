import functools
import operator

from bitarray import bitarray
from bitarray.util import hex2ba, ba2int


def value(packet_tree):
    print(packet_tree)
    version, type, content = packet_tree

    if type == 0:
        return sum(map(value, content))
    elif type == 1:
        return functools.reduce(operator.mul, map(value, content))
    elif type == 2:
        return min(map(value, content))
    elif type == 3:
        return max(map(value, content))
    elif type == 4:
        return content
    elif type == 5:
        return int(value(content[0]) > value(content[1]))
    elif type == 6:
        return int(value(content[0]) < value(content[1]))
    else:
        return int(value(content[0]) == value(content[1]))


def packet(i):
    end = i + 3
    p_version = ba2int(ba[i:end])
    i = end

    end = i + 3
    p_type = ba2int(ba[i:end])
    i = end

    if p_type == 4:
        is_not_last = True
        literal = bitarray()
        while is_not_last:
            is_not_last = ba[i]
            i += 1

            end = i + 4
            literal += ba[i:end]
            i = end

        return i, (p_version, p_type, ba2int(literal))
    else:
        length_type = ba[i]
        i += 1

        if length_type:
            end = i + 11
            number = ba2int(ba[i:end])
            i = end

            sub_packets = []
            for _ in range(number):
                i, sub_packet = packet(i)
                sub_packets.append(sub_packet)

            return i, (p_version, p_type, sub_packets)
        else:
            end = i + 15
            number = ba2int(ba[i:end])
            i = end

            j = i
            i += number
            sub_packets = []
            while j < i:
                j, sub_packet = packet(j)
                sub_packets.append(sub_packet)

            return i, (p_version, p_type, sub_packets)


with open('in.txt') as f:
    ba = hex2ba(f.read())
    packet = packet(0)[1]
    print(value(packet))
