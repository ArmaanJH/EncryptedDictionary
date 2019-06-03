from EncryptionClass import Encryption
# from DictionaryClass import Dict
import time

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
        print("1. Create a key and value pair")
        print("2. Change the value of a key")
        print("3. Swap key values")
        print("4. Display Dictionary")
        print("")
        choice = input("Please enter a number for the desired task or '0' to Exit: ")

        if choice == 0:
            break

        elif choice == 1:
            print("Place holder")
        elif choice == 2:
            print("Place holder")
        elif choice == 3:
            print("Place holder")
        elif choice == 4:
            print("Place holder")
