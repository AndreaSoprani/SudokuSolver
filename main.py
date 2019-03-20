from solver import *
import time

if __name__ == "__main__":

    sudokus = open("sudokus.txt", "r")
    output = open("solutions.txt", "w")
    lines = sudokus.read().splitlines()

    print("{} sudokus loaded.".format(len(lines)))

    counter = 0
    total_time = 0

    for line in lines:

        line.strip()

        ignore = False

        if len(line) != 81:
            ignore = True

        for x in line:
            if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                ignore = True
                break

        if ignore:
            continue

        counter += 1

        start_time = time.time()

        solved = solve(line)

        solved_time = time.time() - start_time

        total_time += solved_time

        print("sudoku {} solved in {}".format(counter, solved_time))

        output.write("sudoku {} solved in {}\n\n".format(counter, solved_time))

        quiz = Grid()
        quiz.set_initial_values(string_to_int_list(line))

        output.write("{}\n".format(str(quiz)))
        output.write("{}\n".format(str(solved)))

    print("{} sudokus solved in {}".format(counter, total_time))
    output.write("{} sudokus solved in {}\n".format(counter, total_time))

    if counter != 0:
        average = total_time / counter
        print("average time: {}".format(average))
        output.write("average time: {}\n".format(average))
