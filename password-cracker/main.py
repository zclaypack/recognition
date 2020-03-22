'''
Recognition - Password Cracker
Python 3.7.4
Brute Force tool for passwords created in Python
'''

#Imports
import itertools

#Pre Defined Variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = alphabet.upper()
alphabetAll = alphabet + alphabetUpper
numbersAll = "1234567890"
charactersAll = "!@#$%^&*()[]/"

#Passoword Cracker Function
def guessPassword(password):
    possibleChars = alphabetAll + numbersAll + charactersAll
    attemptCount = 0 
    for passwordLength in range(1, 20):
        for guess in itertools.product(possibleChars, repeat=passwordLength):
            attemptCount += 1
            guess = ''.join(guess)
            if guess == password:
                return 'The password is {}. It was found in {} guesses.'.format(guess, attemptCount)
            print("Attempted Password {} Attempt # {}".format(guess, attemptCount))

#User Inputs Password
userPassword = input("Please enter a password to be cracked: ")

#Call Function Using User Input
print(guessPassword(userPassword))