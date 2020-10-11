from tkinter import  *
import bcrypt
from tkinter import messagebox
import sqlite3
import datetime
from print_invoice import print_bill 
class Parking:



	def __init__(self):

		self.con = sqlite3.connect('app_data.db')
		self.c= self.con.cursor()

		self.initilaize_database()

		self.main_win()

	def initilaize_database(self):

		try:
			self.c.execute("""CREATE TABLE employee (
					  full_name text NOT NULL,
					  email text NOT NULL UNIQUE,
					  phone text NOT NULL UNIQUE,
					  login_ig text NOT NULL UNIQUE,
					  password text NOT NULL
									)""")
		except:
			pass
		
		try:
			self.c.execute("""CREATE TABLE admin (
					  full_name text NOT NULL,
					  email text NOT NULL UNIQUE,
					  phone text NOT NULL UNIQUE,
					  login_ig text NOT NULL UNIQUE,
					  password text NOT NULL
									)""")
		except: 
			pass
		try:
			self.c.execute("""CREATE TABLE cost (
					  cost_2 text,
					  cost_4 text,
					  total_slots text
									  )""")
		except:
			pass
		try:
			self.c.execute("INSERT INTO employee VALUES ( :full_name, :email, :phone_number, :login_id, :password)",
												  {
												  'full_name':"mukund reddy",
												  'email':"mukundlpunest@gmail.com",
												  'phone_number':"9972439176",
												  'login_id':"mukun_rdd",
												  'password':"$2b$12$Yd9x9dym9xO.pVTVUXqmV.2wj/wo/RxsR9XZSvX2htp59A1VQMqwG"

												  })
		except:
			pass

		try:	
			self.c.execute("INSERT INTO admin VALUES ( :full_name, :email, :phone_number, :login_id, :password)",
												  {
												  'full_name':"mukund reddy",
												  'email':"mukundqwert@gmail.com",
												  'phone_number':"9972439176",
												  'login_id':"Admin",
												  'password':"$2b$12$Yd9x9dym9xO.pVTVUXqmV.2wj/wo/RxsR9XZSvX2htp59A1VQMqwG"

												  })
		except:
			pass

		try:
			self.c.execute("INSERT INTO cost VALUES ( :cost_2, :cost_4, :total_slots)",
												  {
												  'cost_2':'20',
												  'cost_4': '40',
												  'total_slots':'20'
												  })
		except:
			pass

		try:
			self.c.execute("""CREATE TABLE vehicles (
					  customer_name text NOT NULL,
					  vehicle_type text NOT NULL ,
					  vehicle_number text NOT NULL UNIQUE,
					  customer_phone_number text NOT NULL UNIQUE,
					  check_in_time timestamp,
					  check_out_time timestamp,
					  total_min timestamp
									)""")
		except:
			pass
		self.con.commit()
	def calc_bill(self,o_v,tot_time):
		self.amount_payable=0.0
		tot_time=tot_time
		o_v=o_v
		self.c.execute("SELECT *,oid FROM vehicles where vehicle_number=?",(o_v,))
		customer_details=self.c.fetchall()
		self.c.execute("SELECT *,oid FROM cost")
		cost_details=self.c.fetchall()
		
		v_type=customer_details[0][1]
		


		if v_type =='2-WHEELER':
			self.cost_min=str(int(cost_details[0][0])/60)
			self.amount_payable=float(self.cost_min)*float(tot_time[0])
		elif v_type =='4-WHEELER':
			self.amount_payable=float(cost_details[0][1]/60)*float(tot_time[0])
		else:
			error_msg="INVALID VEHICLE TYPE"
		
		self.display_bill(customer_details,self.cost_min,self.amount_payable)




	
	def print_details(self,oid,c_name,v_type,v_num,c_p_num,tot_time,cost_min,amount_payable):
		global display_window
		amount_payable=self.amount_payable
		cost_min=self.cost_min
		print_bill(oid,c_name,v_type,v_num,c_p_num,tot_time,cost_min,amount_payable)
		messagebox.showinfo("Print Invoice", "Print Sucessfull \n Saved In Your Program Folder",parent=display_window)






	def display_bill(self,customer_details,cost_min,amount_payable):

		global check_out_window,display_window
		c_name= customer_details[0][0]   
		v_type=customer_details[0][1]
		v_num = customer_details[0][2]
		c_p_num=customer_details[0][3]
		c_in_time=customer_details[0][4]
		c_out_time=customer_details[0][5]
		tot_time=customer_details[0][6]
		oid=customer_details[0][-1]
		self.amount_payable=amount_payable
		
		display_window =Toplevel(check_out_window)
		display_window.title(" Bill Page ")
		display_window.iconbitmap("main_icon.ico")
		display_window.geometry("550x400")

		l1 = Label(display_window, text="BILL INVOICE", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
		l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

		r1=Label(display_window,text="Customer Name:")
		r1.grid(row=1,column=0)
		c1=Label(display_window,text=c_name)
		c1.grid(row=1,column=1)
		r2=Label(display_window,text="Phone Number:")
		r2.grid(row=2,column=0)
		c2=Label(display_window,text=c_p_num)
		c2.grid(row=2,column=1)
		r3=Label(display_window,text="Vehicle Type:")
		r3.grid(row=3,column=0)
		c3=Label(display_window,text=v_type)
		c3.grid(row=3,column=1)
		r4=Label(display_window,text="Vehicle Number:")
		r4.grid(row=4,column=0)
		c4=Label(display_window,text=v_num)
		c4.grid(row=4,column=1)
		r5=Label(display_window,text="Check-in Time:")
		r5.grid(row=5,column=0)
		c5=Label(display_window,text=c_in_time)
		c5.grid(row=5,column=1)
		r6=Label(display_window,text="Check-out Time:")
		r6.grid(row=6,column=0)
		c6=Label(display_window,text=c_out_time)
		c6.grid(row=6,column=1)
		r7=Label(display_window,text="Amount Payable:")
		r7.grid(row=7,column=0)
		c7=Label(display_window,text=self.amount_payable)
		c7.grid(row=7,column=1)

		print_button = Button(display_window, text=" PRINT BILL ",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=lambda: self.print_details(oid,c_name,v_type,v_num,c_p_num,tot_time,self.cost_min,self.amount_payable))
		print_button.grid(row=8,column=1,pady=30,ipadx=50)







	def checkout_details(self):
		
		check_out_time= datetime.datetime.now()
		out_vehicle=self.out_vehicle_number.get()

		self.c.execute("SELECT check_in_time,oid FROM vehicles where vehicle_number=?",(out_vehicle,))
		records=self.c.fetchall()

		
	   
		check_in_time = datetime.datetime.strptime(records[0][0], "%Y-%m-%d %H:%M:%S.%f")
		tot_min=check_out_time-check_in_time

		tot_min =  divmod(tot_min.total_seconds(), 60) 

		self.c.execute("UPDATE vehicles SET check_out_time=?,total_min=? where vehicle_number=?",(check_out_time,tot_min[0],out_vehicle))
		self.con.commit()
		self.calc_bill(out_vehicle,tot_min)


		

	def checkout(self):
		global e_window,check_out_window
		check_out_window =Toplevel(e_window)
		check_out_window.title(" Exit Page ")
		check_out_window.iconbitmap("main_icon.ico")
		check_out_window.geometry("550x400")

		l1 = Label(check_out_window, text="CHECK-OUT VEHICLE", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
		l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
	
		self.out_vehicle_number = Entry(check_out_window,width=30)
		self.out_vehicle_number.grid(row=1,column=1,padx=20)
		
		
		
		out_vehicle_number_label=Label(check_out_window,text="Vehical Number")
		out_vehicle_number_label.grid(row=1,column=0)
		
	
		check_out_button = Button(check_out_window, text=" CHECK-OUT ",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=self.checkout_details)
		check_out_button.grid(row=2,column=1,pady=30,ipadx=50)




	def entery_details(self):

		global check_in_window
		
		self.check_in_time= datetime.datetime.now()

		self.c.execute("INSERT INTO vehicles VALUES ( :customer_name, :vehicle_type,:vehicle_number ,:customer_phone_number, :check_in_time,:check_out_time,:total_min)",
												  {
												  'customer_name':self.customer_name.get(),
												  'vehicle_type':self.vehicle_type.get(),
												  'vehicle_number':self.vehicle_number.get(),
												  'customer_phone_number':self.customer_phone_number.get(),
												  'check_in_time':self.check_in_time,
												  'check_out_time':'0',
												  'total_min':'0'
												  })

		self.con.commit()
		
		
		self.customer_name.delete(0,END)
	
		self.vehicle_number.delete(0,END)
		self.customer_phone_number.delete(0,END)
		messagebox.showinfo("Registered", "Entry Sucessfull",parent=check_in_window)
		check_in_window.destroy()




	def checkin(self):
		global e_window,check_in_window
		check_in_window =Toplevel(e_window)
		check_in_window.title(" Entry Page ")
		check_in_window.iconbitmap("main_icon.ico")
		check_in_window.geometry("550x400")

		l1 = Label(check_in_window, text="CHECK-IN VEHICLE", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
		l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
		self.customer_name = Entry(check_in_window,width=30)
		self.customer_name.grid(row=1,column=1,padx=20)
		self.vehicle_type = StringVar(check_in_window)
		self.vehicle_type.set("2-WHEELER")
		self.vehi_type = OptionMenu(check_in_window, self.vehicle_type, "2-WHEELER", "4-WHEELER")
		self.vehi_type.config(bg="WHITE",font="Times 10 bold")
		self.vehi_type.grid(row=2,column=1,padx=20)
		self.vehicle_number = Entry(check_in_window,width=30)
		self.vehicle_number.grid(row=3,column=1,padx=20)
		self.customer_phone_number = Entry(check_in_window,width=30)
		self.customer_phone_number.grid(row=4,column=1,padx=20)
		
		customer_name_label=Label(check_in_window,text="Customer Name:")
		customer_name_label.grid(row=1,column=0)
		vehicle_type_label=Label(check_in_window,text="Vehical Type:")
		vehicle_type_label.grid(row=2,column=0)
		vehicle_number_label=Label(check_in_window,text="Vehical Number")
		vehicle_number_label.grid(row=3,column=0)
		customer_phone_number_label=Label(check_in_window,text="Customer Phone Number")
		customer_phone_number_label.grid(row=4,column=0)
	
		check_in_button = Button(check_in_window, text=" SUBMIT ",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=self.entery_details)
		check_in_button.grid(row=7,column=1,pady=30,ipadx=50)



	def stats(self):
		global e_window
		stats_window = Toplevel(e_window)
		stats_window.title(" Employee List ")
		stats_window.iconbitmap("main_icon.ico")
		self.c.execute("SELECT * ,oid FROM vehicles")
		records=self.c.fetchall()
		total_rows = len(records)
		total_columns = len(records[0])
		for r in range(total_rows):
			for c in range(total_columns):
				dis = Entry(stats_window,width=20,fg="blue",font=('Arial',16,'bold'))
				dis.grid(row=r,column=c)
				dis.insert(END,records[r][c])
			
		self.con.commit()
	def employee_window(self):
		global main_window,e_window
		e_window = Toplevel(main_window)
		e_window.title(" Executive Page ")
		e_window.iconbitmap("main_icon.ico")
		e_window.geometry("550x400")
		l1 = Label(e_window, text="  WELCOME BACK \n HAVE A GOOD DAY  ", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
		l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
		check_in_button = Button(e_window, text=" CHECK-IN", bg="white", fg="black", padx=40, pady=20,
								 activebackground="red", command=self.checkin)
		check_in_button.grid(row=1, column=1)
		check_out_button = Button(e_window, text="CHECK-OUT", bg="white", fg="black", padx=40, pady=20,
								 activebackground="red", command=self.checkout)
		check_out_button.grid(row=2, column=1)
		stats_button = Button(e_window, text="STATISTICS", bg="white", fg="black", padx=40, pady=20,
								 activebackground="red", command=self.stats)
		stats_button.grid(row=3, column=1)
	

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



	def display(self):
		global a_window
		display_window = Toplevel(a_window)
		display_window.title(" Employee List ")
		display_window.iconbitmap("main_icon.ico")
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
		



	def register(self):

		global a_window
		global register_window

		register_window = Toplevel(a_window)
		register_window.title(" Registration Page ")
		register_window.iconbitmap("main_icon.ico")
		register_window.geometry("550x400")

		l1 = Label(register_window, text="EMPLOYEE REGISTRATION", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
		l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)
		self.f_name = Entry(register_window,width=30)
		self.f_name.grid(row=1,column=1,padx=20)
		self.l_name = Entry(register_window,width=30)
		self.l_name.grid(row=2,column=1,padx=20)
		self.email = Entry(register_window,width=30)
		self.email.grid(row=3,column=1,padx=20)
		self.phone_number = Entry(register_window,width=30)
		self.phone_number.grid(row=4,column=1,padx=20)
		self.login_id = Entry(register_window,width=30)
		self.login_id.grid(row=5,column=1,padx=20)
		self.password = Entry(register_window,width=30,show="*")
		self.password.grid(row=6,column=1,padx=20)

		f_name_label=Label(register_window,text="First Name")
		f_name_label.grid(row=1,column=0)
		l_name_label=Label(register_window,text="Last Name")
		l_name_label.grid(row=2,column=0)
		email_label=Label(register_window,text="Email")
		email_label.grid(row=3,column=0)
		phone_number_label=Label(register_window,text="Phone Number")
		phone_number_label.grid(row=4,column=0)
		login_id_label=Label(register_window,text="Login Id")
		login_id_label.grid(row=5,column=0)
		password_label=Label(register_window,text="Password")
		password_label.grid(row=6,column=0)
		
		submit_button = Button(register_window, text=" REGISTER EMPLOYEE",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=self.submit)
		submit_button.grid(row=7,column=1,pady=30,ipadx=50)

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
		park_window.iconbitmap("main_icon.ico")
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


	def admin_window(self):
		global main_window,login_window,a_window
		login_window.destroy()
		a_window = Toplevel(main_window)
		a_window.title(" Admin Page ")
		a_window.iconbitmap("main_icon.ico")
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



	def verify(self):

		#print(self.auth)
		global login_window
		uid=StringVar()
		uid= self.user_name.get()
		pwd=self.password.get().encode("utf-8")
		#print(uid,pwd)
		
		if self.variable.get() == "ADMIN":
			admin_temp={record[0]:record[1] for record in self.con.execute("SELECT login_ig,password from admin") }
			if uid in admin_temp.keys():
				if bcrypt.checkpw(pwd, admin_temp[uid].encode("utf-8")):
					Label(login_window, text="Valid User",font="10").grid(row=6, column=1, padx=10, pady=10)
					login_window.destroy()
					self.admin_window()

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
					self.employee_window()

				else:
					self.result = "Wrong Password"
					Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)

			else:
				self.result = "User Does Not Exist"
				Label(login_window, text=self.result,font="10").grid(row=6, column=1, padx=10, pady=10)
			

	def login(self):
		global main_window,login_window
		login_window = Toplevel(main_window)
		login_window.title(" Login Page ")
		login_window.iconbitmap("main_icon.ico")
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
		


	def main_win(self):
		global main_window
		main_window = Tk()
		main_window.title(" Parking Management ")
		main_window.iconbitmap("main_icon.ico")
		main_window.geometry("550x400")
		l1=Label(main_window, text="PARKING MANAGEMENT AUTHENTICATION", font="Times 15 bold",padx=10, pady=40, bg="red", fg="black")
		l1.grid(row=0,column=0,columnspan=3,padx=30,pady=30)
		self.variable = StringVar(main_window)
		self.variable.set("EMPLOYEE")
		w = OptionMenu(main_window, self.variable, "ADMIN", "EMPLOYEE")
		w.config(bg="WHITE",font="Times 20 bold")
		w.grid(row=1,column=0,columnspan=3,padx=30,pady=30,rowspan=2)
		login_button = Button(main_window, text="LOGIN",font="Times 15 bold", bg="white", fg="black", padx=60, pady=10,activebackground="red", command=self.login)
		login_button.grid(row=3, column=0,columnspan=3,padx=30,pady=30,rowspan=2)
		l1.grid_configure(sticky="nsew")


		main_window.grid_rowconfigure(0, weight=1)
		main_window.grid_columnconfigure(0, weight=1)
		main_window.protocol("WM_DELETE_WINDOW",lambda: on_closing(self))
		main_window.mainloop()
	
def on_closing(self):
	global main_window
	if messagebox.askokcancel("Quit", "Do you want to quit?"):
		self.con.close()	
		main_window.destroy()
Parking()    
	