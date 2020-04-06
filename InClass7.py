"""Author:      Timothy Kuelker
    Date:       October 1, 2019
    Course:     CMPSCI 4500
    Description:This program reads information from a user.  The first input will be the dimensions
    of a grid.  The next input will be the number of grids to be drawn.   The program will then draw
    a grid of size n x n using turtle graphics.   It will then randomly place a paint blob into each
    square of the grid, making sure that no paint spills out.  When all cells have at least one blob
    of paint, that painting is finished.  The user will be prompted to press enter to start the next
    painting. After all paintings have finished, information about the blobs of paint will be displayed
    on the console.  Any information about a function should be in a comment above that function.

    Draw Speed: So that the drawing process doesn't take too long, and so the user can see whats happening,
    I increment the speed.  Starting at 'slowest', every 10 seconds the turtle speed will step up one
    notch until 'fastest' is reached.   Could tweak this to draw faster or slower depending on time.
"""


from turtle import *
import time
import random

LENGTH = 30  # each grid element will be LENGTH x LENGTH pixels
RADIUS = 5   # each circle element will have a radius of 5


# and keeps track of that location
def get_random_location( n, grid_filler):
    neg_threshold = int(n) / 2

    # Getting a random cell location on the grid
    grid_x = int(random.randint(1, n))
    grid_y = int(random.randint(1, n))

    grid_filler[grid_x - 1][grid_y - 1] += 1

    # Getting a random location in the cell on the grid

    # X's range is 5, 25 due to how turtle draws circle
    cell_x = int(random.uniform(LENGTH - RADIUS, RADIUS))

    # Y's range is 0, 20 due to how turtle draws circle
    cell_y = int(random.uniform(LENGTH - (RADIUS * 2), 0))

    # Calculation true position from the grid_location and the cell location.
    x = (((grid_x - neg_threshold) * LENGTH) - cell_x)
    y = (((grid_y - neg_threshold) * LENGTH) - cell_y)


def main():
    # Getting size of grid, storing in n
    while True:
        try:
            # Getting size of grid
            n = int(input("Please enter a number between 2 and 15 inclusively for the size of the 'canvas': "))
        except ValueError:
            print("\n\tValue Error: Value must be an INTEGER\n")
        else:
            if n in range(2, 16):
                print("\nThank You!\n")
                break
            else:
                print("\n\tUser input must be an integer between 2 and 15 inclusively.\n")

    # Getting number of 'paintings', storing in k
    while True:
        try:
            # Getting size of grid
            k = int(input("Please enter a number between 1 and 10 inclusively for the number of 'canvases': "))
        except ValueError:
            print("\n\tValue Error: Value must be an INTEGER\n")
        else:
            if k in range(1, 101):
                print("\nThank You!\n")
                break
            else:
                print("\n\tUser input must be an integer between 1 and 10 inclusively.\n")

    print("\nThis program will now begin to draw the " + str(k) + " - " + str(n) + " x " + str(n) + " canvas(es).\n"
          "The longer this program takes to complete the drawing, the more the turtles drawing speed increases!\n"
          "\n\tProgram will begin painting in 2 seconds!\n")


    # Initializing min an max values to extremes
    all_time_min_blobs = 1000000
    all_time_max_blobs = 0
    all_time_blobs = 0

    cells_min_blobs = 1000000
    cells_max_blobs = 0

    # Loop runs until all paintings finished
    j = 0
    while j < k:

        print("\nStarting Painting " + str(j + 1) + "!\n")

        grid_filler = [[0 for _ in range(n)] for _ in range(n)]
        total_blobs = 0

        # Run while loop until there is not a 0 in grid_filler
        while any(0 in sublist for sublist in grid_filler):
            get_random_location(int(n), grid_filler)

            total_blobs += 1

        all_time_blobs += total_blobs
        all_time_min_blobs = min(all_time_min_blobs, total_blobs)
        all_time_max_blobs = max(all_time_max_blobs, total_blobs)

        flattened_grid_filler = [j for sub in grid_filler for j in sub]

        cells_min_blobs = min(cells_min_blobs, min(flattened_grid_filler))
        cells_max_blobs = max(cells_max_blobs, max(flattened_grid_filler))

        # Waits until something is entered to continue program
        print("\nDone with Painting " + str(j + 1) + "!\n")

        j += 1

    print("\nDone painting!\n")

    print("\nOn average it took " + str(all_time_blobs / k) + " blobs to finish a painting.\n"
          "The maximum number of blobs on a canvas was " + str(all_time_max_blobs) +
          "\nThe minimum number of blobs on a canvas was " + str(all_time_min_blobs))

    print("\nFrom all paintings, on average a cell contains " + str((all_time_blobs / k) / (n * n)) + " blobs.\n"
          "The maximum number of blobs in a single cell was " + str(cells_max_blobs) +
          "\nThe minimum number of blobs in a single cell was " + str(cells_min_blobs))


main()
