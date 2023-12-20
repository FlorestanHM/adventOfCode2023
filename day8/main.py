INPUT_FILE = 'input.txt'


def get_instructions():
    transformation = {'L': 0, 'R': 1}
    # return the first line of INPUT_FILE
    with open(INPUT_FILE) as f:
        first = f.readline()
        first = first.strip('\n')
        suite = [transformation[i] for i in first]
        return suite


def get_map():
    dic = {}
    # for each line from 3rd line of INPUT_FILE
    for line in open(INPUT_FILE).readlines()[2:]:
        dic[line[0:3]] = [line[7:10], line[12:15]]
    return dic


def end(currents):
    for current in currents:
        if current[2] != 'Z':
            return False
    return True


def get_longueur_cycle(dic, starts, instructions):
    longeurs = []
    for start in starts:
        steps = 0
        current = start
        while current[2] != 'Z':
            current = dic[current][instructions[steps % len(instructions)]]
            steps += 1
        longeurs.append(steps)
    return longeurs


def ppcm(longeurs):
    ppcm = longeurs[0]
    for i in longeurs[1:]:
        ppcm = ppcm * i // pgcd(ppcm, i)
    return ppcm


def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def main():
    instructions = get_instructions()
    dic = get_map()
    starts = [key for key in dic.keys() if key[2] == 'A']
    longueur = get_longueur_cycle(dic, starts, instructions)
    print(ppcm(longueur))


if __name__ == '__main__':
    main()
