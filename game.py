def tour_start():
    dims = [x for x in input("Enter your board dimensions: ").split()]
    visited = []
    squares = 1
    if validation_of_dims(dims):
        dim_x, dim_y = int(dims[0]), int(dims[1])
        start_position = [x for x in input("Enter the knight's starting position: ").split()]
        while not validation_of_position(dim_x, dim_y, start_position):
            start_position = [x for x in input("Enter the knight's starting position: ").split()]
        x, y = int(start_position[0]), int(start_position[1])
        visited.append((x, y))
        decision = input('Do you want to try the puzzle? (y/n): ')
        while decision != 'n' and decision != 'y':
            print('Invalid input!', end=' ')
            decision = input('Do you want to try the puzzle? (y/n): ')
        if decision == 'n':
            solve_kt(dim_x, dim_y, x, y, decision)
        elif decision == 'y':
            if solve_kt(dim_x, dim_y, x, y, decision):
                if validation_of_position(dim_x, dim_y, start_position):
                    artist(dim_x, dim_y, x, y, visited)
                game_continue(dim_x, dim_y, x, y, visited, squares)
    else:
        tour_start()
        return


def game_continue(dim_x, dim_y, x, y, visited, squares):
    next_move = [el for el in input('Enter your next move: ').split()]
    x_next, y_next = int(next_move[0]), int(next_move[1])

    if validation_of_move(dim_x, dim_y, x, y, next_move) and (y_next, x_next) not in visited:
        unblocked_moves = all(move in visited for move in get_all_moves(dim_x, dim_y, x_next, y_next))
        squares += 1
        artist(dim_x, dim_y, y_next, x_next, visited)
        if squares == dim_x * dim_y:
            print('What a great tour! Congratulations!')
            return
        if unblocked_moves:
            print('No more possible moves!\nYour knight visited {0} squares!'.format(squares))
            return
        visited.append((y_next, x_next))
        game_continue(dim_x, dim_y, x_next, y_next, visited, squares)
    else:
        print("Invalid move!", end=' ')
        game_continue(dim_x, dim_y, x, y, visited, squares)


def artist(dim_x, dim_y, x, y, visited):
    cell_size = len(str(dim_x * dim_y))
    print(' ' * len(str(dim_y)) + '-' * (dim_x * (cell_size + 1) + 3))
    for i in range(dim_y, 0, -1):
        print((' ' * (len(str(dim_y)) - len(str(i)))) + str(i) + '|', end=' ')
        for j in range(1, dim_x + 1):
            if (i, j) in visited:
                print(' ' * (cell_size - 1) + '*', end=' ')
                continue
            elif is_pot_move(x, y, i, j):
                print(' ' * (cell_size - 1) + amnt_of_moves(dim_x, dim_y, j, i), end=' ')
                continue
            elif i == x and j == y:
                print(' ' * (cell_size - 1) + 'X', end=' ')
                continue
            print('_' * cell_size, end=' ')
        print('|')
    print(' ' * len(str(dim_y)) + '-' * (dim_x * (cell_size + 1) + 3))
    print(' ' * (len(str(y)) + cell_size), end=' ')
    for i in range(1, dim_x + 1):
        print(i, end=' ' * cell_size)
    print()


def upgrade_artist(dim_x, dim_y, desk):
    cell_size = len(str(dim_x * dim_y))
    print("Here's the solution!")
    print(' ' * len(str(dim_y)) + '-' * (dim_x * (cell_size + 1) + 3))
    for i in range(dim_y, 0, -1):
        print((' ' * (len(str(dim_y)) - len(str(i)))) + str(i) + '|', end=' ')
        for j in range(1, dim_x + 1):
            print(' ' * (len(str(dim_x * dim_y)) - len(str(desk[i][j]))) + str(desk[i][j]), end=' ')
        print('|')
    print(' ' * len(str(dim_y)) + '-' * (dim_x * (cell_size + 1) + 3))
    print(' ' * (len(str(dim_y)) + cell_size), end=' ')
    for i in range(1, dim_x + 1):
        print(i, end=' ' * cell_size)
    print()


