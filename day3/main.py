INPUT = 'input.txt'


# Retourne le tableau de caractères à partir d'un fichier
def get_table(file):
    table = []
    for line in file:
        # filtrer tab pour enlever les caractères \n
        line = line.rstrip('\n')
        table.append([char for char in line])
    return table


# Affiche le tableau
def pretty_print(table):
    index = 0
    for line in table:
        print(index, line)
        index += 1


# Find the next coord in the table
# If the next coord is out of the table, return False
def next_coord(table, coord):
    if coord[1] < len(table[coord[0]]) - 1:
        return [coord[0], coord[1] + 1]
    elif coord[0] != len(table) - 1:
        return [coord[0] + 1, 0]
    else:  # Si on est à la fin du tableau, retourner False
        return False


# Retourne le prochain nombre et la coordonnée de la fin du nombre
def find_number(table, coord):
    if table[coord[0]][coord[1]].isdigit():
        number = int(table[coord[0]][coord[1]])
        for i in range(coord[1] + 1, len(table[coord[0]])):
            if table[coord[0]][i].isdigit():
                number = (number * 10) + int(table[coord[0]][i])
            else:
                return number, [coord[0], coord[1], i-1]
        return number, [coord[0], coord[1], len(table[coord[0]])]
    else:
        return False


# Retourne si il y a un symbole autre que '.' autour de ces coordonnées
def is_something_adjacent(table, y, x1, x2):
    for j in [y - 1, y, y + 1]:
        for i in range(x1-1, x2 + 2):
            if 0 <= j < len(table) and 0 <= i < len(table[j]):
                if not (x1 <= i <= x2 and j == y) and table[j][i] != '.':
                    return True


def main():
    with open(INPUT) as file:
        table = get_table(file)
        pretty_print(table)

        total = 0
        coord = [0, 0]  # Coordonnées du début du tableau
        while coord:  # Tant qu'on a pas fini le tableau
            if find_number(table, coord) is False:
                coord = next_coord(table, coord)
                continue
            number, coord = find_number(table, coord)  # Trouver le prochain nombre
            test = False
            # Si il y a un symbole autour de ce nombre
            if is_something_adjacent(table, coord[0], coord[1], coord[2]):
                total += number
                test = True
            print(number, coord, test)
            coord = next_coord(table, [coord[0], coord[2]])

        print('TOTAL', total)


if __name__ == '__main__':
    main()
