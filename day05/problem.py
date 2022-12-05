def map_input_element(line):
    res = line.split(",")
    return list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), res))

def read_file(size):
    f = open("data.txt", "r")

    instructions = []
    boxes = []
    for _ in range(size):
        boxes.append([])

    for line in f:
        if line.strip() == "":
            continue
        elif line.startswith("move"):
            inst = list(map(lambda y: int(y), filter(lambda x: x != '', line.strip().replace("move", "").replace("from", "").replace("to", "").split(" "))))
            instructions.append(inst)
            continue
        elif line.startswith(" 1"):
            continue

        trimmed = line.replace("]", "").replace("[", "").replace("\n", "").replace("    ", " -").split(" ")
        for i, value in enumerate(trimmed):
            if value == "-" or value == "":
                continue
            boxes[i].insert(0, value.replace("-", ""))

    return (instructions, boxes)

def run_1():
    data = read_file(9)
    boxes = data[1]

    for inst in data[0]:
        for _ in range(inst[0]):
            v = boxes[inst[1] - 1].pop()
            boxes[inst[2] - 1].append(v)

    return ''.join(list(map(lambda x: x.pop(), boxes)))


def run_2():
    data = read_file(9)
    boxes = data[1]
    for inst in data[0]:
        from_col = boxes[inst[1] - 1]
        v = from_col[len(from_col) - inst[0]:]
        boxes[inst[1] - 1] = from_col[:len(from_col) - inst[0]]
        boxes[inst[2] - 1].extend(v)

    return ''.join(list(map(lambda x: x.pop(), boxes)))

print(run_1())
print(run_2())