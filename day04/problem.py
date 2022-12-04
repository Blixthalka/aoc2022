def map_input_element(line):
    res = line.split(",")
    return list(map(lambda x: list(map(lambda y: int(y), x.split("-"))), res))

def read_file():
    f = open("data.txt", "r")
    return list(map(lambda line: map_input_element(line.strip()), f))

def run_1():
    sum = 0
    for input in read_file():
        f = input[0]
        s = input[1]
        if f[0] <= s[0] and f[1] >= s[1]:
            sum += 1
        elif s[0] <= f[0] and s[1] >= f[1]:
            sum += 1
    return sum

def is_between(x, range):
    return x >= range[0] and x <= range[1]

def run_2():
    sum = 0
    for input in read_file():
        first = input[0]
        second = input[1]

        if is_between(first[0], second):
            sum += 1
        elif is_between(first[1], second):
            sum += 1
        elif is_between(second[0], first):
            sum += 1

    return sum

print(run_1())
print(run_2())