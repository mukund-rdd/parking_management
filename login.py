

from tkinter import  *
from tkinter import messagebox
import bcrypt
import sqlite3
from admin_win import Admin
from employee_win import Employee

class Login:
		


		def __init__(self,main_window,user):

			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	
			self.main_window=main_window
			self.user=user
			self.login()



		def verify(self):

			#print(self.auth)
			global login_window
			uid=StringVar()
			uid= self.user_name.get()
			pwd=self.password.get().encode("utf-8")
			#print(uid,pwd)
			
			if self.user == "ADMIN":
				admin_temp={record[0]:record[1] for record in self.con.execute("SELECT login_ig,password from admin") }
				if uid in admin_temp.keys():
					if bcrypt.checkpw(pwd, admin_temp[uid].encode("utf-8")):
						Label(login_window, text="Valid User",font="10").grid(row=6, column=1, padx=10, pady=10)
						login_window.destroy()
						a=Admin(self.main_window)

					else:
						self.result = "Wrong Password"
						Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)

				else:
					self.result = "User Does Not Exist"
					Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)
			else:
				emp_temp={record[0]:record[1] for record in self.con.execute("SELECT login_ig,password from employee") }
				if uid in emp_temp.keys():
					if bcrypt.checkpw(pwd, emp_temp[uid]):
						Label(login_window, text="Valid User",font="10").grid(row=6, column=1, padx=10, pady=10)
						login_window.destroy()
						e=Employee(self.main_window)

					else:
						self.result = "Wrong Password"
						Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)

				else:
					self.result = "User Does Not Exist"
					Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)
				




		def login(self):
			global login_window
			login_window = Toplevel(self.main_window)
			login_window.title(" Login Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			login_window.geometry("550x400")
			l1 = Label(login_window, text="   LOGIN   ", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
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
			login_button = Button(login_window, text="   LOGIN   ", bg="white", fg="black", padx=60, pady=20,activebackground="red", command=self.verify)
			login_button.grid(row=5, column=0, padx=10, pady=10)
			l1.grid_configure(sticky="nsew")
			l2.grid_configure(sticky="nsew")
			l3.grid_configure(sticky="nsew")
			login_window.grid_rowconfigure(0, weight=1)
			login_window.grid_columnconfigure(0, weight=1)
			login_window.mainloop()
