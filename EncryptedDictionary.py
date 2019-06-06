from EncryptionClass import Encryption
# from DictionaryClass import Dict
import time
import os

CrPa_loop = False
while CrPa_loop is False:
    passw1 = input("Enter a Password: ")
    passw2 = input("Please reenter Password: ")
    if passw1 == passw2:
        encrypt = Encryption(passw1)
        EK = encrypt.generate_ekey()
        CrPa_loop = True
    else:
        print("Error: Password does not match!")
        print("")

print('\n'*1000)  # if program is ran in IDE like pycharm that inhibits os functions
os.system('cls' if os.name == 'nt' else 'clear')  # clears previous lines if ran in command/terminal
print("Password has been set!")
print("----------------------")
wrongPcount = 0
while encrypt.validPass is False:
    EK2 = encrypt.isValidPass(wrongPcount, EK)
    if encrypt.validPass is True:
        break
    wrongPcount += 1
    if wrongPcount >= 3:
        while True:
            print("Wrong password entered too many times! Please restart console")
            time.sleep(2)


if EK2 == EK:
    choice = 1
    while True:
        print("------------------------------")
        print("")
        print("1. Create a key and value pair")
        print("2. Change the value of a key")
        print("3. Swap key values")
        print("4. Display Dictionary")
        print("5. Export data to new file")
        print("6. Logout")
        print("")
        choice = input("Please enter a number for the desired task or '0' to Exit: ")

        if choice == "0":
            print("Thank you!")
            time.sleep(2)
            break

        elif choice == "1":
            print("Place holder")
            
        elif choice == "2":
            print("Place holder")
            
        elif choice == "3":
            print("Place holder")
            
        elif choice == "4":
            print("Place holder")
            
        elif choice == "5":
            print("Place holder")

        elif choice == "6":
            encrypt.logout(passw1)
            
        else:
            print("Error: Invalid choice. Please choose again")
