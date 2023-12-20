import sys

INPUT_FILE = 'temp2.txt'


def get_grid():
    return [[char for char in line.strip()] for line in open(INPUT_FILE).readlines()]


def pretty_print(grid):
    for line in grid:
        print(line)


def transform_s(grid, x, y):
    # Check N, S, E, W
    possible = []
    symbol = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['N', 'E'], 'J': ['N', 'W'], '7': ['S', 'W'], 'F': ['S', 'E']}
    if x - 1 >= 0 and grid[x - 1][y] in symbol and 'S' in symbol[grid[x - 1][y]]:
        possible.append('N')
    if x + 1 < len(grid) and grid[x + 1][y] in symbol and 'N' in symbol[grid[x + 1][y]]:
        possible.append('S')
    if y - 1 >= 0 and grid[x][y - 1] in symbol and 'E' in symbol[grid[x][y - 1]]:
        possible.append('W')
    if y + 1 < len(grid[0]) and grid[x][y + 1] in symbol and 'W' in symbol[grid[x][y + 1]]:
        possible.append('E')
    # Trouver le symbole qui a pour direction possible ceux dans possible
    for key, value in symbol.items():
        if value == possible:
            grid[x][y] = key




def explore(grid, new_grid, x, y, last_value):
    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.

    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == '.':
        return
    # Si ça commence par un X, on a déjà visité
    else:
        if new_grid[x][y] != '.' and last_value > int(new_grid[x][y]):
            return
        else:
            new_grid[x][y] = last_value
        current = grid[x][y]
        if current == '|':
            explore(grid, new_grid, x - 1, y, last_value + 1)  # nord
            explore(grid, new_grid, x + 1, y, last_value + 1)  # sud
        elif current == '-':
            explore(grid, new_grid, x, y + 1, last_value + 1)  # est
            explore(grid, new_grid, x, y - 1, last_value + 1)  # ouest
        elif current == 'L':
            explore(grid, new_grid, x - 1, y, last_value + 1)  # nord
            explore(grid, new_grid, x, y + 1, last_value + 1)  # est
        elif current == 'J':
            explore(grid, new_grid, x, y - 1, last_value + 1)  # ouest
            explore(grid, new_grid, x - 1, y, last_value + 1)  # nord
        elif current == '7':
            explore(grid, new_grid, x, y - 1, last_value + 1)  # ouest
            explore(grid, new_grid, x + 1, y, last_value + 1)  # sud
        elif current == 'F':
            explore(grid, new_grid, x + 1, y, last_value + 1)  # sud
            explore(grid, new_grid, x, y + 1, last_value + 1)  # est


def find_max(grid):
    max_value = 0
    for line in grid:
        for value in line:
            if value != '.' and value > max_value:
                max_value = value
    print(max_value)


def is_oppose_in(direction, list_direction):
    if direction == 'N':
        return 'S' in list_direction
    elif direction == 'S':
        return 'N' in list_direction
    elif direction == 'E':
        return 'W' in list_direction
    elif direction == 'W':
        return 'E' in list_direction


def remove_useless_at(grid, i, j):
    if grid[i][j] == '.':
        return False
    symbol = {'|': ['N', 'S'], '-': ['E', 'W'], 'L': ['N', 'E'], 'J': ['N', 'W'], '7': ['S', 'W'],
              'F': ['S', 'E']}
    direction = {'N': [-1, 0], 'S': [1, 0], 'E': [0, 1], 'W': [0, -1]}
    current_directions = symbol[grid[i][j]]
    for current_direction in current_directions:
        ajout_coord = direction[current_direction]
        if (i + ajout_coord[0] < 0 or len(grid) <= i + ajout_coord[0]
                or j + ajout_coord[1] < 0 or  len(grid[i + ajout_coord[0]]) <= j + ajout_coord[1]
                or grid[i + ajout_coord[0]][j + ajout_coord[1]] == '.'
                or not is_oppose_in(current_direction, symbol[grid[i + ajout_coord[0]][j + ajout_coord[1]]])):
            grid[i][j] = '.'
            return True


def remove_useless(grid):
    change = True
    while change:
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                 change = change or remove_useless_at(grid, i, j)


def convert_file():
    # Open the file in read mode and read lines
    with open('temp.txt', 'r') as file:
        lines = file.readlines()

    # Process lines to remove unwanted characters
    processed_lines = []
    for line in lines:
        tab = eval(line.strip())
        for i in range(len(tab)):
            if str(tab[i]).isdigit():
                tab[i] = 'X'
        processed_lines.append(''.join(tab) + '\n')

    # Open the file in write mode and write processed lines
    with open('temp2.txt', 'w') as file:
        file.writelines(processed_lines)

    print(processed_lines)

# Retourne si on trouve bien au moins element au nord, sud, est et ouest de i, j
def checkIfEnclose(grid, i, j):
    directions = {'N': [-1, 0], 'S': [1, 0], 'E': [0, 1], 'W': [0, -1]}
    dic = {}
    for key, direction in directions.items():
        distance = 1
        while 0 <= i + direction[0] * distance < len(grid) and 0 <= j + direction[1] * distance < len(grid[0]):
            if grid[i + direction[0] * distance][j + direction[1] * distance] != '.':
                dic[key] = True
            distance += 1
    if len(dic) == 4:
        grid[i][j] = 'X'


def grid_to_file(grid):
    processed_lines = [''.join(line) + '\n' for line in grid]

    # Open the file in write mode and write processed lines
    with open('temp2.txt', 'w') as file:
        file.writelines(processed_lines)

    print(processed_lines)


def main():
    grid = get_grid()
    print('-------------------')

    change = True
    while change:
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Si c'est un .
                if grid[i][j] == 'X':
                    # regarder si il est adjacent à un .
                    if i - 1 >= 0 and grid[i - 1][j] == '.': # nord
                        grid[i][j] = '.'
                        change = True
                    elif i + 1 < len(grid) and grid[i + 1][j] == '.': # sud
                        grid[i][j] = '.'
                        change = True
                    elif j - 1 >= 0 and grid[i][j - 1] == '.': # ouest
                        grid[i][j] = '.'
                        change = True
                    elif j + 1 < len(grid[0]) and grid[i][j + 1] == '.': # est
                        grid[i][j] = '.'
                        change = True
                else:
                    continue

    grid_to_file(grid)


if __name__ == '__main__':
    main()