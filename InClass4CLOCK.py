"""
Author:    Tim Kuelker
Date:       09, 12, 2019
Course:     CMPSCI 4500
Description:  Program takes in a start time from user, in 24-hour time format.  Then it
            takes in an end time from the user, the end time will be sometime in the next
            24-hours after the start time.  Both are checked by a regular expression
            to be sure in proper form.  Program then calculates the time elapsed.  It will
            then draw the "clocks" on the screen to display the starting time, ending time,
            and elapsed time.
"""


import re
from turtle import *


# Python Program to Convert seconds
# into hours, minutes and seconds
def convert(seconds):
    minutes = seconds % 3600/60
    hours = seconds/3600
    return "%d:%02d" % (hours, minutes)


def draw_rectangle(header, times, x, y, title):
    # Drawing first clock
    rectangle = Turtle()

    if title == 0:
        rectangle.penup()
        rectangle.sety(100)
        rectangle.write("Clocks all in 24-hour time format (HH:MM)", False, "center", ("Arial", 30, "normal"))

    # Moving pen to left side of screen
    rectangle.penup()
    rectangle.setx(x)
    rectangle.sety(y)
    rectangle.pendown()

    rectangle.begin_fill()

    # Building shape
    rectangle.right(90)
    rectangle.forward(100)
    rectangle.left(90)
    rectangle.forward(180)
    rectangle.left(90)
    rectangle.forward(100)
    rectangle.left(90)
    rectangle.forward(180)

    # Filling color
    rectangle.color("blue")
    rectangle.end_fill()

    # Putting time in place
    rectangle.penup()
    rectangle.setx(x + 90)
    rectangle.sety(y - 65)
    rectangle.pendown()
    rectangle.color("red")
    rectangle.write(times, False, "center", ("Arial", 24, "normal"))

    rectangle.penup()
    rectangle.sety(y + 5)
    rectangle.pendown()
    rectangle.color("black")
    rectangle.write(header, False, "center", ("Arial", 24, "normal"))
    rectangle.hideturtle()


time_pattern = re.compile("^([01][0-9]|2[0-3]):?([0-5][0-9])$")
while True:
    start_time = input("Please enter a START time in 24-hour format (00:00 - 23:59): ")

    if not time_pattern.match(start_time):
        print("\nNot in 24-hour time format, try again.\n")
        continue
    else:
        start_time_hours = start_time.split(':')[0]
        start_time_minutes = start_time.split(':', 1)[1]
        break

while True:
    end_time = input("Please enter an END time (sometime in the next 24 hours) in 24-hour format (00:00 - 23:59): ")

    if not time_pattern.match(end_time):
        print("\nNot in 24-hour time format, try again.\n")
        continue
    else:
        end_time_hours = end_time.split(':')[0]
        end_time_minutes = end_time.split(':', 1)[1]
        break

start_time_seconds = (int(start_time_hours) * 60 * 60) + (int(start_time_minutes) * 60)
end_time_seconds = (24 * 60 * 60) + (int(end_time_hours) * 60 * 60) + (int(end_time_minutes) * 60)

time_elapsed = end_time_seconds - start_time_seconds

clock_headers = ["Start Time", "End Time", "Elapsed Time"]
clock_times = [start_time, end_time, convert(time_elapsed)]

y_coord = 0
x_coord = -400
i = 0
while i < 3:
    draw_rectangle(clock_headers[i], clock_times[i], x_coord, y_coord, i)
    x_coord += 300
    i += 1

done()

