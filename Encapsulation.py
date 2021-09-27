

#name of protected class
class Brimestone:
    def __init__(self):
        self._protect = "Zealot"
        self.__privato = "eight"

    def getPrivato(self):
        print(self.__privato)

    def setPrivato(self,name):
        self.__privato = name 


#object name 
code = Brimestone()
print(code._protect)
code.getPrivato()
code.setPrivato("duh")
code.getPrivato()





