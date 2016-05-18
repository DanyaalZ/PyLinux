import time
import platform
from datetime import datetime

#OS 
def OS():
    command = input ("@root: ~$ ")
    if command == "pwd":
        print ("/root")
        OS()
    if command == "shutdown":
        print ("Shutting down...") 
        time.sleep(3)
        quit()
        OS()
    if command == "shutdown -h now":
        quit()
    if command == "shutdown -r now":
        OS()        
    if command == "startx":
        print ("No gui currently in OS")
        OS()
    if command == "ls":
        print ("Desktop \n Downloads \n Music \n Public \n Videos \n Documents \n Pictures \n")
        OS()
    if command == "echo":
        echo = input ("echo: ")
        print (echo)
        OS()
#Root password
def Password():  
    sudo = input ("Welcome, root please enter the password for the system ")
    if sudo == 'toor':
        print ("Started root at:", str(datetime.now()))
        OS()
    elif sudo != 'toor':
        print ("Incorrect password please try again.")
        time.sleep(1)
        Password()

#beggining     
print ("Welcome to PyLinux v0.1 alpha")
time.sleep(1)
print ("v0.1, running on OS:", platform.system(), "PyLinux nogui")
time.sleep(1)
Password()


    

