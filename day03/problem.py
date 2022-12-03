def read_file():
    f = open("data.txt", "r")
    return list(map(lambda line: line.strip(), f))

def points(char):
    if char.lower() == char:
        return ord(char) - 96
    else:
        return ord(char) - 38

def run_1():
    sacks = read_file()
    sum = 0
    for sack in sacks:
        length = len(sack) // 2;
        for char in sack[:length]:
            if char in sack[length:]:
                sum += points(char)
                break
    return sum

def run_2():
    sacks = read_file()
    sum = 0
    for i in range(0, (len(sacks) // 3)):
        current_sacks = sacks[i*3:(i+1)*3]
        for char in current_sacks[0]:
            if char in current_sacks[1] and char in current_sacks[2]:
                sum += points(char)
                break
    return sum

print(run_1())
print(run_2())