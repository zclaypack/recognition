'''
Recognition - Password Manager - Main
Python 3.7.4
A password manager which, generates a password and stores it in a text file.
'''

#Import Statements
import functions

#Loop That Goes Until Broken
while True:
    #Call The Menu Prompt
    functions.menuPrompt()
    #Take Users Input
    UserChoice = input("Please Select An Option: ")

    if UserChoice == '1':
        functions.createLogin()
    elif UserChoice == '2':
        functions.displayLogins()
    elif UserChoice == '3':
        break
    else:
        print("Oops! You didn't enter a number between 1-3, please try again!")