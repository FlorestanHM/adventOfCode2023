INPUT_FILE = 'input.txt'

def get_data():
    # return in a list of list of string
    return [[int(elem) for elem in line.split()] for line in open(INPUT_FILE).readlines()]

def get_pyramide(data):
    data.reverse()
    pyramide = [data]
    current = data
    # tant que tout les elements de current ne sont pas == 0
    while not all(elem == 0 for elem in current):
        new = []
        # new[i] = current[i+1] - current[i]
        for i in range(len(current)-1):
            new.append(current[i+1] - current[i])
        pyramide.append(new)
        current = new
    return pyramide

def main():
    data_tab = get_data()
    sum = 0
    for data in data_tab:
        pyramide = get_pyramide(data)
        # En parcourant le pyramide de bas en haut
        pyramide[len(pyramide)-1].append(0)
        for i in range(len(pyramide)-2, -1, -1):
            pyramide[i].append(pyramide[i+1][len(pyramide[i+1])-1] + pyramide[i][len(pyramide[i])-1])
        sum += pyramide[0][len(pyramide[0])-1]
    print(sum)


if __name__ == '__main__':
    main()
