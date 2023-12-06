INPUT_FILE = 'input.txt'

def get_lines():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()
    return data

def get_data():
    lines = get_lines()
    line0 = lines[0].split()
    line1 = lines[1].split()

    data = [[line0[i], line1[i]] for i in range(0, len(line0))][1:]

    return [''.join([course[0] for course in data]), ''.join([course[1] for course in data])]


def main():
    course = get_data()
    duree_course = int(course[0])
    distance_battre = int(course[1])

    nombre_possibilite = 0
    for i in range(0, duree_course + 1):
        distance_parcouru = (duree_course - i)  * i
        if distance_parcouru > distance_battre:
            nombre_possibilite += 1

    print(nombre_possibilite)




if __name__ == '__main__':
    main()