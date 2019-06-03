import random

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
