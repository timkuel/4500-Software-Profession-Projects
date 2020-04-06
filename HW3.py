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


# Function to write the title to the turtle display
def write_title(turtle, n, title):
    turtle.penup()
    turtle.sety(((n * LENGTH) / 2) + LENGTH)
    turtle.pendown()
    turtle.write("Painting " + str(title), False, "center", ("Ariel", 30, "normal"))


# Function to draw the key box
def draw_key_box(turtle, n):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.sety(((n * LENGTH) / 2))
    turtle.setx(((n * LENGTH) / 2) + LENGTH)
    turtle.pendown()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(140)
    turtle.right(90)


# Function to write the tile of the key box
def write_key_box(turtle):
    turtle.penup()
    turtle.goto(turtle.pos() + (75, -20))
    turtle.pendown()
    turtle.write("KEY", False, "center", ("Ariel", 16, "bold", "underline"))


# Function to draw a blank square in the key box
def draw_empty_square(turtle, x, y):
    turtle.penup()
    turtle.goto(turtle.pos() + (x, y))
    turtle.pendown()

    turtle.forward(LENGTH)
    turtle.right(90)
    turtle.forward(LENGTH)
    turtle.right(90)
    turtle.forward(LENGTH)
    turtle.right(90)
    turtle.forward(LENGTH)
    turtle.right(90)


# Function to write empty square info for the key box
def write_square(turtle, title):
    turtle.penup()
    turtle.goto(turtle.pos() + (LENGTH + 10, -LENGTH))
    turtle.pendown()
    turtle.write(":", False, "center", ("Ariel", LENGTH, "normal"))
    turtle.penup()
    turtle.goto(turtle.pos() + (0, 5))
    turtle.pendown()
    turtle.write(title, False, "left", ("Ariel", 12, "bold"))


# Writing all info besides the grid to the screen
def write_info(turtle, n):
    # Creating rectangle for key
    draw_key_box(turtle, n)

    # Writing in the 'Key' box
    write_key_box(turtle)

    # Drawing empty square for key representation
    draw_empty_square(turtle, -70, -20)

    # Writing key info for empty square
    write_square(turtle, " EMPTY")

    # Drawing another empty square for key representation
    draw_empty_square(turtle, -40, -20)

    # Storing the top right as turtle_pos
    # turtle.right(180)
    turtle_pos = turtle.pos()

    i = 0
    while i < 3:
        # X's range is 5, 25 due to how turtle draws circle
        cell_x = int(random.uniform(LENGTH - RADIUS, RADIUS))

        # Y's range is 0, 20 due to how turtle draws circle
        cell_y = int(random.uniform(LENGTH, RADIUS * 2))

        turtle.penup()
        turtle.goto(turtle.pos() + (cell_x, -cell_y))
        turtle.pendown()

        draw_circle(turtle)

        turtle.penup()
        turtle.goto(turtle_pos)
        turtle.pendown()
        i += 1

    # Writing key info about that square
    write_square(turtle, " COLORED IN")


# Function that monitors time, as time increases so does the turtle draw speed
def get_turtle_speed(start_time, timer):
    if timer - start_time < 10:
        speed = "slow"
    elif timer - start_time < 20:
        speed = "normal"
    elif timer - start_time < 30:
        speed = "fast"
    else:
        speed = "fastest"

    return speed


# Draws a n x n grid to drop blobs of paint in
def grid(turtle, n):
    sign = 1
    for _ in range(2):

        for _ in range(n):
            turtle.forward(LENGTH * n)
            turtle.left(sign * 90)
            turtle.forward(LENGTH)
            turtle.left(sign * 90)
            sign = 0 - sign

        turtle.forward(LENGTH * n)
        [turtle.right, turtle.left][n % 2](90)
        sign = 0 - sign


# Moves the turtle position to some random location on the n x n grid
# and keeps track of that location
def get_random_location(turtle, n, grid_filler):
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

    turtle.penup()

    # Calculation true position from the grid_location and the cell location.
    x = (((grid_x - neg_threshold) * LENGTH) - cell_x)
    y = (((grid_y - neg_threshold) * LENGTH) - cell_y)

    turtle.goto(x, y)

    turtle.pendown()


