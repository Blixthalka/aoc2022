def read_file():
    f = open("data.txt", "r")
    return list(f)[0].strip()


def is_unique(seq):
    for i in range(len(seq)):
        for j in range(len(seq)):
            if i == j:
                continue

            if seq[i] == seq[j]:
                return False
    return True

def run(size):
    s = read_file()

    seq = ''
    for index, c in enumerate(s):
        seq += c
        if len(seq) < size:
            continue

        if is_unique(seq):
            return index + 1

        seq = seq[1:]

    return None

def run_1():
    return run(4)

def run_2():
    return run(14)

print(run_1())
print(run_2())