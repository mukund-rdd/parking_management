

from tkinter import  *                              # IMPORTING TKINTER LIBRARY CLASSES AND FUNCTIONS 
from tkinter import messagebox                      # IMPORTING TKINTER MESSEGEBOX FOR POP UP WARNINGS AND INFO

import sqlite3                                      # IMPORTING SQL LITE LIBRARY FOR 
                                                    # FETCHING AND STORING VALUES TO DATABASE

import datetime                                     # DATETIME LIBRARY TO FETCH CURRENT DATE AND TIME

from print_invoice import print_bill                # PRINT INVOICE SCRIPT TO SAVE INVOICE AS PDF 

class Employee:                                     #ADMIN CLASS WHICH IS CALLED IN LOGIN SCRIPT
		


		def __init__(self,main_window):             # CONSTRUCTOR TO INITIALIZE CONNECTION WITH DATABASE 
                                                    # AND INTIALIZE VALUES

			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()	

			self.main_window=main_window            # ASSIGNING MAIN WINDOW OBJECT

			self.employee_window()                  # INVOKING EMPLOYEE GUI WINDOW



		def stats(self):                            # FUNCTION TO DISPLAY PARKING STATISTICS 
			global e_window
			stats_window = Toplevel(e_window)       # CREATING GUI WINDOW
												    # DISPLAY WINDOW ON TOP OF MAIN WINDOW

			stats_window.title(" Employee List ")   # ASSIGNING WINDOW TITLE
			try:
				self.main_window.iconbitmap("main_icon.ico") # SETTING WINDOW ICON (PREFERRED FOR WINDOWS SYSTEM)
			except:
				self.main_window.iconbitmap("@main_icon.xbm") # SETTING WINDOW ICON (PREFERRED FOR LINUX SYSTEM)

			self.c.execute("SELECT * ,oid FROM vehicles")     # FETCHING VEHICLE DETAILS FROM DATABASE
			records=self.c.fetchall()
			total_rows = len(records)
			total_columns = len(records[0])
			for r in range(total_rows):
				for c in range(total_columns):
					dis = Entry(stats_window,width=20,fg="blue",font=('Arial',16,'bold'))
					dis.grid(row=r,column=c)
					dis.insert(END,records[r][c])
				
			self.con.commit()         # COMMITING CHANGES TO DATABAS



		def calc_bill(self,o_v,tot_time):           # FUNCTION TO CALCULATE PARKING BILL
			self.amount_payable=0.0
			tot_time=tot_time
			o_v=o_v
			self.c.execute("SELECT *,oid FROM vehicles where vehicle_number=?",(o_v,)) # FETCHING DETAILS FROM DATABASE
			customer_details=self.c.fetchall()
			self.c.execute("SELECT *,oid FROM cost")                                   # FETCHING DETAILS FROM DATABASE
			cost_details=self.c.fetchall()
			
			v_type=customer_details[0][1]
			


			if v_type =='2-WHEELER':
				self.cost_min=str(int(cost_details[0][0])/60)
				self.amount_payable=float(self.cost_min)*float(tot_time[0])
			elif v_type =='4-WHEELER':
				self.amount_payable=float(cost_details[0][1]/60)*float(tot_time[0])
			else:
				error_msg="INVALID VEHICLE TYPE"
			
			self.display_bill(customer_details,self.cost_min,self.amount_payable)      # CALLING DISPLAY BILL FUNCTION 




		
		def print_details(self,oid,c_name,v_type,v_num,c_p_num,tot_time,cost_min,amount_payable):  # FUNCTION TO SEND PARKING BILL DETAILS
		                                                                                           # TO PRINT INVOICE SCRIPT
			global display_window
			amount_payable=self.amount_payable
			cost_min=self.cost_min
			print_bill(oid,c_name,v_type,v_num,c_p_num,tot_time,cost_min,amount_payable)          # PASSING BILL DETAILS TO CREATE INVOICE
			messagebox.showinfo("Print Invoice", "Print Sucessfull \n Saved In Your Program Folder",parent=display_window)






		def display_bill(self,customer_details,cost_min,amount_payable):  # FUNCTION TO DISPLAY PARKING BILL
			self.amount_payable=0.0

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

			# MAIN HEADING LABEL 

			l1 = Label(display_window, text="BILL INVOICE", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

			# SET OF LABELS TO DISPLAY PARKING BILL         
			r1=Label(display_window,text="Customer Name:")       # HERE r- REFERS TO ROW
			r1.grid(row=1,column=0)                              # AND c- REPRESENTS COLUMN
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

			# PRINT BUTTON 
			# TO SAVE BILL DETAILS
			print_button = Button(display_window, text=" PRINT BILL ",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=lambda: self.print_details(oid,c_name,v_type,v_num,c_p_num,tot_time,self.cost_min,self.amount_payable))
			print_button.grid(row=8,column=1,pady=30,ipadx=50)







		def checkout_details(self):                   # FUNCTION IS USED TO UPDATE CHECK-OUT TIME OF A VEHICLE
			
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


			

		def checkout(self):                      # FUNCTION IS USED TO  CHECK-OUT  A VEHICLE
			
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




		def entery_details(self):              # FUNCTION IS USED TO SAVE CHECK-IN TIME AND DETAILS OF A VEHICLE

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

			self.con.commit()  # COMMITING CHANGES TO DATABASE
			
			#CLEARING INPUT FEILDS 
			
			self.customer_name.delete(0,END)
		
			self.vehicle_number.delete(0,END)
			self.customer_phone_number.delete(0,END)
			messagebox.showinfo("Registered", "Entry Sucessfull",parent=check_in_window)
			check_in_window.destroy()         #CLOSING CHECK-IN WINDOW AFTER SAVING VALUES




		def checkin(self):                                 # FUNCTION IS USED TO  CHECK-IN  A VEHICLE
			global e_window,check_in_window
			check_in_window =Toplevel(e_window)
			check_in_window.title(" Entry Page ")
			try:
				self.main_window.iconbitmap("main_icon.ico")
			except:
				self.main_window.iconbitmap("@main_icon.xbm")
			check_in_window.geometry("550x400")

			# MAIN HEADING LABEL 

			l1 = Label(check_in_window, text="CHECK-IN VEHICLE", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30)

			#SET OF ENTRY WIDGETS TO INPUT VALUES
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

			# SET OF LABELS FOR PROMPTING CHECK-IN DETAILS

			customer_name_label=Label(check_in_window,text="Customer Name:")
			customer_name_label.grid(row=1,column=0)
			vehicle_type_label=Label(check_in_window,text="Vehical Type:")
			vehicle_type_label.grid(row=2,column=0)
			vehicle_number_label=Label(check_in_window,text="Vehical Number")
			vehicle_number_label.grid(row=3,column=0)
			customer_phone_number_label=Label(check_in_window,text="Customer Phone Number")
			customer_phone_number_label.grid(row=4,column=0)

			# CHECK-IN BUTTON 
			# TO SAVE CHECK-IN DETAILS

			check_in_button = Button(check_in_window, text=" SUBMIT ",font="Times 15 bold" ,bg="white", fg="black",activebackground="green", command=self.entery_details)
			check_in_button.grid(row=7,column=1,pady=30,ipadx=50)





		def employee_window(self):            # FUNCTION TO INVOKE EMPLOYEE GUI WINDOW
			global e_window
			e_window = Toplevel(self.main_window) # CREATING GUI WINDOW
												  # EMPLOYEE WINDOW ON TOP OF MAIN WINDOW

			e_window.title(" Executive Page ")    # ASSIGNING WINDOW TITLE
			try:
				self.main_window.iconbitmap("main_icon.ico") # SETTING WINDOW ICON (PREFERRED FOR WINDOWS SYSTEM)
			except:
				self.main_window.iconbitmap("@main_icon.xbm") # SETTING WINDOW ICON (PREFERRED FOR LINUX SYSTEM)  

			e_window.geometry("550x400")          # SETTING GEOMETERY OF WINDOW

			# MAIN HEADING LABEL 

			l1 = Label(e_window, text="  WELCOME BACK \n HAVE A GOOD DAY  ", font="Times 20 bold", padx=40, pady=40,bg="blue", fg="black")
			l1.grid(row=0, column=0, columnspan=3, padx=30, pady=30) # DISPLAYING LABEL IN WINDOW

			# CHECK-IN BUTTON 
			# TO CHECK-IN VEHICLE

			check_in_button = Button(e_window, text=" CHECK-IN", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.checkin)
			check_in_button.grid(row=1, column=1)

			# CHECK-OUT BUTTON 
			# TO CHECK-OUT VEHICLE

			check_out_button = Button(e_window, text="CHECK-OUT", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.checkout)
			check_out_button.grid(row=2, column=1)

			# BUTTON TO DISPLAY PARKING STATISTICS 
			stats_button = Button(e_window, text="STATISTICS", bg="white", fg="black", padx=40, pady=20,
									 activebackground="red", command=self.stats)
			stats_button.grid(row=3, column=1)
		