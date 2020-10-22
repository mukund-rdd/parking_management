
from tkinter import  *
from tkinter import messagebox
import sqlite3
import datetime
from print_invoice import print_bill 

class Employee:
		


		def __init__(self,main_window):

			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	
			self.main_window=main_window
			self.employee_window()
		def stats(self):
			global e_window
			stats_window = Toplevel(e_window)
			stats_window.title(" Employee List ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
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
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
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
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
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
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
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





		def employee_window(self):
			global e_window
			e_window = Toplevel(self.main_window)
			e_window.title(" Executive Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
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
		