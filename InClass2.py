""" Author:    Tim Kuelker
    Date:       August 27, 2019
    Course:     CMPSCI 4500
    Description: Program that does file input from a file called InClass2infile.txt.  This file is guaranteed to have
    three numbers, each one on its own line, and no other lines. There will be no blanks in the file. The numbers will
    be: an integer from 1 to 1000, an integer from 1 to 100, and a real number from 0.000 to 1.000, with a digit
    before the decimal point, and three digits behind the decimal point.  After you read in the three numbers, simulate
    a batter with the batting average BatAverage batting AtBats times. For each at bat, throw a random number between
    0.0 and 1.0 from a uniform random distribution. Use Rseed to seed Python's random number generator.  If the number
    you throw is less than or equal to the BatAverage, then the batter gets a hit. If the number you throw is greater
    than BatAverage, the batter does not get a hit. Keep doing this AtBats times.
    All output stored to InClass2Outfile.txt """

import random

# Opening InClass2infile.txt and storing the lines to respective variables
with open("InClass2infile.txt", "r") as in_file:

    # Reading first line to AtBats and checking format
    AtBats = int(in_file.readline().rstrip())
    if AtBats not in range(1, 1001):
        with open("InClass2outfile.txt", "w") as out_file:
            out_file.write("The number of at bats in the first line must be between 1 and 1000, not " + str(AtBats))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

    # Reading second line to Rseed and checking format
    Rseed = int(in_file.readline().rstrip())
    if Rseed not in range(1, 101):
        with open("InClass2outfile.txt", "w") as out_file:
            out_file.write("The number used to seed the random number generator on the second line "
                           "must be between 1 and 100, not " + str(Rseed))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

    # Reading third line to BatAverage and checking format
    BatAverage = float(in_file.readline().rstrip())
    if BatAverage > 1:
        with open("InClass2outfile.txt", "w") as out_file:
            out_file.write("The batting average must be between 0.000 and 1.000, not " + str(BatAverage))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

# Seeding the random number generator
random.seed(Rseed)

i = 0
rndHit = 0
totalHits = 0
maxHitsRow = 0
hitsRow = 0

while i < AtBats:

    # Getting a random number between 0.0 and 1.0 from uniform random distribution
    rndHit = random.uniform(0.0, 1.0)

    # Logic to determine if a batter got a hit or not
    if rndHit <= BatAverage:
        hitPrev = True
        totalHits += 1
    else:
        hitPrev = False

    if hitPrev:
        hitsRow += 1
    else:
        maxHitsRow = max(hitsRow, maxHitsRow)
        hitsRow = 0

    i += 1

# Calculating batting average
batAvg = totalHits / AtBats

# Writing collected data to InClass2outfile.txt
with open("InClass2outfile.txt", "w") as out_file:
    out_file.write("The number used to seed the random number generator for the simulation was " + str(Rseed))
    out_file.write("\nThe hitters batting average used for the simulation was " + str(BatAverage))
    out_file.write("\nThe number of at bats simulated was " + str(AtBats))
    out_file.write("\n\nThe number of hits the batter got during the simulation was " + str(totalHits))
    out_file.write("\nThe batters batting average during the simulation was %.3f" % batAvg)
    out_file.write("\nThe maximum number of hits in a row during the simulation was " + str(maxHitsRow))

print("\nDone running the simulation, all output has been stored to InClass2outfile.txt.  "
      "\n\t\t\t\tPress ENTER to finish running the program.")

input()

