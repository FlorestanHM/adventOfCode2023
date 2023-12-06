def main():
    # Open the file input.txt and iterate over each line
    sum = 0
    with open('input.txt') as f:
        for line in f:
            # transform digits written in letters to digits
            digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
            for digit in digits:
                line = line.replace(digit, digit + str(digits.index(digit)) + digit)
            resultLine = []
            for car in line:
                # If the car is a number, add it to the resultLine
                if car.isdigit():
                    resultLine.append(car)
            if len(resultLine) >= 2:
                # If the line has at least 2 numbers, add the sum of the numbers to the sum
                print("" + resultLine[0] + resultLine[len(resultLine) - 1])
                sum += int("" + resultLine[0] + resultLine[len(resultLine) - 1])
            else:
                print("" + resultLine[0] + resultLine[0])
                sum += int("" + resultLine[0] + resultLine[0])
            print(line)
    print(sum)


if __name__ == '__main__':
    main()