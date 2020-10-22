
"""

THIS SCRIPT CREATES AND INVOKES TKINTER GUI (MAIN WINDOW)
FOR PARKING MANGEMENT

"""

from tkinter import  *                   # IMPORTING TKINTER LIBRARY CLASSES AND FUNCTIONS 
from tkinter import messagebox           # IMPORTING TKINTER MESSEGEBOX FOR POP UP WARNINGS AND INFO

import sqlite3                           # IMPORTING SQL LITE LIBRARY FOR 
                                         # CLOSING CONNECTION WITH DATABASE WHEN MAIN WINDOW CLOSES 

from login import Login                  # IMPORTING LOGIN SCRIPT TO INVOKE LOGIN WINDOW WHEN PROMPTED


class Gui:                               # CLASS FOR GUI ,WHICH IS CALLED IN MAIN SCRIPT


		def __init__(self):              # CONSTRUCTOR TO INITIALIZE CONNECTION WITH DATABASE 
			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	

			self.main_win()              # INVOKING MAIN GUI WINDOW 

		def call(self):                  # FUNCTION TO INVOKE OR CALL LOGIN WINDOW
			global main_window

			l=Login(main_window,self.user.get()) # CALLING LOGIN CLASS , PASSING MAIN WINDOW OBJECT AND TYPE OF USER DETAILS

		def on_closing(self):                    # FUNCTION TO HANDEL CLOSING WINDOW EVENT 
			global main_window
			if messagebox.askokcancel("Quit", "Do you want to quit?"):   # ASKING USER CONFIRMATION
				self.con.close()	                                     # CLOSSING CONNECTION WITH DATABASE
				main_window.destroy()	                                 # CLOSING MAIN WINDOW

		def main_win(self):              # MAIN WINDOW FUNCTION 
			global main_window
			main_window = Tk()           # CREATING GUI WINDOW
			main_window.title(" Parking Management ") # ASSIGNING WINDOW TITLE

			try:
				main_window.iconbitmap("main_icon.ico") # SETTING WINDOW ICON (PREFERRED FOR WINDOWS SYSTEM)
			except:
				main_window.iconbitmap("@main_icon.xbm") # SETTING WINDOW ICON (PREFERRED FOR LINUX SYSTEM)

					
			main_window.geometry("550x400")              # SETTING GEOMETERY OF WINDOW 

			# MAIN HEADING LABEL      
			l1=Label(main_window, text="PARKING MANAGEMENT AUTHENTICATION", font="Times 15 bold",padx=10, pady=40, bg="red", fg="black")
			l1.grid(row=0,column=0,columnspan=3,padx=30,pady=30) # DISPLAYING LABEL IN WINDOW
			self.user = StringVar(main_window)                   # VARIABLE TO STORE TYPE OF USER LOGGING-IN
			self.user.set("EMPLOYEE")                            # SETTING DEFAULT USER VALUE

			w = OptionMenu(main_window, self.user, "ADMIN", "EMPLOYEE")  # MENU FOR CHOICING TYPE OF USER
			w.config(bg="WHITE",font="Times 20 bold")                    # SETTING BACKGROUNG COLOR AND FONT
			w.grid(row=1,column=0,columnspan=3,padx=30,pady=30,rowspan=2) # DISPLAYING MENU IN WINDOW
			# LOGIN BUTTON 
			# TO INVOKE LOGIN PAGE
			login_button = Button(main_window, text="LOGIN",font="Times 15 bold", bg="white", fg="black", padx=60, pady=10,activebackground="red", command=self.call)
			login_button.grid(row=3, column=0,columnspan=3,padx=30,pady=30,rowspan=2) # DISPLAYING LOGIN BUTTON IN WINDOW
			l1.grid_configure(sticky="nsew")


			main_window.grid_rowconfigure(0, weight=1)  # CONFIGURING MAIN WINDOW FOR FULL SCREEN 
			main_window.grid_columnconfigure(0, weight=1) # CONFIGURING MAIN WINDOW FOR FULL SCREEN 

			main_window.protocol("WM_DELETE_WINDOW",self.on_closing) # CAPTURING CLOSING EVENT

			main_window.mainloop() # LOOP TO WAIT FOR CAPTURING EVENTS AND VALUES OF MAIN WINDOW
		
		                            


		                                             """ END OF SCRIPT """