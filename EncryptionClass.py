import random
import time
import os

class Encryption:
    def __init__(self, password):
        self.password = password
        self.validPass = False

    def generate_ekey(self):
        charlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                    'q', 'r', 's', 't', 'u' 'v', 'w', 'x',
                    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
                    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                    'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
                    '5', '6', '7', '8', '9', '0', '!', '@',
                    '#', '$', '%', '^', '&', '*', '(', ')']
        encryption_key = ""
        for x in range(1,17):
            encryption_key += random.choice(charlist)
        return encryption_key

    def isValidPass(self, count, EK):
        p = input("Password: ")
        ekPass = ""
        if p != self.password:
            print("Invalid Password")
            print("%d attempts left\n" % (2-count))
            self.validPass = False
        else:
            print('\n' * 1000)  # if program is ran in IDE like pycharm that inhibits os functions
            os.system('cls' if os.name == 'nt' else 'clear')  # clears previous lines if ran in command/terminal
            print("Welcome! ")
            ekPass = EK
            self.validPass = True
        return ekPass

    def logout(self, password):
        print("Logout Successful!")
        print("------------------")
        passw = ""
        count = 0
        while passw != password:
            passw = input("Please Enter your password: ")
            if passw == password:
                print('\n' * 1000)  # if program is ran in IDE like pycharm that inhibits os functions
                os.system('cls' if os.name == 'nt' else 'clear')  # clears previous lines if ran in command/terminal
                print("Welcome!")
                break
            else:
                print("Invalid password")
                print("%d attempts left\n" % (2-count))
                count += 1
                if count == 3:
                    while True:
                        print("Wrong password entered too many times! Please restart console")
                        time.sleep(2)
