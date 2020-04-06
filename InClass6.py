"""Author:      Timothy Kuelker
    Date:       October 1, 2019
    Course:     CMPSCI 4500
    Description: Program takes a file name from user.  From that file, the program
    will store all the words into a dictionary as keys, if a word is read again, it will
    increment the value of that key.  This will give us the occurrences of each word.
    After it finishes reading the file, it will sort the list by keys, or the words, and
    print that list to WordCounts.txt.  It will then display the top 20 most occurred words,
    if there were any ties for the 20th spot, the one left out will be the one that occurred
    later than the rest it tied with.  There will not be a distinction between the name Will
    and the verb will.  When putting values into the dictionary and comparing them, all words
    are lowercase.  This was more simple to handle then trying to separate a verb will happening
    at the beginning of a sentence being treated the same as the name Will.
"""

import collections
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


def print_graph(dictionary):
    names = []
    values = []

    i = 0
    for k, v in dictionary.items():
        if i == 20:
            break

        names.append(k)
        values.append(v)

        i += 1

    y_pos = np.arange(len(names))

    plt.barh(y_pos, values, align='center', alpha=1.0)
    plt.yticks(y_pos, names)
    plt.xlabel('Number of Occurrences')

    plt.title('Top 20 Word Occurrences')

    plt.show()


def write_dict_to_file(dictionary):
    with open("WordCounts.txt", "w") as out_file:
        for key, value in dictionary.items():
            out_file.write(key + " " + str(value) + "\n")


def main():
    dict_o_ints = defaultdict(int)
    while True:
        try:
            file_name = input("Please enter a name for the file to read from: ")
            f = open(file_name, "r")
        except FileNotFoundError:
            print("\nFile '" + file_name + "' does not exist, please enter an existing file!\n")
        else:
            for line in f:

                # Taking line, moving all words to lower case, replacing '-' with ' ', replacing '.' with '',
                # replacing ',' with '', and finally splitting the line by spaces
                for words in line.lower().replace("-", " ").replace(".", "").replace(",", "").split():

                    # Checks if the key already exists in the dictionary, if it does not exist
                    # add it to the dictionary with a value of 1
                    if words not in dict_o_ints:
                        dict_o_ints[words] = 1

                    # If the word already exists, increment that keys value by one
                    else:
                        dict_o_ints[words] = (dict_o_ints[words] + 1)

            f.close()
            break

    print("\nWriting the dictionary sorted by keys to WordCounts.txt\n")

    # Sorting dictionary by keys
    key_sorted_dict = collections.OrderedDict(sorted(dict_o_ints.items()))

    write_dict_to_file(key_sorted_dict)

    print("\nDisplaying a bar graph of the 20 most occurred words and their occurrence count.\n")

    # Sorting dictionary by values
    value_sorted_dict = collections.OrderedDict(sorted(dict_o_ints.items(), key=lambda kv: kv[1], reverse=True))

    print_graph(value_sorted_dict)


main()

