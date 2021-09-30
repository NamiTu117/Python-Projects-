import os
import stat
import datetime
from datetime import datetime, timedelta





#browse2 ='User/Nami/OneDrive/Documents/Python-Projects-/Stationary/'



#creating function for user to browse and retrieve folders
def Directory():
     file = input("Open File (Y/N): ")
     if file == "Y":
          browse ="C:/Users/Nami/OneDrive/Documents/Python-Projects-/Files/"
          print(os.listdir(browse))
          file = input ("Select your file: ")
          if file == "Working":
               file1 = "C:/Users/Nami/OneDrive/Documents/Python-Projects-/Files/Working/"
               print(os.listdir(file1))
     elif file == "N":
          print("Have a good day!") 
     
     #Working has recent files. Stationary is to receive files
     

     #    print(os.listdir(browse))
      #   file = input("\nSelect any file to see if it's been accessed/modified within the past 24hrs\n")
     #  if file < time: 
      #       print("This file was accessed/modified as of recent")
       #  else:
        #         print("This file has not been accessed/modified within the past 24hrs")
     #elif file == "Stationary":
      #   print(os.listdir(browse2))

         #def Detect(Directory):
            # file = input("Select a file to see if it has been accessed/edited within the past 24hrs: ")
             
             



        # print("This file has not been accessed/edited within the past 24hrs.")
             
    
        
        

    
    


    





if __name__ =="__main__":
    Directory()



    
    
                            
                            










