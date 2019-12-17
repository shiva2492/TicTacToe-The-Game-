# Deciding the data structure to use for the grid
initial_grid = [['  ','  ','  '] for i in range(3)]
# print(initial_grid)

# Function to print the grid
def printGrid():
    for row in initial_grid:
        row_str = ''
        for i in range(len(row)):
            if i == 0 :
                row_str +=  "| {} |".format(row[i])
            else:
                row_str +=  " {} |".format(row[i])
        print(row_str)

# Function to alter the grid one at a time
def move(icon, position):
    inner_position = position
    outer_position = int(position / 3)
    elem = initial_grid[outer_position]
    
    if inner_position - 3 < 0:
        if elem[inner_position] == "  ":
            elem[inner_position] = icon
        else:
            print()
            print("That space is taken!")
        
    else:
        inner_position = inner_position - 3 * outer_position
        if elem[inner_position] == "  ":
            elem[inner_position] = icon
        else:
            print()
            print("That space is taken!")
       

    # print(initial_grid)


# Function to decide who is the triumph
def isVictory(player):
    temp = False
    first_col = []
    last_col = []
    start_diagonal = []
    end_diagonal = []
    
    for i in range(len(initial_grid)):
        length = len(initial_grid[i])
        first_col.append(initial_grid[i][0])
        last_col.append(initial_grid[i][length-1])
        start_diagonal.append(initial_grid[i][i])
        end_diagonal = start_diagonal[::-1]
        temp = (len(set(initial_grid[i])) == 1 and initial_grid[i][0] == player)
        if(temp):
            break
        temp = (len(first_col) == 3 and len(set(first_col)) == 1 and first_col[0] == player)
        if(temp):
            break
        temp = (len(last_col) == 3 and len(set(last_col)) == 1 and last_col[0] == player)
        if(temp):
            break
        temp = (len(start_diagonal) == 3 and len(set(start_diagonal)) == 1 and start_diagonal[0] == player)
        if(temp):
            break
        temp = (len(end_diagonal) == 3 and len(set(end_diagonal)) == 1 and end_diagonal[0] == player)
        if(temp):
            break

    return temp
    

# Function to check if game is draw
def isDraw():
    flat_list = [item for sublist in initial_grid for item in sublist]
    
    if '  ' not in flat_list:
        return True
    else:
        return False


# final loop with checks for wins and draws
while True:
    player_one = "X"
    player_two = "0"
    printGrid()
    position = int(input("Player {}, Your next move..? ".format(player_one)).strip())
    move(player_one, position - 1)
    printGrid()
    victor = isVictory(player_one)
    if victor:
        print("You win player {}".format(player_one))
        break
    elif isDraw():
        print("The match is a draw")
        break
    position = int(input("Player {}, Your next move..? ".format(player_two)).strip())
    move(player_two, position - 1)
    victor = isVictory(player_two)
    if victor:
        printGrid()
        print("You win player {}".format(player_two))
        break
    elif isDraw():
        printGrid()
        print("The match is a draw")
        break
