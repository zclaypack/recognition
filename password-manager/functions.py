'''
Recognition - Password Manager - Functions
Python 3.7.4
Functions needed for Password Manager
'''

#Import Statements
import random
import csv

#Pre Defined Variables
lettersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersLower = lettersUpper.lower()
lettersAll = lettersUpper + lettersLower
numbers = "1234567890"
characters = "!@#$%&*():;/"


#Functions

#Function to Create Menu Prompt
def menuPrompt():
    print("Press 1 - To Create a Login")
    print("Press 2 - To Display All Currently Saved Logins")
    print("Press 3 - To Quit the Program")

#Function to Create Login
def createLogin():
    website = input("Name of Website/Login: ")
    username = input("Username/Email for Login: ")
    passwordCheck = input("Please enter a password! If you want a randomly generated password, hit the ENTERKEY. : ")
    if passwordCheck == "":
        password = generatePassword()
    else:
        password = passwordCheck
    print("Login: {} ".format(website))
    print("Username: {} ".format(username))
    print("Password: {} ".format(password))
    print("Has Been Saved!")
    print()
    dataFormat = [["Login", "Username", "Password"],
                [website, username, password],
                [""]]
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerows(dataFormat)

#Function to Display Logins
def displayLogins():
    with open('passwords.csv', "r") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            for i in row:
                print(i)

#Funcation to Generate A Password
def generatePassword():
    counter = 0
    tempPassword = ""
    while counter != 6:
        randomLetter = (random.choice(lettersAll))
        randomNumber = (random.choice(numbers))
        randomCharacter = (random.choice(characters))
        tempPassword = tempPassword + str(str(randomLetter) + str(randomNumber) + str(randomCharacter))
        counter += 1
    generatedPassword = tempPassword
    return generatedPassword

