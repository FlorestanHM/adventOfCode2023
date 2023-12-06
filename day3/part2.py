INPUT = 'input.txt'


# Retourne le tableau de caractères à partir d'un fichier
def get_table(file):
    table = []
    for line in file:
        line = line.rstrip('\n')
        table.append([char for char in line])
    return table


# Retourne les deux nombres adjacents à cette coordonnée
def get_adjacent_numbers(table, y, x):
    adjacent_numbers = set()
    visited = set()

    def dfs(row, col, number):
        if (row, col) in visited:
            return
        visited.add((row, col))
        if table[row][col].isdigit():
            number.append([table[row][col], col])
            for c in range(col - 1, col + 2):
                if 0 <= row < len(table) and 0 <= c < len(table[row]):
                    dfs(row, c, number)

    for j in [y - 1, y, y + 1]:
        for i in [x - 1, x, x + 1]:
            if 0 <= j < len(table) and 0 <= i < len(table[j]):
                if table[j][i].isdigit():
                    num = []
                    dfs(j, i, num)
                    if len(num) > 0:
                        num.sort(key=lambda x: x[1])
                        adjacent_numbers.add(int(''.join(num[i][0] for i in range(len(num)))))

    return list(adjacent_numbers)


def main():
    with open(INPUT) as file:
        table = get_table(file)
        total_gear_ratios = 0
        for y in range(len(table)):
            for x in range(len(table[y])):
                if table[y][x] == '*':
                    adjacent_numbers = get_adjacent_numbers(table, y, x)
                    print(adjacent_numbers)
                    if len(adjacent_numbers) == 2:
                        total_gear_ratios += adjacent_numbers[0] * adjacent_numbers[1]

        print('Total gear ratios:', total_gear_ratios)


if __name__ == '__main__':
    main()
