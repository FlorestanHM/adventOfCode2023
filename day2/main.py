INPUT = 'input.txt'


def get_game_id(line):
    return int(line.split(':')[0].split(' ')[1])


def get_manches(line):
    manches_text = line.split(':')[1]
    tab = manches_text.split(';')
    manches = []
    for manche_text in tab:
        manche = {}
        for tirage in manche_text.split(','):
            tirage = tirage.strip()
            manche[tirage.split(' ')[1]] = int(tirage.split(' ')[0])
        manches.append(manche)
    return manches


def is_possible(manches, sac):
    for manche in manches:
        for color, nb in manche.items():
            if sac[color] < nb:
                return False
    return True


def get_minimum(game, colors):
    # for each color, get the minimum number of balls to draw
    minimum = {}
    for color in colors:
        min = 0
        for manche in game:
            if color in manche:
                if manche[color] > min:
                    min = manche[color]
        minimum[color] = min
    return minimum


def mult_colors(minimum, colors):
    mult = 1
    for color in colors:
        mult *= minimum[color]
    return mult


def main():
    # Open the file input.txt and iterate over each line
    sum_game_possible = 0
    sum_required = 0
    with open(INPUT) as file:
        for line in file:
            gameId = get_game_id(line)
            game = get_manches(line)
            sac = {'red': 12, 'green': 13, 'blue': 14}
            if is_possible(game, sac):
                print('Game ' + str(gameId) + ': possible')
                sum_game_possible += gameId
            colors = {'blue', 'red', 'green'}
            minimum = get_minimum(game, colors)
            sum_required += mult_colors(minimum, colors)
    print('sum_game_possible: ' + str(sum_game_possible))
    print('sum_required: ' + str(sum_required))


if __name__ == '__main__':
    main()
