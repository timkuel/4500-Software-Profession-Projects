""" Author:    Tim Kuelker
    Date:       August 22, 2019
    Course:     CMPSCI 4500
    Description:Python program that reads name from user, then prints a statement
                    using that users name.  It then waits until ENTER is pressed to end the program. """

""" input reads user input, will store into variable 'name' """
name = input("\nPlease enter your name: ")

""" printing statement """
print("\nHello, " + name + ". Press ENTER to finish this program.")

""" input is waiting for a user to input something from the keyboard,
        so it acts like a wait command until ENTER is pressed """
input()
