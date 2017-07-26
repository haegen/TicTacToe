# coding: utf-8
# Python 2.7

LEER = " "
X = 'X'
O = 'O'

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

player_one = X
player_two = O
fields = 9

def __main__():
    global field
    check = X
    
    field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print_field()
    
    while (True):
        
        if check == 0:
            break
        
        if (check == X):
            check = new_move(O)
        else:
            check = new_move(X)

def print_field():
    # print column header
    print("     1   2   3\n   +---+---+---+")
    for i in range(3):
        # print row header
        print((i + 1), " | " + field[i][0] + " | " + field[i][1] + " | " + field[i][2] + " | ")
        print("   +---+---+---+")
        
    print("")

def new_move(char):
    global fields
    print("Next player is ", char)
    row = raw_input("Row (1-3): ")
    column = raw_input("Column (1-3): ")
    print("")
    
    if (field[row-1][column-1] == LEER):
        field[row-1][column-1] = char
        print_field()
        
        if (is_winner()):
            return 0
    else:
        print_field()
        print("This field is already taken.")
        
        if (char == 'X'):
            return O
        else:
            return X
    
    fields -= 1
    if (fields > 0):
        return char
    else:
        print("All fields are taken.")
        return 0

def is_winner():
    if (   field[0][0] == player_one and field[0][1] == player_one and field[0][2] == player_one
        or field[1][0] == player_one and field[1][1] == player_one and field[1][2] == player_one
        or field[2][0] == player_one and field[2][1] == player_one and field[2][2] == player_one
        or field[0][0] == player_one and field[1][0] == player_one and field[2][0] == player_one
        or field[0][1] == player_one and field[1][1] == player_one and field[2][1] == player_one
        or field[0][2] == player_one and field[1][2] == player_one and field[2][2] == player_one
        or field[0][0] == player_one and field[1][1] == player_one and field[2][2] == player_one
        or field[0][2] == player_one and field[1][1] == player_one and field[2][0] == player_one
       ): 
            print("Player {} has won", player_one)
            return True
    elif ( field[0][0] == player_two and field[0][1] == player_two and field[0][2] == player_two
        or field[1][0] == player_two and field[1][1] == player_two and field[1][2] == player_two
        or field[2][0] == player_two and field[2][1] == player_two and field[2][2] == player_two
        or field[0][0] == player_two and field[1][0] == player_two and field[2][0] == player_two
        or field[0][1] == player_two and field[1][1] == player_two and field[2][1] == player_two
        or field[0][2] == player_two and field[1][2] == player_two and field[2][2] == player_two
        or field[0][0] == player_two and field[1][1] == player_two and field[2][2] == player_two
        or field[0][2] == player_two and field[1][1] == player_two and field[2][0] == player_two
       ): 
            print("Player {} has won", player_two)
            return True
    return False

__main__()
