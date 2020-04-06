""" Author:     Timothy Kuelker
    Date:       September 5, 2019
    Course:     CMPSCI 4500
    Description:This program reads "game" information from a file named HW2infile.txt and generates a game board
                from the provided information.  The program will start in the first circle, and then
                will randomly choose between the links created outward to travel around the diGraph game board.
                The program will finish running when all the circles have been visited at least one time.
                The program will run this game for a total of 10 times.
                All information obtained during the run of this program, from success to failures, will be stored
                in the file HW2kuelkerOutfile.txt.

    Data Structures:For this program, a dictionary of lists was used to hold all the data.  The dictionary reference
                    would be the current circle (head circle) , and the corresponding list of numbers will be what
                    can be traveled to from that circle (tail circle).

    File Format:The file HW2infile.txt should be formatted in a specific manor.  The first line, N, will be the number
                of circles wanting to generate for the game, the second line, K, will be the number of pairs between
                the circles.  The next K lines will be the pairs themselves, each pair needs to be separated by a space.
                """

import random
from collections import defaultdict


# This function writes all the error messaging to the output file.
def outfile_failed_write(error):
    in_file.close()
    with open("HW2kuelkerOutfile.txt", "w") as out_file:
        out_file.write("It appears a(n) " + error + " occurred, check below for more information.\n\n"
                       "FileFormatError:  This error occurs when HW2infile.txt is not in the proper format.\n"
                       "Be sure that the files first line is N - the number of nodes in this game (between 1 and 10 "
                       "inclusive),\nK - The number of edges between nodes, and the next K-lines will be the actual "
                       "connections between the nodes.\nThe connections must be integers between 1 and N inclusive, "
                       "and in pair format separated by a space.\n\n"
                       "IndexError:  This error occurs when the pairs of connections are not in pair form or the node "
                       "value exceeds\nthe number of nodes.  Be sure in HW2infile.txt that the pairs are on their own "
                       "lines, separated by a space.\nAlso be sure that the node using was actually generated and "
                       "you're not trying to go to a non-existent node.\n\n"
                       "FileNotFoundError:  This error occurs if a file is attempting to be open, and cannot be "
                       "located.\nBe sure that your file is named HW2infile.txt and in the proper root folder.\n"
                       "The file should be put in the same project folder as this project, so it knows where to read "
                       "the file from.\n\n"
                       "ValueError:  This error occurred during the traveling around the diGraph.  The random number\n"
                       "generator generates an node to travel too, but if there is not a node to travel too\n"
                       "(a way out of the current node) it throws that error.  Be sure that each node has at "
                       "least one way out.\n\n"
                       "WeakGraphError:  This error occurred when the generated graph is not a strong graph.  "
                       "Be sure that\neach circle has an arrow pointing to it and an arrow pointing away from it.\n"
                       "All circles must be visitable from any other circle.")

    exit(1)


# Clears the outfile so that things can be appended
def clear_out_file():
    with open("HW2kuelkerOutfile.txt", "w") as out_file:
        print("Clearing outfile for new game!\n")


# Performs a breadth first search, returns all visited nodes as a list
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                queue.append(neighbor)

    return visited


def check_strength():
    strong_check = [0] * int(N)
    m = 1
    while m <= int(N):
        # strong_check gets set equal to the returned 'visited' list
        strong_check[(m - 1)] = bfs(dict_o_lists, m)

        m += 1

    n = 0
    while n < int(N):
        # if any of the lengths of the sub lists don't match the number of nodes,
        # there is a weak graph.
        if len(strong_check[n]) < int(N):
            print("\nIt appears a WeakGraphError occurred.  Be sure each node can be visited from any other node.\n"
                  "Check HW2kuelkerOutfile.txt for more information.")
            outfile_failed_write("WeakGraphError")
        n += 1


