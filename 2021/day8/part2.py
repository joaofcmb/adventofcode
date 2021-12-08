import operator


def pattern_num(p, segments):
    p_set = set(list(p))

    if len(p) == 2:
        return '1'
    elif len(p) == 3:
        return '7'
    elif len(p) == 4:
        return '4'
    elif len(p) == 5:
        if segments[1] in p_set:
            return '5'
        elif segments[5] in p_set:
            return '3'
        else:
            return '2'
    elif len(p) == 6:
        if segments[2] not in p_set:
            return '6'
        elif segments[3] not in p_set:
            return '0'
        else:
            return '9'
    elif len(p) == 7:
        return '8'


def value(patterns, outputs):
    patterns = sorted([set(list(p)) for p in patterns], key=len)

    segment_a = (patterns[1] - patterns[0]).pop()

    segment_c, segment_f = map(operator.itemgetter(0), sorted(
        [(x, len([p for p in patterns if x in p])) for x in patterns[0]], key=operator.itemgetter(1)
    ))

    segments_bd = patterns[2] - patterns[0]
    segment_b, segment_d = map(operator.itemgetter(0), sorted(
        [(x, len([p for p in patterns if x in p])) for x in segments_bd], key=operator.itemgetter(1)
    ))

    patterns = [p - {segment_a, segment_b, segment_c, segment_d, segment_f} for p in patterns]
    segments_eg = max(patterns, key=len)
    segment_e, segment_g = map(operator.itemgetter(0), sorted(
        [(x, len([p for p in patterns if x in p])) for x in segments_eg], key=operator.itemgetter(1)
    ))

    return int(''.join(
        [pattern_num(p, [segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g]) for p in outputs]
    ))


with open('in.txt') as f:
    patterns_and_outputs = [map(str.split, x.split(" | ")) for x in f.read().splitlines()]
    print(sum(value(*x) for x in patterns_and_outputs))