def validation_of_dims(array):
    if len(array) != 2 or not array[0].isdigit() or not array[1].isdigit() or \
            int(array[0]) < 1 or int(array[1]) < 1:
        print("Invalid dimensions!")
        return False
    return True


def validation_of_position(dim_x, dim_y, array):
    if len(array) != 2 or not array[1].isdigit() or not array[0].isdigit() or int(array[1]) < 1 or int(array[1]) > dim_y or \
            int(array[0]) < 1 or int(array[0]) > dim_x:
        print("Invalid position!")
        return False
    return True


def validation_of_move(dim_x, dim_y, x, y, array):
    if len(array) != 2 or not array[0].isdigit() or not array[1].isdigit() or int(array[0]) < 1 or int(array[1]) > dim_y or \
            int(array[1]) < 1 or int(array[0]) > dim_x or not is_pot_move(x, y, int(array[0]), int(array[1])):
        return False
    return True


def is_pot_move(x, y, x_n, y_n):
    if (abs(x - x_n) == 2 and abs(y - y_n) == 1) or (abs(x - x_n) == 1 and abs(y - y_n) == 2):
        return True
    return False


def get_all_moves(dim_x, dim_y, x, y):
    moves = []
    if x + 2 <= dim_x:
        if y + 1 <= dim_y:
            moves.append((x + 2, y + 1))
        if y - 1 >= 1:
            moves.append((x + 2, y - 1))

    if x - 2 >= 1:
        if y + 1 <= dim_y:
            moves.append((x - 2, y + 1))
        if y - 1 >= 1:
            moves.append((x - 2, y - 1))

    if x + 1 <= dim_x:
        if y + 2 <= dim_y:
            moves.append((x + 1, y + 2))
        if y - 2 >= 1:
            moves.append((x + 1, y - 2))

    if x - 1 >= 1:
        if y + 2 <= dim_y:
            moves.append((x - 1, y + 2))
        if y - 2 >= 1:
            moves.append((x - 1, y - 2))

    return moves


def amnt_of_moves(dim_x, dim_y, x, y):
    res = 0
    if x + 2 <= dim_x:
        if y + 1 <= dim_y:
            res += 1
        if y - 1 >= 1:
            res += 1

    if x - 2 >= 1:
        if y + 1 <= dim_y:
            res += 1
        if y - 1 >= 1:
            res += 1

    if x + 1 <= dim_x:
        if y + 2 <= dim_y:
            res += 1
        if y - 2 >= 1:
            res += 1

    if x - 1 >= 1:
        if y + 2 <= dim_y:
            res += 1
        if y - 2 >= 1:
            res += 1

    return str(res - 1)


def is_safe(dim_x, dim_y, x, y, board):
    if x >= 1 and y >= 1 and x <= dim_x and y <= dim_y and board[y][x] == -1:
        return True
    return False


def solve_kt(dim_x, dim_y, x, y, flag):
    board = [[-1] * (dim_x + 1) for i in range(dim_y + 1)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    board[y][x] = 1

    pos = 2

    if not solve_kt_util(dim_x, dim_y, board, x, y, move_x, move_y, pos):
        print("No solution exists!")
    else:
        if flag == 'n':
            upgrade_artist(dim_x, dim_y, board)
        return 1


def solve_kt_util(dim_x, dim_y, board, curr_x, curr_y, move_x, move_y, pos):
    if pos == dim_x * dim_y + 1:
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if is_safe(dim_x, dim_y, new_x, new_y, board):
            board[new_y][new_x] = pos
            if solve_kt_util(dim_x, dim_y, board, new_x, new_y, move_x, move_y, pos+1):
                return True

            board[new_y][new_x] = -1
    return False


if __name__ == "__main__":
    tour_start()