def builder_func():
    k = 1
    # Generating 'N' circles/nodes
    while k < int(N):
        dict_o_lists[k] = list()
        k += 1

    # Catches error where an integer is not used as a pair
    try:
        # Splitting HW2infile.txt pairs so that they cane accessed
        pair_list = [[int(x) for x in line.split()] for line in in_file]
    except ValueError:
        print("\nIt appears a FileFormatError/ValueError occurred.  Be sure pairs are integers.\n"
              "Check HW2kuelkerOutfile.txt for more information.")
        outfile_failed_write("FileFormatError/ValueError")
    else:
        for pairs in pair_list:

            # This try block check to make sure HW2infile.txt is providing pairs
            try:
                start = pairs[0]
                end = pairs[1]
            except IndexError:
                print("\nIt appears an FileFormatError/IndexError occurred when creating the lists."
                      "\nCheck HW2kuelkerOutfile.txt for more information.")
                outfile_failed_write("IndexError/FileFormatError")
            else:
                if end > int(N):
                    print("\nIt appears an FileFormatError/IndexError occurred when trying to place a "
                          "tail node.  Tail node may not exist.\nCheck HW2kuelkerOutfile.txt for more information.")
                    outfile_failed_write("FileFormatError/IndexError")

                dict_o_lists[start].append(end)

        check_strength()


def traveler_func():
    # Since starting on circle 1, give it a 'check mark' in the counter array at 1's index
    current = 1
    check_counter[0] = 1

    while True:
        # Putting the current list of 'goto' options into a variable to access
        goto_list = dict_o_lists[current]

        goto_array = []
        for elements in goto_list:
            goto_array.append(elements)

        try:
            goto = goto_array[random.randint(0, len(goto_array) - 1)]

            # This line adds one each time a circle is visited to counter elements
            check_counter[goto - 1] = check_counter[goto - 1] + 1
            current = goto
        except ValueError:
            print("\nIt appears a ValueError occurred when choosing a random node to travel to.\n"
                  "Check HW2kuelkerOutfile.txt for more information.")
            outfile_failed_write("ValueError")

        except IndexError:
            print("\nIt appears an IndexError occurred when trying to travel around the diGraph.\n"
                  "Check HW2kuelkerOutfile.txt for more information.")
            outfile_failed_write("IndexError")

        if sum(check_counter) >= 1000000:
            print("\nA single game exceeded one million checks, TERMINATING PROGRAM!\n")
            exit(1)

        # If the counter array contains all non-zero numbers, then all of the
        # circles/nodes have been visited and return out of function. Method taken from link below
        # https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
        if all([values != 0 for values in check_counter]):
            return


def outfile_write_per_game():
    # Writing all the information gathered through this program to HW2kuelkerOutfile.txt.
    # File automatically closes using 'with' statement
    with open("HW2kuelkerOutfile.txt", "a") as out_file:
        out_file.write("\tGame " + str(simulation_runner + 1) + " statistics!" +
                       "\nThe total number of circles generated for this game was " + N +
                       "\nThe total number of arrows used to generate the diGraph for this game was " + K +
                       "\nThe total number of times all circles were visited in this game was " + str(total_visits) +
                       "\nThe average number of times each circle was visited is " + str(average_visits))

        if len(temp_array) == 1:
            out_file.write("\nThe most visited circle was " + str(temp_array) +
                           " with a total visit count of " + str(most_visits) + "\n\n")
        else:
            out_file.write("\nThe most visited circles are " + str(temp_array) +
                           " with a total visit count of " + str(most_visits) + "\n\n")


def outfile_write_all_games():
    # Writing all the information gathered through this program to HW2kuelkerOutfile.txt.
    # File automatically closes using 'with' statement
    with open("HW2kuelkerOutfile.txt", "a") as out_file:
        out_file.write("\n\n\tStatistics of all Games!\nThe average number of total checks per game was " + str(all_time_checks/simulation_runner) +
                       "\nThe maximum number of total checks in a single game was " + str(max_checks_simulation) +
                       "\nThe minimum number of total checks in a single game was " + str(min_checks_simulation))

        loop = 0
        while loop < int(N):
            avg_checks_per_circle[loop] = (avg_checks_per_circle[loop] / 10)
            out_file.write("\nCircle " + str(loop + 1) + " was visited on average " +
                           str(avg_checks_per_circle[loop]) + " time(s).")
            loop += 1

        out_file.write("\nThe minimum number of single circle checks was " + str(min_single_circle) +
                       "\nThe maximum number of single circle checks was " + str(max_single_circle))


