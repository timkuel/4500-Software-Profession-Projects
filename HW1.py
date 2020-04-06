""" Author:     Timothy Kuelker
    Date:       August 23, 2019
    Course:     CMPSCI 4500
    Description:This program reads "game" information from a file named HW1infile.txt and generates a game board
                from the provided information.  The program will start in the first circle, and then
                will randomly choose between the links created outward to travel around the diGraph game board.
                The program will finish running when all the circles have been visited at least one time.
                All information obtained during the run of this program, from success to failures, will be stored
                in the file HW1kuelkerOutfile.txt.

    Data Structures:For this program, a dictionary of sets was used to hold all the data.  The dictionary reference
                    would be the current circle (head circle) , and the corresponding set of numbers will be what
                    can be traveled to from that circle (tail circle).

    File Format:The file HW1infile.txt should be formatted in a specific manor.  The first line, N, will be the number
                of circles wanting to generate for the game, the second line, K, will be the number of pairs between
                the circles.  The next K lines will be the pairs themselves, each pair needs to be separated by a space.
                """

import random
from collections import defaultdict


# This function writes all the error messaging to the output file.
def outfile_failed_write(error):
    with open("HW1kuelkerOutfile.txt", "w") as out_file:
        out_file.write("It appears a(n) " + error + " occurred, check below for more information.\n\n"
                       "FileFormatError:  This error occurs when HW1infile.txt is not in the proper format.\n"
                       "Be sure that the files first line is N - the number of nodes in this game (between 1 and 10 "
                       "inclusive),\nK - The number of edges between nodes, and the next K-lines will be the actual "
                       "connections between the nodes.\nThe connections must be integers between 1 and N inclusive, "
                       "and in pair format separated by a space.\n\n"
                       "IndexError:  This error occurs when the pairs of connections are not in pair form or the node "
                       "value exceeds\nthe number of nodes.  Be sure in HW1infile.txt that the pairs are on their own "
                       "lines, separated by a space.\nAlso be sure that the node using was actually generated and "
                       "you're not trying to go to a non-existent node.\n\n"
                       "FileNotFoundError:  This error occurs if a file is attempting to be open, and cannot be "
                       "located.\nBe sure that your file is named HW1infile.txt and in the proper root folder.\n"
                       "The file should be put in the same project folder as this project, so it knows where to read "
                       "the file from.\n\n"
                       "ValueError:  This error occurred during the traveling around the diGraph.  The random number\n"
                       "generator generates an node to travel too, but if there is not a node to travel too\n"
                       "(a way out of the current node) it throws that error.  Be sure that each node has at "
                       "least one way out.")

    exit(1)


def traveler_func():
    # Since starting on circle 1, give it a 'check mark' in the counter array at 1's index
    current = 1
    counter[0] = 1

    print("\n\nBeginning to travel around the diGraph, starting in circle 1...")

    while True:
        # Putting the current set of 'goto' options into a variable to access
        goto_set = dict_o_sets[str(current)]

        # Sets are unordered, so the order of the set will not be the same each time generated.
        # To help with randomness, the unordered set is translated to an array.  That
        # array then has a random element in the range of the array length selected from it.
        goto_array = []
        for elements in goto_set:
            goto_array.append(elements)

        try:
            goto = goto_array[random.randint(0, len(goto_array) - 1)]

            # This block can be commented out as it is used to display information.
            print("\nCurrently in circle " + str(current))
            print("Options to travel to are " + str(goto_array))
            print("Traveling to circle " + str(goto) + "\n")

            # This line adds one each time a circle is visited to counter elements
            counter[int(goto) - 1] = counter[int(goto) - 1] + 1
            current = goto
        except ValueError:
            print("\nIt appears a ValueError occurred when trying to choose a random node to travel to.\n"
                  "Check HW1kuelkerOutfile.txt for more information.")
            outfile_failed_write("ValueError")

        except IndexError:
            print("\nIt appears an Index error occured when trying to travel around the diGraph.\n"
                  "Check HW1kuelkerOutfile.txt for more information.")
            outfile_failed_write("IndexError")

        # If the counter array contains all non-zero numbers, then all of the
        # circles/nodes have been visited and return out of function. Method taken from link below
        # https://stackoverflow.com/questions/3525953/check-if-all-values-of-iterable-are-zero
        if all([values != 0 for values in counter]):
            j = 0
            circles = [0] * int(N)
            while j < int(N):
                circles[j] = j + 1
                j += 1

            # This block is commented out as it is used to display information.
            print("\nAll circles visited one time!\nCircle Numbers:\t\t" + str(circles) +
                  "\nNumber Times Visited:\t" + str(counter))
            return


