def score(x):
    return sum([abs(x - num) * (abs(x - num) + 1) // 2 for num in nums])


with open('in.txt') as f:
    nums = [int(x) for x in f.read().split(',')]
    print(score(min(range(min(*nums), max(*nums)), key=score)))
