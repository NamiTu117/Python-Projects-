import os
import stat
import datetime
from datetime import datetime, timedelta





#browse2 ='User/Nami/OneDrive/Documents/Python-Projects-/Stationary/'



#creating function for user to browse and retrieve folders
def Directory():
     browse ="C:/Users/Nami/OneDrive/Documents/Python-Projects-/Working/"
     browse2="C:/Users/Nami/OneDrive/Documents/Python-Projects-/Stationary/"
     now = datetime.now()
     time = now.strftime("24:00:00")
     #Working has recent files. Stationary is to receive files
     file = input("Working or Stationary: ")
     if file == "Working":
         print(os.listdir(browse))
         file = input("\nSelect any file to see if it's been accessed/modified within the past 24hrs\n")
         if file < time: 
             print("This file was accessed/modified as of recent")
         else:
                 print("This file has not been accessed/modified within the past 24hrs")
     elif file == "Stationary":
         print(os.listdir(browse2))

         #def Detect(Directory):
            # file = input("Select a file to see if it has been accessed/edited within the past 24hrs: ")
             
             



        # print("This file has not been accessed/edited within the past 24hrs.")
             
    
        
        

    
    


    





if __name__ =="__main__":
    Directory()



    
    
                            
                            










