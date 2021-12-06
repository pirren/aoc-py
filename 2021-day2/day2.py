# Day 2: Dive!


def part_a():
    commands = dict()
    for x in open("in.in").read().strip().split('\n'):
        val = x.split()
        if val[0] not in commands:
            commands[val[0]] = int(val[1])
        else:
            commands[val[0]] += int(val[1])
    print("part A:", (commands.get("down") - commands.get("up")) * commands.get("forward"))


def part_b():
    depth, dist, aim = 0, 0, 0
    for x in open("in.in").read().strip().split('\n'):
        data = x.split()
        command, val = data[0], int(data[1])
        if command == "forward":
            dist += val
            depth += aim * val
        if command == "down":
            aim += val
        if command == "up":
            aim -= val
    print("part B:", dist * depth)


part_a()
part_b()


