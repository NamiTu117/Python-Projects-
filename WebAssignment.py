import webbrowser
import generator 


#create a script that should open to a new html file that says:
#"Stay tuned for our amazing summer sale!"

#creates simple html file 
text = ''' 
<html>
    <body>
        <h1>
    Stay tuned for our amazing summer sale!

        </h1>
    </body>
</html>
'''



#opens new html file 
file = open("assignment.html", "w")
file.write(text)
file.close()
