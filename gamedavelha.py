# cells pattern
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def gameui(pattern):
    print("---------")
    print("| " + pattern[0] + " " + pattern[1] + " " + pattern[2] + " |")
    print("| " + pattern[3] + " " + pattern[4] + " " + pattern[5] + " |")
    print("| " + pattern[6] + " " + pattern[7] + " " + pattern[8] + " |")
    print("---------")


gameui(cells)

# variables to be used in the code
count = 0
os = 0
xs = 0
ended = True
owin = 0
xwin = 0
impossible = False
dic = {
    "1": {"1": 0, "2": 1, "3": 2},
    "2": {"1": 3, "2": 4, "3": 5},
    "3": {"1": 6, "2": 7, "3": 8}
}

for i in cells:
    if i == 'O':
        os = os + 1
    elif i == 'X':
        xs = xs + 1
    else:
        ended = False


# function to determine the winner
def who(tipo):
    global owin
    global xwin
    if tipo == 'OOO':
        owin = owin + 1
    elif tipo == 'XXX':
        xwin = xwin + 1


# movement function
def move(coord1, coord2, symbol):
    global cells
    global nextmove
    global count  # while to check if the coordinates are in the range
    while int(coord1) > 3 or int(coord2) > 3 or int(coord1) <= 0 or int(coord2) <= 0:
        print("Coordinates should be from 1 to 3!")
        nextmove = input("Enter the coordinates:").split()
        coord1 = nextmove[0]
        coord2 = nextmove[1]
    sla = dic[coord1]   # while to check if the coordinates are occupied
    while not cells[sla[coord2]] == " ":
        print("This cell is occupied! Choose another one!")
        nextmove = input("Enter the coordinates:").split()
        coord1 = nextmove[0]
        coord2 = nextmove[1]
        sla = dic[coord1]

    count += 1
    cells[sla[coord2]] = symbol
    gameui(cells)


def hasnumbers(inputstring):
    return any(char.isdigit() for char in inputstring)


# for loop to determine how much Os and Xs
def gamestate(cells):
    global os
    global xs
    global ended
    global impossible
    # horizontal win confirmation
    if cells[0] + cells[1] + cells[2] != '___':
        who(cells[0] + cells[1] + cells[2])
    if cells[3] + cells[4] + cells[5] != '___':
        who(cells[3] + cells[4] + cells[5])
    if cells[6] + cells[7] + cells[8] != '___':
        who(cells[6] + cells[7] + cells[8])
    # vertical win confirmation
    if cells[0] + cells[3] + cells[6] != '___':
        who(cells[0] + cells[3] + cells[6])
    if cells[1] + cells[4] + cells[7] != '___':
        who(cells[1] + cells[4] + cells[7])
    if cells[2] + cells[5] + cells[8] != '___':
        who(cells[2] + cells[5] + cells[8])
    # diagonal win confirmation
    if cells[0] + cells[4] + cells[8] != '___':
        who(cells[0] + cells[4] + cells[8])
    if cells[6] + cells[4] + cells[2] != '___':
        who(cells[6] + cells[4] + cells[2])


# winner confirmation
def winconf(owin, xwin):
    global nextmove
    global ended
    global os
    global xs
    ended = True
    for i in cells:
        if i == 'O':
            os = os + 1
        elif i == 'X':
            xs = xs + 1
        else:
            ended = False

    if owin == 1 and xwin == 0:
        ended = True
        print('O wins')
    elif xwin == 1 and owin == 0:
        ended = True
        print('X wins')
    elif not impossible:  # if not impossible and not yet ended will ask to make a move
        if not ended:
            pass
    if ended and owin == 0 and xwin == 0:
        print("Draw")


nextmove = input("Enter the coordinates: ").split()
while not hasnumbers(nextmove):
    print('You should enter numbers!')
    nextmove = input("Enter the coordinates:").split()

while not ended:
    nextmove = input("Enter the coordinates:").split()
    if count % 2 == 0:
        move(nextmove[0], nextmove[1], "X")
        gamestate(cells)
        winconf(owin, xwin)
    else:
        move(nextmove[0], nextmove[1], "O")
        gamestate(cells)
        winconf(owin, xwin)
