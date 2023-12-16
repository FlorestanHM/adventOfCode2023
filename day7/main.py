INPUT_FILE = 'input.txt'


def get_data():
    data = []
    for line in open(INPUT_FILE, 'r'):
        data.append(line.split())
    return data


def transform_main(main):
    jeu = {}
    joker = 0
    for car in main:
        if car == 'J':
            joker += 1
        else:
            if car in jeu:
                jeu[car] += 1
            else:
                jeu[car] = 1

    # Joker
    if joker > 0 and joker < 5:
        max = 0
        max_elem = ''
        for elem in jeu:
            if jeu[elem] > max:
                max = jeu[elem]
                max_elem = elem
        if max_elem != '':
            jeu[max_elem] += joker
    elif joker == 5:
        jeu['J'] = 5

    return jeu


def valeur_jeu(main):
    jeu = transform_main(main)
    power = 1
    debut_full = 0
    for elem in jeu:
        if jeu[elem] == 5:
            power = 7 # Etoile
        elif jeu[elem] == 4:
            power = 6 # Carré
        elif jeu[elem] == 3:
            power = 4 # Brelan
            if debut_full == 0:
                debut_full = 3
            elif debut_full == 2:
                power = 5  # Full
        elif jeu[elem] == 2:
            power = 2
            if debut_full == 0:
                debut_full = 2
            elif debut_full == 3:
                power = 5  # Full
            elif debut_full == 2:
                power = 3 # Double paire
    return 10 ** 10 * power + convert_main(main)


def convert_main(main):
    valeur = {'2': 2, '3': 3, '4': 4, '5': 5,
              '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10,
              'J': 0, 'Q': 12, 'K': 13, 'A': 14}
    convert = 0
    index = 4
    for car in main:
        convert += valeur[car] * 10 ** (index * 2)
        index -= 1
    return convert


def calculer_score(jeux):
    somme = 0
    for i in range(len(jeux)):
        somme += (i + 1) * int(jeux[i][1])
    return somme


def main():
    mains = get_data()
    mains.sort(key=lambda x: valeur_jeu(x[0]))
    for main in mains:
        print(main[0], transform_main(main[0]), valeur_jeu(main[0]))
    print(calculer_score(mains))


if __name__ == '__main__':
    main()