def outfile_passed_write():
    # Writing all the information gathered through this program to HW1kuelkerOutfile.txt.
    # File automatically closes using 'with' statement
    with open("HW1kuelkerOutfile.txt", "w") as out_file:
        out_file.write("The total number of circles generated for this game was " + N +
                       "\nThe total number of arrows used to generate the diGraph for this game was " + K +
                       "\nThe total number of times all circles were visited in this game was " + str(total_visits) +
                       "\nThe average number of times each circle was visited is " + str(average_visits))

        if len(temp_array) == 1:
            out_file.write("\nThe most visited circle was " + str(temp_array) +
                           " with a total visit count of " + str(most_visits))
        else:
            out_file.write("\nThe most visited circles are " + str(temp_array) +
                           " with a total visit count of " + str(most_visits))


# This try block will attempt to open HW1infile.txt and do some work with it.
try:
    # One line code to give number of lines in file taken from below. Subtract 2 for match with K for error checking.
    # https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python
    with open("HW1infile.txt") as file:
        file_length = sum(1 for line in file) - 2
    # and second line (Number of links/arrows between circles/nodes) in 'K'.
    with open("HW1infile.txt", "r") as in_file:
        N = in_file.readline().rstrip()

        K = in_file.readline().rstrip()

        if len(N) == 0 or len(N) > 2 or int(N) not in range(2, 11) or not K.isdigit() or int(K) != file_length:
            in_file.close()
            print("\nIt appears an FileFormatError occurred when attempting to read from HW1infile.txt.\n"
                  "Check HW1kuelkerOutfile.txt for more information.")
            outfile_failed_write("FileFormatError")

        # Creating a dictionary of sets to create graph from.  I used the website below as a reference for this
        # https://www.w3schools.com/python/default.asp
        dict_o_sets = defaultdict(set)

        i = 1
        counter = [0] * int(N)
        strong_check = [0] * int(N)

        # Generating 'N' circles/nodes
        while i < int(N):
            dict_o_sets[str(i)] = set()
            i += 1

        # Catches error where an integer is not used as a pair
        try:
            # Splitting HW1infile.txt pairs so that they cane accessed
            pair_list = [[int(x) for x in line.split()] for line in in_file]
        except ValueError:
            print("\nIt appears a FileFormatError/ValueError occurred.  Be sure pairs are integers.\n"
                  "Check HW1kuelkerOutfile.txt for more information.")
            outfile_failed_write("FileFormatError/ValueError")

        for pairs in pair_list:

            # This try block check to make sure HW1infile.txt is providing pairs
            try:
                start = str(pairs[0])
                end = str(pairs[1])
            except IndexError:
                print("\nIt appears an FileFormatError/IndexError occurred when creating the sets."
                      "\nCheck HW1kuelkerOutfile.txt for more information.")
                outfile_failed_write("IndexError")
            else:
                if int(end) > int(N):
                    print("\nIt appears an FileFormatError/IndexError occurred when trying to place a tail node.  "
                          "Tail node may not exist.\nCheck HW1kuelkerOutfile.txt for more information.")
                    outfile_failed_write("IndexError")

                strong_check[int(end) - 1] = 1
                this_set = set()
                this_set.add(end)
                dict_o_sets[start] |= this_set
except FileNotFoundError:
    print("\nIt appears an FileNotFoundError occurred when trying to read from from a file."
          "\nCheck HW1kuelkerOutfile.txt for more information.")
    outfile_failed_write("FileNotFoundError")


if 0 in strong_check:
    print("\nIt appears a FileFormatError occurred."
          "\nCheck HW1kuelkerOutfile.txt for more information.")
    outfile_failed_write("FileFormatError")


# Making the diGraph output a little more clean (this block is commented out as it is used to display information.)
diGraph = str(dict_o_sets).replace('defaultdict(<class \'set\'>, {', '[').replace('})', ']')

print("\nGenerating a diGraph with " + N + " circles and " + K + " links!")
print("\nThe following is a representation of how to read the generated diGraph, and the generated diGraph itself.")
print("\n['Head Node': {'Tail Node', 'Tail Node', ... }, ... ]")
print(diGraph + "\n")

traveler_func()

# Making the diGraph output a little more clean (this block is commented out as it is used to display information.)
diGraph = str(dict_o_sets).replace('defaultdict(<class \'set\'>, {', '[').replace('})', ']')

print("\n\nTERMINATING PROGRAM, all information will be stored to HW1kuelkerOutfile.txt")

# Total number times each circle is visited is the total number of visits in each spot added up.
total_visits = 0
for visits in counter:
    total_visits = total_visits + visits

# Calculating the most visited square(s) total number of visits
most_visits = 0
for visits in counter:
    most_visits = max(most_visits, visits)

# Using most_visits above, calculating the circle(s)/node(s) that were visited the most
temp_array = []
index_counter = 0
for visits in counter:
    if visits == most_visits:
        temp_array.append(index_counter + 1)
    index_counter += 1

average_visits = total_visits / int(N)

outfile_passed_write()
