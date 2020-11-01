

from tkinter import  *                  # IMPORTING TKINTER LIBRARY CLASSES AND FUNCTIONS 
from tkinter import messagebox          # IMPORTING TKINTER MESSEGEBOX FOR POP UP WARNINGS AND INFO

import bcrypt                           # IMPORTING BYCRYPT LIBRARY WHICH USED TO SAVE PASSWORDS SAFELY
import sqlite3                          # IMPORTING SQL LITE LIBRARY FOR 
                                        # FETCHING VALUES FROM DATABASE

from admin_win import Admin             # IMPORTING ADMIN WINDOW SCRIPT TO INVOKE ADMIN WINDOW WHEN PROMPTED

from employee_win import Employee       # IMPORTING EMPLOYEE WINDOW SCRIPT TO INVOKE EMPLOYEE WINDOW WHEN PROMPTED

class Login:
		


		def __init__(self,main_window,user):      # CONSTRUCTOR TO INITIALIZE CONNECTION WITH DATABASE 
                                                  # AND INTIALIZE VALUES
			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	
			self.main_window=main_window          # ASSIGNING MAIN WINDOW OBJECT
			self.user=user
			self.login()                          # INVOKING LOGIN GUI WINDOW 



		def verify(self):                         # FUNCTION TO VERIFY USER DETAILS

			global login_window
			uid=StringVar()
			uid= self.user_name.get()             # FETCHING USER ID
			pwd=self.password.get().encode("utf-8")  # FETCHING PASSWORD AND ENCODING IT INTO UTF-8 FORMAT


			
			# VERIFYING USER DETAILS

			if self.user == "ADMIN":  

			    # FETCHING ADMIN RECORDS
				admin_temp={record[0]:record[1] for record in self.con.execute("SELECT login_ig,password from admin") }

				if uid in admin_temp.keys():
					if bcrypt.checkpw(pwd, admin_temp[uid].encode("utf-8")): # CHECKING CRYPTED PASSWORD 
						Label(login_window, text="Valid User",font="10").grid(row=6, column=1, padx=10, pady=10)
						login_window.destroy()
						a=Admin(self.main_window)  # INVOKING ADMIN WINDOW

					else:
						self.result = "Wrong Password"
						Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)

				else:
					self.result = "User Does Not Exist"
					Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)
			else:

				# FETCHING ADMIN RECORDS

				emp_temp={record[0]:record[1] for record in self.con.execute("SELECT login_ig,password from employee") }

				if uid in emp_temp.keys():
					if bcrypt.checkpw(pwd, emp_temp[uid]): # CHECKING CRYPTED PASSWORD 
						Label(login_window, text="Valid User",font="10").grid(row=6, column=1, padx=10, pady=10)
						login_window.destroy()
						e=Employee(self.main_window)  # INVOKING EMPLOYEE WINDOW

					else:
						self.result = "Wrong Password"
						Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)

				else:
					self.result = "User Does Not Exist"
					Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)
				




		def login(self):                                  # FUNCTION TO INVOKE LOGIN GUI WINDOW

			global login_window

			login_window = Toplevel(self.main_window)    # CREATING GUI WINDOW
														 # LOGIN WINDOW ON TOP OF MAIN WINDOW

			login_window.title(" Login Page ")           # ASSIGNING WINDOW TITLE

			try:
				self.main_window.iconbitmap("main_icon.ico") # SETTING WINDOW ICON (PREFERRED FOR WINDOWS SYSTEM)
			except:
				self.main_window.iconbitmap("@main_icon.xbm") # SETTING WINDOW ICON (PREFERRED FOR LINUX SYSTEM)

			login_window.geometry("550x400")                  # SETTING GEOMETERY OF WINDOW

            # MAIN HEADING LABEL  
			l1 = Label(login_window, text="   LOGIN   ", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30) # DISPLAYING LABEL IN WINDOW

            # SET OF LABELS AND ENTERY TO INPUT USER DETAILS

			l2=Label(login_window, text="User Name: ")
			l2.grid(row=1, column=0, padx=10, pady=10)
			self.user_name=StringVar()
			id=Entry(login_window, textvariable=self.user_name)
			id.grid(row=2, column=0, padx=10, pady=10)
			l3=Label(login_window, text="Password: ")
			l3.grid(row=3, column=0, padx=10, pady=10)
			self.password = StringVar()
			pwd=Entry(login_window, textvariable=self.password,show='*')
			pwd.grid(row=4, column=0, padx=10, pady=10)
			
			# LOGIN BUTTON 
			# TO VERIFY USER DETAILS AND INVOKE RESPECTIVE PAGES 
			login_button = Button(login_window, text="   LOGIN   ", bg="white", fg="black", padx=60, pady=20,activebackground="red", command=self.verify)
			login_button.grid(row=5, column=0, padx=10, pady=10)

			# CONFIGURING LABELS FOR FULL SCREEN

			l1.grid_configure(sticky="nsew")
			l2.grid_configure(sticky="nsew")
			l3.grid_configure(sticky="nsew")

			# CONFIGURING MAIN WINDOW FOR FULL SCREEN 

			login_window.grid_rowconfigure(0, weight=1)
			login_window.grid_columnconfigure(0, weight=1)

			# LOOP TO WAIT FOR CAPTURING EVENTS AND VALUES OF LOGIN WINDOW

			login_window.mainloop()
"""		
		                            


		                                                  END OF SCRIPT             """		