# Drawing circle in random location that is inside the random grid location
def draw_circle(turtle):
    color = ["Chartreuse", "Goldenrod", "Gainsboro", "Steel Blue", "Red", "Orange", "Cyan", "Aquamarine", "yellow",
             "Green", "Blue", "Purple", "Dark Slate Gray", "Midnight Blue", "Deep Pink"]

    # drawing a 'blob'
    turtle.begin_fill()

    # building shape
    turtle.circle(RADIUS)

    # Filling color
    turtle.fillcolor(color[random.randint(0, len(color) - 1)])
    turtle.end_fill()


# Chooses a random location on n x n grid and draws a circle in it
def drop_blob(turtle, n, grid_filler):
    turtle.shape("turtle")

    # Moving to random location on grid
    get_random_location(turtle, n, grid_filler)

    # Moving circle randomly within square
    draw_circle(turtle)


def kill_turtle(turtle):
    turtle.getscreen().bye()


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
            if k in range(1, 11):
                print("\nThank You!\n")
                break
            else:
                print("\n\tUser input must be an integer between 1 and 10 inclusively.\n")

    print("\nThis program will now begin to draw the " + str(k) + " - " + str(n) + " x " + str(n) + " canvas(es).\n"
          "The longer this program takes to complete the drawing, the more the turtles drawing speed increases!\n"
          "\n\tProgram will begin painting in 2 seconds!\n")

    time.sleep(2)

    print("\nDrawing Key-Box\n")

    # Initializing min an max values to extremes
    all_time_min_blobs = 1000000
    all_time_max_blobs = 0
    all_time_blobs = 0

    cells_min_blobs = 1000000
    cells_max_blobs = 0

    # Creating key turtle so only need to draw key once
    key = Turtle()
    write_info(key, n)
    key.hideturtle()

    # Turtle object for the canvas
    canvas = Turtle()

    # Loop runs until all paintings finished
    j = 0
    while j < k:
        # Resetting canvas for new paining
        canvas.reset()

        print("\nStarting Painting " + str(j + 1) + "!\n")

        grid_filler = [[0 for _ in range(n)] for _ in range(n)]
        total_blobs = 0

        # Writing the title of each painting
        write_title(canvas, n, j + 1)

        # Centering the paint canvas
        canvas.penup()
        canvas.goto(-n * LENGTH / 2, -n * LENGTH / 2)  # center our grid (optional)
        canvas.pendown()

        # Drawing the paint canvas as fast as turtle can
        canvas.speed("fastest")
        grid(canvas, int(n))

        time_start = time.perf_counter()

        # Run while loop until there is not a 0 in grid_filler
        while any(0 in sublist for sublist in grid_filler):
            canvas.speed(get_turtle_speed(time_start, time.perf_counter()))

            drop_blob(canvas, int(n), grid_filler)

            total_blobs += 1

        all_time_blobs += total_blobs
        all_time_min_blobs = min(all_time_min_blobs, total_blobs)
        all_time_max_blobs = max(all_time_max_blobs, total_blobs)

        flattened_grid_filler = [j for sub in grid_filler for j in sub]

        cells_min_blobs = min(cells_min_blobs, min(flattened_grid_filler))
        cells_max_blobs = max(cells_max_blobs, max(flattened_grid_filler))

        # Waits until something is entered to continue program
        input("\nDone with Painting " + str(j + 1) + "!\n"
              "\n\tTo begin next painting, if there is one, PRESS ENTER/RETURN to continue!\n")

        j += 1

    print("\nDone painting, removing turtle screen in 3 seconds!\n")

    time.sleep(3)
    kill_turtle(canvas)

    print("\nOn average it took " + str(all_time_blobs / k) + " blobs to finish a painting.\n"
          "The maximum number of blobs on a canvas was " + str(all_time_max_blobs) +
          "\nThe minimum number of blobs on a canvas was " + str(all_time_min_blobs))

    print("\nFrom all paintings, on average a cell contains " + str((all_time_blobs / k) / (n * n)) + " blobs.\n"
          "The maximum number of blobs in a single cell was " + str(cells_max_blobs) +
          "\nThe minimum number of blobs in a single cell was " + str(cells_min_blobs))


main()

