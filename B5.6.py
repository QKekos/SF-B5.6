
def coord_input_try(text):

    try:
        x, y = map(int, input(text).split())

        print('-------------------------')

        if x not in range(0, 3) or y not in range(0, 3):
            return coord_input_try('Input correct values:\n')

        return x, y

    except:
        print('-------------------------')
        return coord_input_try('Input correct values:\n') 

def print_field():

    for i in field:

        for k in i:
            print(k, end=' ')

        print('\n')

def check_winner():

    global current_turn
    global winner

    win = False

    for i in ['x', 'o']:

        for k in range(1, 4):

            if (
                # Horizontal
                field[k][1] == i and field[k][2] == i and field[k][3] == i or

                # Vertical
                field[1][k] == i and field[2][k] == i and field[3][k] == i
            ):
                win = True

        if (
            # Diagonal
            field[1][1] == i and field[2][2] == i and field[3][3] == i or
            field[3][1] == i and field[2][2] == i and field[1][3] == i
        ):
            win = True
        
        if win:
            current_turn = 'x' if current_turn == 'o' else 'o'
            print('-------------------------')
            print(current_turn, 'wins!')
            print('-------------------------')

            winner = True
            return

    if check_draw():

        print('-------------------------')
        print('Draw')
        print('-------------------------')

        winner = True

def check_draw():

    for i in field:
        for k in i:
            if k == '-':
                return False

    return True

def turn(x, y):

    global field
    global current_turn

    if field[x+1][y+1] == '-':
        field[x+1][y+1] = 'x' if current_turn == 'x' else 'o'
        current_turn = 'x' if current_turn == 'o' else 'o'
        print_field()
        check_winner()

    else:
        print('Input correct coordinates')


if __name__ == '__main__':

    current_turn = 'x'
    winner = False

    field = [
        [' ', '0', '1', '2'],
        ['0']+['-']*3,
        ['1']+['-']*3,
        ['2']+['-']*3,
    ]

    print('-------------------------')
    print_field()

    while not winner:

        print('-------------------------')
        x, y = coord_input_try('Iput row and column:\n')
        turn(x, y)
