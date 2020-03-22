'''
Recognition - Password Generator
Python 3.7.4.
Functions needed for password generator
'''

#Import Statements 
import random

#Pre Defined Variables
lettersUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersLower = lettersUpper.lower()
lettersAll = lettersUpper + lettersLower
numbers = "1234567890"
characters = "!@#$%&*():;/"

# Funcation to Generate A Password
def generatePassword():
    counter = 0
    tempPassword = ""
    while counter != 8:
        randomLetter = (random.choice(lettersAll))
        randomNumber = (random.choice(numbers))
        randomCharacter = (random.choice(characters))
        tempPassword = tempPassword + str(str(randomLetter) + str(randomNumber) + str(randomCharacter))
        counter += 1
    generatedPassword = tempPassword
    return generatedPassword