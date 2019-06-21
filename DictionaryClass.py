class Dict:
    def __init__(self):
        self.UserDict = {}

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __iter__(self):
        return iter(self.key)

    def KeyandVal(self, key, val):
        self.UserDict[key] = val

    def changeVal(self, key):
        cKey = False
        for keys in self.UserDict:
            if key == keys:
                cKey = True
        if cKey is True:
            val = input("Enter new value: ")
            self.UserDict[key] = val
        else:
            print("Key does not exist!")

    def SwapVal(self, key1, key2):
        cKey1 = False
        cKey2 = False
        for key in self.UserDict:
            if key1 == key:
                cKey1 = True
            if key2 == key:
                cKey2 = True

        if cKey1 is True and cKey2 is True:
            temp = ""
            temp = self.UserDict[key1]
            self.UserDict[key1] = self.UserDict[key2]
            self.UserDict[key2] = temp
            print("Values Swaped!")
        else:
            print("One or more of the keys provided do not exist!")

    def display(self):
        for key, value in self.UserDict.items():
            print(key, end=":  ")
            print(value)

    def export(self):  # need to finish
        f = open("New_Data.txt", 'w')
        f.write("KEY")
        f.write("   ")
        f.write("VALUE")
        f.write("\n")
        for key, value in self.UserDict.items():
            f.write(key)
            f.write(":   ")
            f.write(value)
            f.write("\n")
        print("Data exported to new .txt file!")
