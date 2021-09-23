

#parent class
class Agent:
    name = "Lourdes Santana"
    birth_date = "05/15/1996" 
    passcode = "79985" 


    def Account(self):
        print("Welcome! This is a new system. Please re-enter your information for a new ID card")
        account_name = input("Name: ")
        account_passcode = input("Passcode:  ") 
        account_birthdate = input("Date of Birth:  ")        
        if (account_name == self.name and account_passcode == self.passcode and account_birthdate == self.birth_date):
            print("Access Granted {}. Go to Pass & ID for your new card.".format(account_name))
        else:
            ("You've entered your information wrong. Try again.")
    


#child class
class Sector(Agent):
    sector_name: "Sector 5" 
    division: "Parapsychology"
    status: "active"
    password: "90Wo9" 

    def Account(self):
        print("Welcome! This is a new system. Please re-enter your information for a new ID card")
        account_name = input("Name: ")
        account_passcode = input("Password: ")
        account_birthdate =input("Date of Birth: ")
        if (account_name ==self.name and account_password == self.password and account_birthdate == self.birth_date)"
            print("Access Granted")
        else:
            print("Access Denied! Re-enter your information)
        
        
            


class Bio(Agent):
    place_of_birth: "Boulder, Colorado"
    school: "Boulder High"
    address: "4650 Kyros Dr."
    zipcode: "80328"

    def Account(self):
        print("Welcome! Please enter your information")
        account_name = input("Name: ")
        account_passcode = input("Password: ")
        account_place = input("Place of Birth: ")
        if (account_name ==self.name and account_password == self.password and account_place == self.place_of_birth)"
            print("Access Granted")
        else:
            print("Access Denied! Re-enter your information)
        
        
            



        
    
    

    
    
    



