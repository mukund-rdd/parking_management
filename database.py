import sqlite3



class Database:


	
		def __init__(self):

			self.con = sqlite3.connect('app_data.db')
			self.c= self.con.cursor()
			self.initilaize_database()

			

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
													  'login_id':"mukund_rdd",
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
			try:
				self.c.execute("""INSERT INTO vehicles VALUES (
						  :customer_name,
						  :vehicle_type,
						  :vehicle_number,
						  :customer_phone_number,
						  :check_in_time,
						  :check_out_time,
						  :total_min
										)""",
						 {'customer_name':' Customer name ',
						  'vehicle_type':' Vehicle Type ',
						  'vehicle_number':'Vehicle Number',
						  'customer_phone_number':'Phone Number',
						  'check_in_time':'In-Time',
						  'check_out_time':'Out-Time',
						  'total_min':'Total Time'

									})
			except:
				pass	
			self.con.commit()

		


