class Player:
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def __str__(self):
        return "\nName: %s\nSymbol: %s\n" % self.__name, self.__symbol
