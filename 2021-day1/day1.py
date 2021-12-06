# Day 1: Sonar Sweep

Data = [int(x) for x in open("in.in").read().split('\n')]


def part_a():
    incr = 0
    for d in range(len(Data))[1:]:
        if Data[d] > Data[d - 1]:
            incr = incr + 1

    print("part A:", incr)


def part_b():
    incr = 0
    for d in range(len(Data))[3:]:
        if Data[d] + Data[d - 1] + Data[d -2] > Data[d - 1] + Data[d - 2] + Data[d - 3]:
            incr = incr + 1
    print("part B:", incr)


part_a()
part_b()


