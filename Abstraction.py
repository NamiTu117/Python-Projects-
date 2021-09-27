from abc import ABC, abstractmethod

#parent class utitlizing abstractmethod 
class Beastiary(ABC):
    def Book(self, dictionary):
        print("You have selected:  ", dictionary)
        @abstractmethod 
        def Read(self, dictionary):
            pass #passes this function to the child function


class Chapters(Beastiary):
#implementing Book function (dictionary)
    def Read(self,dictionary):
        print ("Hearing a beautiful voice near the water may indicate a {} is close." .format(dictionary))


#objects printing out results 
codex = Chapters()
codex.Book("Siren")
codex.Read("Siren")
        
    
