def print_field():
    print("---------")
    print("|", cells[0], cells[1], cells[2], "|")
    print("|", cells[3], cells[4], cells[5], "|")
    print("|", cells[6], cells[7], cells[8], "|")
    print("---------")

def three_in_row():
    l = []
    field = [list(cells[0:3]), list(cells[3:6]), list(cells[6:9])]
    for letter in ['X', 'O']:
        for x in range(3):
            if field[x][0] == field[x][1] == field[x][2] == letter:
                l.append(letter)
                break
        for x in range(3):
            if field[0][x] == field[1][x] == field[2][x] == letter:
                l.append(letter)
                break
        if field[0][0] == field[1][1] == field[2][2] == letter or field[0][2] == field[1][1] == field[2][0] == letter:
            l.append(letter)
    if len(l) == 0:
        return 'F'
    elif 'X' in l and 'O' in l:
        return 'I'  # Impossible
    else:
        return l[0]

cells = list(" " * 9)
right = False
finish = False
i = 0
print_field()
while not finish:
    right = False
    while not right:
        coordinates = list(input("Enter the coordinates:").split())
        if len(coordinates) != 2 or not all([x.isdigit() for x in coordinates]):
            print("You should enter numbers!")
        elif any([int(x) not in range(1, 4) for x in coordinates]):
            print("Coordinates should be from 1 to 3!")
        else:
            coordinates = [int(x) for x in coordinates]
            x = 3 * (coordinates[0] - 1) + coordinates[1] - 1
            if cells[x] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                cells[x] = "X" if i % 2 == 0 else "O"
                i += 1
                right = True
    print_field()
    res = three_in_row()
    if res in ['X', 'O']:
        print(f"{res} wins")
        finish = True
    elif res == 'F' and " " not in cells:
        print("Draw")
        finish = True