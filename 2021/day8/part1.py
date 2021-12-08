def is_easy_num(p):
    return len(p) <= 4 or len(p) == 7


with open('in.txt') as f:
    patterns, output = list(zip(*[map(str.split, x.split(" | ")) for x in f.read().splitlines()]))
    flatten_output = [p for line in output for p in line]

    print(len(list(filter(is_easy_num, flatten_output))))
