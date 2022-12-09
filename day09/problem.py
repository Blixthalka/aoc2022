def read_file():
    f = open("data.txt", "r")
    return list(map(lambda x: x.strip().split(" "), f))

def run_1():
    places = {
        (0, 0): 1
    }
    head_pos = [0, 0]
    tail_pos = [0, 0]

    for inst in read_file():
        head_dx, head_dy = delta(inst[0])
        for _ in range(int(inst[1])):
            head_pos[0] += head_dy
            head_pos[1] += head_dx

            if not is_touching(head_pos, tail_pos):
                tail_pos[0] += close_gap_delta(tail_pos[0], head_pos[0])
                tail_pos[1] += close_gap_delta(tail_pos[1], head_pos[1])
                places[(tail_pos[0], tail_pos[1])] = 1

    return len(places)

def delta(direction):
    if direction == 'R':
        return 1, 0
    if direction == 'L':
        return -1, 0
    if direction == 'U':
        return 0, 1
    if direction == 'D':
        return 0, -1

def is_touching(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1

def close_gap_delta(a, b):
    if a == b:
        return 0
    elif a < b:
        return 1
    else:
        return -1

def run_2():
    places = {
        (0, 0): 1
    }
    head_pos = [0, 0]
    tail = [[0, 0] for _ in range(9)]

    for inst in read_file():
        head_dx, head_dy = delta(inst[0])
        for _ in range(int(inst[1])):
            head_pos[0] += head_dy
            head_pos[1] += head_dx

            for i, tail_pos in enumerate(tail):
                if i == 0:
                    prev_pos = head_pos
                else:
                    prev_pos = tail[i - 1]

                if not is_touching(prev_pos, tail_pos):
                    tail_pos[0] += close_gap_delta(tail_pos[0], prev_pos[0])
                    tail_pos[1] += close_gap_delta(tail_pos[1], prev_pos[1])

                    if i == len(tail) - 1:
                        places[(tail_pos[0], tail_pos[1])] = 1

    return len(places)

print(run_1())
print(run_2())