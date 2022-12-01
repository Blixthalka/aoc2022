def read_file():
    f = open("data.txt", "r")

    elves = []
    current_elve = 0

    for line in f:
        if line == '\n':
            elves.append(current_elve)
            current_elve = 0
            continue
        current_elve += int(line)

    elves.append(current_elve)
    return elves

def run_take(num):
    elves = read_file()
    sorted_elves = sorted(elves, reverse=True)
    return sum(sorted_elves[:num])

def run_1():
    return run_take(1)

def run_2():
    return run_take(3)

Result1 = run_1()
Result2 = run_2()
print(Result1)
print(Result2)