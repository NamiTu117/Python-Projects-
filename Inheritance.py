
#main class 
class Character:
    name = "Aloyna"
    race = "Dranei" 
    occupation = "Alliance" 
    class_type = ""

#game information 
class Game(Character):
    company = "Blizzard Entertainment" 
    game = "World of Warcraft"
    

#third class, describes account info 
class Account(Character):
    name = ""
    email = "esgel@gmail.com" 
    password = "tillitsbackwards"
    subscription = 'Monthly' 
    
    
