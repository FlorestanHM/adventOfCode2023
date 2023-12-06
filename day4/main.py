INPUT = 'inputTest.txt'


def get_numbers(line):
    card, line = line.strip().split(':')
    card_number = int(card.split()[1])
    numbers = line.split('|')
    winning = [int(i) for i in numbers[0].split(' ') if i.isdigit()]
    yours = [int(i) for i in numbers[1].split(' ') if i.isdigit()]
    return card_number, winning, yours


def get_intersection_len(winning, yours):
    winning = set(winning)
    yours = set(yours)
    intersection = winning.intersection(yours)
    return len(intersection)


def number_of_point(number_of_win):
    if number_of_win == 1:
        return 1
    elif number_of_win == 0:
        return 0
    else:
        return number_of_point(number_of_win - 1) * 2


def main():
    with open(INPUT) as file:
        number_of_cards = {}
        for line in file:
            card_number, winning, yours = get_numbers(line)
            number_of_win = get_intersection_len(winning, yours)
            if number_of_cards.get(card_number) is None:
                number_of_cards[card_number] = 1
            for i in range(card_number + 1, card_number + number_of_win + 1):
                number_of_cards[i] = number_of_cards.get(card_number, 1) + number_of_cards.get(i, 1)
            print(number_of_cards)

        # sum of number of cards
        print(sum(number_of_cards.values()))


if __name__ == '__main__':
    main()
