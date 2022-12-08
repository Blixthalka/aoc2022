import functools

def read_file():
    f = open("data.txt", "r")
    v =  list(map(lambda x: [*x.strip()], f))
    return list(map(lambda x: list(map(lambda y: int(y), x)), v))

def is_visible(data, x_len, y_len, x, y, dir):
    dx, dy = dir
    cur_x = x
    cur_y = y
    while not is_edge(cur_x, cur_y, x_len, y_len):
        cur_x += dx
        cur_y += dy
        if data[y][x] <= data[cur_y][cur_x]:
            return False
    return True

def run_1():
    data = read_file()

    x_len = len(data[0])
    y_len = len(data)
    visible = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for x in range(x_len):
        for y in range(y_len):
            if any(list(map(lambda d: is_visible(data, x_len, y_len, x, y, d), directions))):
                visible += 1

    return visible

def is_edge(x, y, x_len, y_len):
    return x == 0 or x == (x_len - 1) or y == 0 or y == (y_len - 1)

def scenic_score_direction(data, x_len, y_len, x, y, dx, dy):
    score = 0
    cur_x = x
    cur_y = y
    while not is_edge(cur_x, cur_y, x_len, y_len):
        cur_x += dx
        cur_y += dy
        if data[y][x] > data[cur_y][cur_x]:
            score += 1
        else:
            score += 1
            break

    return score

def scenic_score(data, x_len, y_len, x, y):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    fun = lambda d: scenic_score_direction(data, x_len, y_len, x, y, d[0], d[1])
    scores = list(map(fun, directions))
    return functools.reduce(lambda a, b: a * b, scores, 1)

def run_2():
    data = read_file()

    x_len = len(data)
    y_len = len(data[0])
    best_score = 0

    for x in range(x_len):
        for y in range(y_len):
            score = scenic_score(data, x_len, y_len, x, y)
            if score > best_score:
                best_score = score

    return best_score

print(run_1())
print(run_2())