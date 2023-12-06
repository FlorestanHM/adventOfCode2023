INPUT_FILE = 'input.txt'

def get_lines():
    with open(INPUT_FILE) as f:
        data = f.read().splitlines()
    return data

def get_data():
    lines = get_lines()
    line0 = lines[0].split()
    line1 = lines[1].split()

    data = [[line0[i], line1[i]] for i in range(0, len(line0))]
    return data[1:]


def main():
    courses = get_data()
    mult = 1
    for course in courses:
        duree_course = int(course[0])
        distance_battre = int(course[1])

        nombre_possibilite = 0
        for i in range(0, duree_course + 1):
            distance_parcouru = (duree_course - i)  * i
            if distance_parcouru > distance_battre:
                nombre_possibilite += 1
        mult *= nombre_possibilite
    print(mult)




if __name__ == '__main__':
    main()