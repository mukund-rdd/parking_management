
from tkinter import  *
from tkinter import messagebox
import sqlite3
import bcrypt
import re
class Admin:
		


		def __init__(self,main_window):

			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	
			self.main_window=main_window
			self.admin_window()

		def save_details(self):

			global park_window

			self.c.execute("""UPDATE cost SET cost_2 = ? ,cost_4 = ?,total_slots = ?""",(self.cost_2.get(),self.cost_4.get(),self.total_slots.get()))

			self.con.commit()
			
			
			self.cost_2.delete(0,END)
			self.cost_4.delete(0,END)
			self.total_slots.delete(0,END)
		
			messagebox.showinfo("Registered", "Details Saved sucessfull",parent=park_window)
			park_window.destroy()




		def park_details(self):
			global a_window
			global park_window

			park_window = Toplevel(a_window)
			park_window.title(" Parking Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			park_window.geometry("550x400")

			l1 = Label(park_window, text="PARKING DETAILS", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
			
	 
			self.cost_2 = Entry(park_window,width=30)
			self.cost_2.grid(row=1,column=1,padx=20)


			self.cost_4 = Entry(park_window,width=30)
			self.cost_4.grid(row=3,column=1,padx=20)

			self.total_slots = Entry(park_window,width=30)
			self.total_slots.grid(row=5,column=1,padx=20)


			cost2_label=Label(park_window,text="2-WEELER Cost in Rs\nfor 1 hr or 60 min:")
			cost4_label=Label(park_window,text="4-WHEELER Cost in Rs\nfor 1 hr or 60 min:")
			total_solts_label=Label(park_window,text="Total Slots Available:")
		  
			cost2_label.grid(row=1,column=0,rowspan=2)
			cost4_label.grid(row=3,column=0,rowspan=2)
			total_solts_label.grid(row=5,column=0)

			save_cost_button = Button(park_window, text="SAVE PARKING DETAILS", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.save_details)
			save_cost_button.grid(row=6, column=1)

		def display(self):
			global a_window
			display_window = Toplevel(a_window)
			display_window.title(" Employee List ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			self.c.execute("SELECT * ,oid FROM employee")
			records=self.c.fetchall()
			total_rows = len(records)
			total_columns = len(records[0])
			for r in range(total_rows):
				i=0
				for c in [-1,0,2,3]:
					dis = Entry(display_window,width=20,fg="blue",font=('Arial',16,'bold'))
					dis.grid(row=r,column=i)
					dis.insert(END,records[r][c])
					i+=1
			self.con.commit()

		

		def submit(self):
		
			global register_window
			
			self.hash_password =bcrypt.hashpw(str(self.password.get()).encode("utf-8"),bcrypt.gensalt())

			self.c.execute("INSERT INTO employee VALUES ( :full_name, :email, :phone_number, :login_id, :password)",
													  {
													  'full_name':self.f_name.get()+ " " + self.l_name.get(),
													  'email':self.email.get(),
													  'phone_number':self.phone_number.get(),
													  'login_id':self.login_id.get(),
													  'password':self.hash_password

													  })

			self.con.commit()
			
			
			self.f_name.delete(0,END)
			self.l_name.delete(0,END)
			self.email.delete(0,END)
			self.phone_number.delete(0,END)
			self.login_id.delete(0,END)
			self.password.delete(0,END)
			messagebox.showinfo("Registered", "Employee Registration sucessfull",parent=register_window)
			register_window.destroy()	
			



		def validate_name(self,name):
			global register_window
			if name.isalpha():
				return True
			elif name == "":
				return True
			else:
				messagebox.showinfo("Validation", "Only Alphabets are allowed for Name",parent=register_window)
				return False

		def validate_number(self,number):
			global register_window
			if number.isdigit():
				return True
			elif number == "":
				return True
			else:
				messagebox.showinfo("Validation", "Only Digits are allowed for Phone Number",parent=register_window)
				return False


		def validate_mail(self,mail):
			global register_window
			if len(mail) > 7 :
				if re.match("^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[_a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$",mail) != None:
					return True
				else :
					messagebox.showinfo("Validation", "This is not a valid email address",parent=register_window)
					return False

			else :
				messagebox.showinfo("Validation", "This is not a valid email address",parent=register_window)
				return False


		def validate_all(self):

			global register_window
			if self.f_name.get() == "":
				messagebox.showinfo("Validation", "Please Enter First Name To Proceed",parent=register_window)
			elif self.l_name.get() == "":
				messagebox.showinfo("Validation", "Please Enter Last Name To Proceed",parent=register_window)
			elif self.phone_number.get() == "":
				messagebox.showinfo("Validation", "Please Enter phone Number To Proceed",parent=register_window)
			elif len(self.phone_number.get()) !=10:
				messagebox.showinfo("Validation", "Please Enter 10 Digit phone Number ",parent=register_window)
			elif self.email.get() == "":
				messagebox.showinfo("Validation", "Please Enter Email To Proceed",parent=register_window)
			elif self.login_id.get() == "":
				messagebox.showinfo("Validation", "Please Enter Login Id To Proceed",parent=register_window)
			elif self.password.get() == "" or self.cpassword.get() == "":
				messagebox.showinfo("Validation", "Please Enter Password To Proceed",parent=register_window)
			elif self.password.get() != self.cpassword.get():
				messagebox.showinfo("Validation", "Password Miss Match",parent=register_window)
			
			elif self.email.get() != "":
				status=self.validate_mail(self.email.get())
				if status:
					self.submit()
			else:
				messagebox.showinfo("Registered", "Employee Registration sucessfull",parent=register_window)


						

			
	

		def register(self):

			global a_window
			global register_window

			register_window = Toplevel(a_window)
			register_window.title(" Registration Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			register_window.geometry("550x400")

			l1 = Label(register_window, text="EMPLOYEE REGISTRATION", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
	
			f_name_label=Label(register_window,text="First Name")
			f_name_label.grid(row=1,column=0)
			l_name_label=Label(register_window,text="Last Name")
			l_name_label.grid(row=2,column=0)
			phone_number_label=Label(register_window,text="Phone Number")
			phone_number_label.grid(row=3,column=0)
			email_label=Label(register_window,text="Email")
			email_label.grid(row=4,column=0)
			login_id_label=Label(register_window,text="Login Id")
			login_id_label.grid(row=5,column=0)
			password_label=Label(register_window,text="Password")
			password_label.grid(row=6,column=0)
			cpassword_label=Label(register_window,text="Confirm Password")
			cpassword_label.grid(row=7,column=0)
			

			self.f_name = Entry(register_window,width=30)
			self.f_name.grid(row=1,column=1,padx=20)
			self.l_name = Entry(register_window,width=30)
			self.l_name.grid(row=2,column=1,padx=20)
			self.phone_number = Entry(register_window,width=30)
			self.phone_number.grid(row=3,column=1,padx=20)
			self.email = Entry(register_window,width=30)
			self.email.grid(row=4,column=1,padx=20)
			self.login_id = Entry(register_window,width=30)
			self.login_id.grid(row=5,column=1,padx=20)
			self.password = Entry(register_window,width=30,show="*")
			self.password.grid(row=6,column=1,padx=20)
			self.cpassword = Entry(register_window,width=30,show="*")
			self.cpassword.grid(row=7,column=1,padx=20)



			valid_name=register_window.register(self.validate_name)
			valid_number=register_window.register(self.validate_number)
			


			self.f_name.config(validate="key",validatecommand=(valid_name,'%P'))
			self.l_name.config(validate="key",validatecommand=(valid_name,'%P'))
			self.phone_number.config(validate="key",validatecommand=(valid_number,'%P'))
		







			submit_button = Button(register_window, text=" REGISTER EMPLOYEE",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=self.validate_all)
			submit_button.grid(row=8,column=1,pady=30,ipadx=50)




		def admin_window(self):
			global login_window,a_window
			a_window = Toplevel(self.main_window)
			a_window.title(" Admin Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			a_window.geometry("550x400")
			l1 = Label(a_window, text="  WELCOME BACK ADMIN!!!!\n HAVE A GOOD DAY  ", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=40, pady=30)
			register_button = Button(a_window, text=" REGISTER EMPLOYEE", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.register)
			register_button.grid(row=1, column=1)
			display_button = Button(a_window, text=" SHOW EMPLOYEE LIST", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.display)
			display_button.grid(row=2, column=1)
			parking_button = Button(a_window, text="EDIT PARKING DETAILS", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.park_details)
			parking_button.grid(row=3, column=1)

