class Dict:
    def __init__(self):
        self.UserDict = {}

    def __setitem__(self, key, item):
        self.__dict__[key] = item

    # def __getitem__(self, key):
        # self.__dict__[key]

    def KeyandVal(self, dic, key, val):
        dic[key] = val

    def SwapVal(self, dic, key1, key2):
        temp = ""
        temp = dic[key1]
        dic[key1] = dic[key2]
        dic[key2] = temp

    def display(self, dic):  # need to make work
        for dic.UserDict.key, dic.UserDict.value in dic.UserDict:
            print(dic.UserDict[key1])
            print(dic.UserDict[key2])

    def export(self):  # need to finish
        f = open("New_Data.txt", 'w')
        
