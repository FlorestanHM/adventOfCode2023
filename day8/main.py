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


def main():
    instructions = get_instructions()
    dic = get_map()
    current = 'AAA'
    steps = 0
    while current != 'ZZZ':
        current = dic[current][instructions[steps % len(instructions)]]
        steps += 1
    print(steps)


if __name__ == '__main__':
    main()
