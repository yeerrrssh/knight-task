def add_values_for_test():
    global counter
    global points
    counter = 1
    points = []
    return counter, points


def move(x, y, step=0):
    if step == counter:
        points.append(str(y) + str(x))
    else:
        if x > 1 and y > 2:
            move(x - 1, y - 2, step + 1)
        if x > 2 and y > 1:
            move(x - 2, y - 1, step + 1)
        if x < 8 and y > 2:
            move(x + 1, y - 2, step + 1)
        if x < 7 and y > 1:
            move(x + 2, y - 1, step + 1)
        if x < 7 and y < 8:
            move(x + 2, y + 1, step + 1)
        if x < 8 and y < 7:
            move(x + 1, y + 2, step + 1)
        if x > 1 and y < 7:
            move(x - 1, y + 2, step + 1)
        if x > 2 and y < 8:
            move(x - 2, y + 1, step + 1)
    return points


def research(entrance):
    global points
    points = []
    x0 = entrance[0]
    y0 = entrance[1]
    move(x0, y0)
    points = ['ABCDEFGH'[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]
    return points


def knight_move(start_position, finish_position):
    global counter
    mid_results = []
    counter = 0
    while finish_position not in mid_results:
        counter += 1
        mid_results = research(start_position)
    return counter


def knights_collision(first, second):
    global counter
    first_mid_results = []
    second_mid_results = []
    counter = 0
    while not set(first_mid_results) & set(second_mid_results):
        counter += 1
        first_mid_results += research(first)
        second_mid_results += research(second)
    return counter


def solve(start_position, final_position, action):
    x0, y0 = list(start_position)
    x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
    y0 = int(y0)
    x_f, y_f = list(final_position)
    x_f = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x_f]
    y_f = int(y_f)
    if action == '1':
        print('Ходов нужно:', knight_move((x0, y0), final_position))
    if action == '2':
        print('Ходов нужно:', knights_collision((x0, y0), (x_f, y_f)))
    if action == '3':
        print('1) Ходов нужно:', knight_move((x0, y0), final_position))
        print('2) Ходов нужно:', knights_collision((x0, y0), (x_f, y_f)))
    return knight_move((x0, y0), final_position), knights_collision((x0, y0), (x_f, y_f))
