def map_input_element(line, mapping):
    splitted = line.strip().split(" ")
    res = list(map(lambda s: mapping[s], splitted))
    return res

def read_file(mapping):
    f = open("data.txt", "r")
    return list(map(lambda line: map_input_element(line, mapping), f))

def game_points(opponent, me):
    if (opponent == me):
        return 3

    if (opponent == 'rock' and me == 'scissor'):
        return 0
    elif (opponent == 'paper' and me == 'rock'):
        return 0
    elif (opponent == 'scissor' and me == 'paper'):
        return 0

    return 6

def action_to_points(me):
    if (me == 'rock'):
        return 1
    elif (me == 'paper'):
        return 2
    elif (me == 'scissor'):
        return 3

def run_1():
    mapping = {
        'A': 'rock', 'B': 'paper', 'C': 'scissor',
        'X': 'rock', 'Y': 'paper', 'Z': 'scissor'
    }
    sum = 0
    for game in read_file(mapping):
        sum += game_points(game[0], game[1])
        sum += action_to_points(game[1])
    return sum

def run_2():
    mapping = {
        'A': 'rock', 'B': 'paper', 'C': 'scissor',
        'X': 0, 'Y': 3, 'Z': 6
    }
    sum = 0
    for game in read_file(mapping):
        for draw in ['rock', 'paper', 'scissor']:
            if (game_points(game[0], draw) == game[1]):
                sum += game_points(game[0], draw)
                sum += action_to_points(draw)
                break

    return sum

Result1 = run_1()
Result2 = run_2()
print(Result1)
print(Result2)