# This try block will attempt to open HW2infile.txt and read data from it.
try:
    # One line code to give number of lines in file taken from below. Subtract 2 for match with K for error checking.
    # https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
    with open("HW2infile.txt") as file:
        file_length = sum(1 for line in file) - 2
    with open("HW2infile.txt", "r") as in_file:
        N = in_file.readline().rstrip()

        K = in_file.readline().rstrip()

        if not N.isdigit() or int(N) not in range(2, 21) or not K.isdigit() or int(K) != file_length:
            in_file.close()
            print("\nIt appears an FileFormatError occurred when attempting to read from HW2infile.txt.\n"
                  "Check HW2kuelkerOutfile.txt for more information.")
            outfile_failed_write("FileFormatError")

        # Creating a dictionary of lists to create graph from.  I used the website below as a reference for this
        # https://www.w3schools.com/python/default.asp
        dict_o_lists = defaultdict(list)

        builder_func()

except FileNotFoundError:
    print("\nIt appears an FileNotFoundError occurred when trying to read from from a file."
          "\nCheck HW2kuelkerOutfile.txt for more information.")
    outfile_failed_write("FileNotFoundError")

# Setting simulation counters
simulation_runner = 0
all_time_checks = 0
max_checks_simulation = 0
min_checks_simulation = 1000000
avg_checks_per_circle = [0] * int(N)
min_single_circle = 1000000
max_single_circle = 0

# This list is used to reference the number of times each circle was visited
j = 0
circles = [0] * int(N)
while j < int(N):
    circles[j] = j + 1
    j += 1

# Clearing outfile for new game
clear_out_file()

while simulation_runner < 10:
    # Resetting single game counters
    check_counter = [0] * int(N)
    min_checks_single_game = 1000000
    max_checks_single_game = 0

    print("\nStarting game " + str(simulation_runner + 1))

    traveler_func()

    index = 0
    for i in check_counter:
        avg_checks_per_circle[index] += i
        index += 1

    print("\nAll circles visited one time for game " + str(simulation_runner + 1) + "!\nCircle Numbers:\t\t" +
          str(circles) + "\nNumber Times Visited:\t" + str(check_counter))
    print("Total checks on game " + str(simulation_runner + 1) + " was " + str(sum(check_counter)))
    print("Maximum checks on game " + str(simulation_runner + 1) + " was " + str(max(check_counter)))
    print("Minimum checks on game " + str(simulation_runner + 1) + " was " + str(min(check_counter)) + "\n")

    max_checks_simulation = max(max_checks_simulation, sum(check_counter))
    min_checks_simulation = min(min_checks_simulation, sum(check_counter))
    all_time_checks += sum(check_counter)
    min_single_circle = min(min(check_counter), min_single_circle)
    max_single_circle = max(max(check_counter), max_single_circle)

    # Total number times each circle is visited is the total number of visits in each spot added up.
    total_visits = 0
    for visits in check_counter:
        total_visits = total_visits + visits

    # Calculating the most visited square(s) total number of visits
    most_visits = 0
    for visits in check_counter:
        most_visits = max(most_visits, visits)

    # Using most_visits above, calculating the circle(s)/node(s) that were visited the most
    temp_array = []
    index_counter = 0

    for visits in check_counter:
        if visits == most_visits:
            temp_array.append(index_counter + 1)
        index_counter += 1

    average_visits = total_visits / int(N)

    outfile_write_per_game()

    simulation_runner += 1

print("\n\nTERMINATING PROGRAM, all information will be stored to HW2kuelkerOutfile.txt")

outfile_write_all_games()

