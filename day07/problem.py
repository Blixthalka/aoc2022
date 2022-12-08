def read_file():
    f = open("data.txt", "r")
    return list(map(lambda x: x.strip(), f))

def calc_size(node):
    if node[3] == []:
        return node[2]

    size = 0
    for child in node[3]:
        size += calc_size(child)

    node[2] = size
    return size

def construct_tree():
    node = ["", None, None, []]
    for inst in read_file():
        if inst.startswith("$ ls"):
            continue
        elif inst.startswith("$ cd /"):
            continue
        elif inst.startswith("$ cd .."):
            node = node[1]
        elif inst.startswith("$ cd"):
            dirname = inst.replace("$ cd ", "")
            node = list(filter(lambda n: n[0] == (node[0] + "/" + dirname), node[3]))[0]
        elif inst.startswith("dir "):
            dirname = inst.replace("dir ", "")
            node[3].append([node[0] + "/" + dirname, node, None, []])
        else:
            split = inst.split(" ")
            node[3].append([node[0] + "/" + split[1], node, int(split[0]), []])

    while node[0] != "":
        node = node[1]

    calc_size(node)
    return node

def sum_dirs_under(node):
    if node[3] == []:
        return 0

    points = 0
    for child in node[3]:
        points += sum_dirs_under(child)

    if node[2] < 100_000:
        points += node[2]

    return points

def run_1():
    return sum_dirs_under(construct_tree())

def find_closest(node, needed):
    if node[3] == []:
        return None

    best = None
    for child in node[3]:
        new_best = find_closest(child, needed)
        if (new_best is not None and new_best > needed) and (best is None or new_best < best):
            best = new_best

    if node[2] > needed and (best is None or node[2] < best):
        best = node[2]

    return best

def run_2():
    node = construct_tree()
    needed = 30_000_000 - (70_000_000 - node[2])
    return find_closest(node, needed)

print(run_1())
print(run_2())