from EncryptionClass import Encryption
from DictionaryClass import Dict

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
