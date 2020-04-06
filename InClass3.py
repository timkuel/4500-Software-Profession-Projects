""" Author:    Tim Kuelker
    Date:       September 03, 2019
    Course:     CMPSCI 4500
    Description: Program that does file input from a file called InClass3infile.txt.  This file is guaranteed to have
                four numbers, each one on its own line, and no other lines. There will be no blanks in the file.
                The numbers will be: an integer from 1 to 1000, an integer from 1 to 100, a real number
                from 0.000 to 1.000, with a digit before the decimal point, and three digits behind the decimal point,
                an integer from 2 to 20.  I will refer to these numbers respectively as number of times at bat (AtBats),
                random seed (Rseed), batting average (BatAverage), and number of simulations (NumSims).  After you read
                in the four numbers, you will do a simulated "season" for the batter NumSims times. Each season involves
                simulating a batter with the batting average BatAverage batting AtBats times. For each at bat, throw a
                random number between 0.0 and 1.0 from a uniform random distribution. Use Rseed to seed Python's random
                number generator. If the number you throw is less than or equal to the BatAverage, then the batter
                gets a hit. If the number you throw is greater than BatAverage, the batter does not get a hit.
                Keep doing this AtBats times.  All output stored to InClass3Outfile.txt """

import random

# Opening InClass3infile.txt and storing the lines to respective variables
with open("InClass3infile.txt", "r") as in_file:

    # Reading first line to AtBats and checking format
    AtBats = int(in_file.readline().rstrip())
    if AtBats not in range(1, 1001):
        with open("InClass3outfile.txt", "w") as out_file:
            out_file.write("The number of at bats in the first line must be between 1 and 1000, not " + str(AtBats))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

    # Reading second line to Rseed and checking format
    Rseed = int(in_file.readline().rstrip())
    if Rseed not in range(1, 101):
        with open("InClass3outfile.txt", "w") as out_file:
            out_file.write("The number used to seed the random number generator on the second line "
                           "must be between 1 and 100, not " + str(Rseed))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

    # Reading third line to BatAverage and checking format
    BatAverage = float(in_file.readline().rstrip())
    if BatAverage > 1:
        with open("InClass3outfile.txt", "w") as out_file:
            out_file.write("The batting average must be between 0.000 and 1.000, not " + str(BatAverage))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

    # Reading third line to BatAverage and checking format
    NumSims = int(in_file.readline().rstrip())
    if NumSims not in range(2, 21):
        with open("InClass3outfile.txt", "w") as out_file:
            out_file.write("The Number of Simulations must be between 2 and 20, not " + str(NumSims))
        print("\nError: Check InClass2outfile.txt for more info.")
        exit(1)

i = 0
j = 0
rndHit = 0

seasonHitsRow = 0
allTimeHits = 0
totalAtBats = 0

avgHitsRowSeason = 0
averageHitsOfAllSeasons = 0
averageOfMaxHitsRowAllTime = 0

# Setting maximums to small number
seasonMaxHitsRow = 0

# Setting minimums to large number
minOfMaxHitsRowAllTime = AtBats
minHitsOfAllSeasons = (AtBats * NumSims)
minBatAverageOfAllSeasons = 1.000

# Seeding the random number generator
random.seed(Rseed)

while j < NumSims:
    i = 0
    seasonHits = 0
    hitPrev = 0

    while i < AtBats:

        # Getting a random number between 0.0 and 1.0 from uniform random distribution
        rndHit = random.uniform(0.0, 1.0)

        # Logic to determine if a batter got a hit or not
        if rndHit <= BatAverage:
            hitPrev = True
            seasonHits += 1
        else:
            hitPrev = False

        if hitPrev:
            seasonHitsRow += 1
        else:
            seasonMaxHitsRow = max(seasonHitsRow, seasonMaxHitsRow)
            avgHitsRowSeason += seasonMaxHitsRow

            seasonHitsRow = 0
        i += 1

    batAvg = seasonHits / AtBats

    # Calculating minimums
    minBatAverageOfAllSeasons = min(minBatAverageOfAllSeasons, batAvg)
    minHitsOfAllSeasons = min(minHitsOfAllSeasons, seasonHits)
    minOfMaxHitsRowAllTime = min(minOfMaxHitsRowAllTime, seasonMaxHitsRow)

    # Calculating totals for average
    averageHitsOfAllSeasons += seasonHits
    averageOfMaxHitsRowAllTime += seasonMaxHitsRow

    allTimeHits += seasonHits

    j += 1

totalAtBats = AtBats * NumSims
allTimeBatAvg = allTimeHits / totalAtBats

# Calculating averages
averageHitsOfAllSeasons /= NumSims
averageOfMaxHitsRowAllTime /= NumSims

# Writing collected data to InClass2outfile.txt
with open("InClass3outfile.txt", "w") as out_file:
    out_file.write("The number used to seed the random number generator for the simulation was " + str(Rseed))
    out_file.write("\nThe hitters batting average used for the simulation was %.3f" % BatAverage)
    out_file.write("\nThe number of at bats per season simulated was " + str(AtBats))
    out_file.write("\nThe number of seasons simulated was " + str(NumSims))

    out_file.write("\n\nThe total number of HITS the batter got during the " + str(NumSims) + " season(s) simulated "
                   "was " + str(allTimeHits))
    out_file.write("\nThe batters total Batting Average during the " + str(NumSims) + " season(s) simulated was %.3f"
                   % allTimeBatAvg)
    out_file.write("\nThe Maximum number of HITS-IN-A-ROW during one of the " + str(NumSims) + " season(s) simulated "
                   "was " + str(seasonMaxHitsRow))
    out_file.write("\nThe Minimum number of HITS the batter got during one of the " + str(NumSims) +
                   " season(s) simulated was " + str(minHitsOfAllSeasons))
    out_file.write("\nThe Minimum Batting Average the batter got during one of the " + str(NumSims) + " season(s) "
                   "simulated was %.3f" % minBatAverageOfAllSeasons)
    out_file.write("\nThe Minimum of the Maximum number of games with HITS-IN-A-ROW during one of the " + str(NumSims) +
                   " season(s) simulated was " + str(minOfMaxHitsRowAllTime))
    out_file.write("\nThe Average number of HITS the batter got during one of the " + str(NumSims) +
                   " season(s) simulated was %.1f" % averageHitsOfAllSeasons)
    out_file.write("\nThe Average of the Maximum number of games with HITS-IN-A-ROW during one of the " + str(NumSims) +
                   " season(s) simulated was " + str(averageOfMaxHitsRowAllTime))

print("\nDone running the simulation, all output has been stored to InClass3outfile.txt.  "
      "\n\t\t\t\tPress ENTER to finish running the program.")

input()

