"""Author:     Tim Kuelker
   Date:        September 17, 2019
   Course:      CMPSCI 4500
   Description: Program that allows a user to interact with a stack.  Program will display menu options,
   and based off of those options, perform action with a stack.  For our stack structure, we used a list.
   The list allowed for easy appending and popping to be done on the stack.  When the program is terminated,
   if there is anything left in the stack, it will all be popped. """

from turtle import *


def draw_stack():

    stacker = Turtle()

    # Moving pen up middle of screen to represent stack
    stacker.penup()
    stacker.sety(y)
    stacker.pendown()

    stacker.write(character, False, "center", ("Ariel", 30, "normal"))

    stacker.hideturtle()


def pop_stack():

    square = Turtle()

    square.penup()
    square.setx(x)
    square.sety(y)
    square.pendown()

    #drawing square
    square.begin_fill()

    # Building shape
    square.pencolor("white")
    square.right(90)
    square.forward(35)
    square.left(90)
    square.forward(35)
    square.left(90)
    square.forward(35)
    square.left(90)
    square.forward(35)

    # Filling color
    square.color("white")
    square.end_fill()

    square.hideturtle()


# Stack class with methods to initialize a stack, check if stack is empty,
# push an item onto the top of the stack, and pop items from the stack.
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return item

    def top(self):
        if self.is_empty():
            return "Stack is empty, nothing to show!"

        return self.items[len(self.items) - 1]

    def pop(self):
        if self.is_empty():
            return False

        return self.items.pop()


print("\nBeginning to work with a stack, select [1, 2, 3, 4, or 5] from the menu options below!\n\n")
stack = Stack()
x = -17.5
y = -300
# Loop will run until the user decides to exit the program
while True:
    s = int(input("Would you like to:\n\n\t1: Check if the stack is empty.\n" 
                  "\t2. Push an item onto the top of the stack\n" 
                  "\t3. Print the item at the top of the stack\n" 
                  "\t4. Pop the top item from the stack\n"
                  "\t5. Exit program\n"))

    if s == 1:
        if stack.is_empty():
            print("\nStack is empty!\n")
        else:
            print("\nStack is not empty\n")

    elif s == 2:
        character = input("\nWhat character would you like to push into the stack: ")
        print("\nThe item '" + stack.push(character) + "' was pushed into the stack\n")
        draw_stack()
        y += 40

    elif s == 3:
        print("\nPrinting item at the top of the stack: " + stack.top() + "\n")

    elif s == 4:
        top = stack.top()
        if not stack.pop():
            print("\nAttempting to pop the top item form stack: Stack is empty, nothing to pop!\n")
        else:
            print("\nAttempting to pop the top item form stack: " + top + " was popped from the stack\n")
            y -= 12
            pop_stack()
            y -= 28
    elif s == 5:
        print("\nFreeing any items left in the stack!\n")
        while not stack.is_empty():
            y -= 12
            pop_stack()
            y -= 28
            print(stack.pop())
        print("\nThanks for using program!\n")

        exit(0)
    else:
        print("\nNot a valid input option, try again!\n")

done()

