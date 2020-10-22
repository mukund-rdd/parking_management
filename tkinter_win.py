from tkinter import  *
from tkinter import messagebox

import sqlite3
from login import Login


class Gui:


		def __init__(self):
			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	
			self.main_win()

		def call(self):
			global main_window
			l=Login(main_window,self.user.get())

		def on_closing(self):
			global main_window
			if messagebox.askokcancel("Quit", "Do you want to quit?"):
				self.con.close()	
				main_window.destroy()	

		def main_win(self):
			global main_window
			main_window = Tk()
			main_window.title(" Parking Management ")
			try:
				main_window.iconbitmap("main_icon.ico")
			except:
				main_window.iconbitmap("@main_icon.xbm")
					
			main_window.geometry("550x400")
			l1=Label(main_window, text="PARKING MANAGEMENT AUTHENTICATION", font="Times 15 bold",padx=10, pady=40, bg="red", fg="black")
			l1.grid(row=0,column=0,columnspan=3,padx=30,pady=30)
			self.user = StringVar(main_window)
			self.user.set("EMPLOYEE")
			w = OptionMenu(main_window, self.user, "ADMIN", "EMPLOYEE")
			w.config(bg="WHITE",font="Times 20 bold")
			w.grid(row=1,column=0,columnspan=3,padx=30,pady=30,rowspan=2)
			login_button = Button(main_window, text="LOGIN",font="Times 15 bold", bg="white", fg="black", padx=60, pady=10,activebackground="red", command=self.call)
			login_button.grid(row=3, column=0,columnspan=3,padx=30,pady=30,rowspan=2)
			l1.grid_configure(sticky="nsew")


			main_window.grid_rowconfigure(0, weight=1)
			main_window.grid_columnconfigure(0, weight=1)
			main_window.protocol("WM_DELETE_WINDOW",self.on_closing)
			main_window.mainloop()
		
		