import time
import platform
from datetime import datetime
from tkinter import *
import getpass

#Hint for GUI
def hint():
    import tkinter.messagebox as tm
    tm.showinfo ("hint", "Generic Linux username and password")


#GUI
def GUI():
    import tkinter.messagebox as tm
    window = Tk()
    window.wm_title("")



    #This is the username entry
    Label(window, text = "Username:", bg = "light blue") .grid(column = 0, row = 0, sticky = W)
    Username = Entry(window, width = 25)
    Username .grid(column = 2, row = 0, sticky = W)

    #This is the password entry
    Label(window, text = "Password:", bg = "light blue") .grid(column = 0, row = 1, sticky = W)
    Password = Entry(window, width = 25, show='*')
    Password .grid (column = 2, row = 1, sticky = W)
      
    #This is the login code
    def Login():
        text = Username.get()
        text1 = Password.get()
        if text == "root" and text1 == "toor":
           tm.showinfo ("GUI", "GUI goes here")
            
        elif text != "Uname" or text1 != "Pass":
            tm.showinfo ("Incorrect", "Try again")

    #This is the submit button
    Button (window, height = 2, width = 5, text = "Submit", bg = "light blue", command = Login) .grid(column = 2, row = 4, sticky = W)
    Button (window, text = "hint", bg = "Light blue", command = hint) .grid(column = 2, row = 5, sticky = W)
    window.mainloop()
  
#OS 
def OS():
    command = input ("root@root:~$ ")
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
        GUI()
        OS()
    if command == "ls":
        print ("Desktop \nDownloads \nMusic \nPublic \nVideos \nDocuments \nPictures\n")
        OS()
    if command == "echo":
        echo = input ("echo: ")
        print (echo)
        OS()
    if command == "df":
        print ("Filesystem     1K-blocks     Used Available Use% Mounted on")
        print ("/dev/sda1               100000000        0 100000000   0% /")
        OS()
    if command == "exit":
        quit()
    else:
        print (command, ": not found")
        OS()
#Root password
def Password():  
    pw = getpass.getpass(prompt="[sudo] password for root: ")
    if pw == 'toor':
        print ("Started root at:", str(datetime.now()))
        OS()
    elif pw != 'toor':
        print ("Incorrect password please try again.")
        time.sleep(1)
        Password()

#beggining     
print ("Welcome to PyLinux v1.3 alpha")
time.sleep(1)
print ("v1.3, running on OS:", platform.system(), "PyLinux")
time.sleep(1)
Password()


    

