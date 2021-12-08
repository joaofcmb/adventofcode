with open('in.txt') as f:
    # 0 days left
    day_after = [1] * 9
    for _ in range(80):
        new_day = [day_after[6] + day_after[8]] + day_after[:8]
        day_after = new_day.copy()

    ages = [int(x) for x in f.read().split(',')]
    print(sum(new_day[x] for x in ages))
