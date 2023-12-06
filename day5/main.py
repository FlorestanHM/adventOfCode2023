INPUT_FILE = 'input.txt'


def get_data():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()

    seeds = data[0].split(' ')
    seeds_number = []
    for i in range(0, len(seeds)):
        seed = seeds[i]
        if seed.isdigit():
            if i % 2 == 0:
                length = int(seed)
                seeds_number.append([start, length])
            else:
                start = int(seed)

    maps = []
    currentMap = []
    for i in range(2, len(data)):
        line = data[i]
        if line == '':
            maps.append(currentMap)
            currentMap = []
            continue
        if line[0].isdigit():  # ligne décrivant une map
            line = line.split(' ')
            currentMap.append([int(line[0]), int(line[1]), int(line[2])])
    maps.append(currentMap)

    return maps, seeds_number


def transform(value, tab):
    ecart = value - tab[1]
    return tab[0] + ecart


def intersection(values_range, tabs):
    new_values_range = []
    for value_range in values_range:
        new_values_range.append(value_range)
        for tab in tabs:
            debut_interval = value_range[0]  # debut de l'interval à tester
            longueur_interval = value_range[1]  # longueur de l'interval à tester
            fin_interval = debut_interval + longueur_interval  # fin de l'interval à tester

            debut_transform = tab[1]  # debut de l'interval de la map
            fin_transform = tab[1] + tab[2]  # fin de l'interval de la map

            # L'interval est complètement en dehors de l'interval de la map
            if fin_interval <= debut_transform or debut_interval >= fin_transform:
                continue
            # Tout l'interval est contenu dans l'interval de la map
            if debut_transform <= debut_interval and fin_interval <= fin_transform:
                new_values_range.pop()
                new_values_range.append([transform(debut_interval, tab), longueur_interval])
                break
            # L'interval commence avant l'interval de la map et se termine dedans
            if debut_interval <= debut_transform and fin_interval <= fin_transform:
                longueur_avant = debut_transform - debut_interval
                new_values_range.pop()
                values_range.append([debut_interval, longueur_avant])
                new_values_range.append([transform(debut_transform, tab), longueur_interval - longueur_avant])
                break
            # L'interval commence dedans et se termine après
            if debut_transform <= debut_interval and fin_transform <= fin_interval:
                longueur_apres = fin_interval - fin_transform
                new_values_range.pop()
                new_values_range.append([transform(debut_interval, tab), longueur_interval - longueur_apres])
                values_range.append([fin_transform, longueur_apres])
                break
            # L'interval est plus grand que l'interval de la map
            if debut_interval <= debut_transform and fin_transform <= fin_interval:
                new_values_range.pop()
                longueur_avant = debut_transform - debut_interval
                longueur_apres = fin_interval - fin_transform
                values_range.append([debut_interval, longueur_avant])
                new_values_range.append(
                    [transform(debut_transform, tab), longueur_interval - longueur_avant - longueur_apres])
                values_range.append([fin_transform, longueur_apres])
                break
    return new_values_range


def main():
    maps, seeds_range = get_data()

    values_range = seeds_range
    for tabs in maps:
        values_range = intersection(values_range, tabs)

    min = 0
    for value_range in values_range:
        if value_range[0] < min or min == 0:
            min = value_range[0]

    print(min)


if __name__ == '__main__':
    main()
