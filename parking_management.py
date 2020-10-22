

"""

MAIN PYTHON FILE TO INITIALIZE AND RUN

EVERYTHING.

"""

from database import Database    # SCRIPT TO INITIALIZE  DATA BASE AND ASSIGN DEFAULT LOGIN CREDENTIALS
                                 # FOR ADMIN AND EMPLOYEE

from tkinter_win import Gui      # SCRIPT TO INVOKE TKINTER GUI




class Parking:

		def __init__(self):    # CONSTRUCTOR
			self.main()        # CALLING MAIN FUNCTION 

		def main(self):

			dbase=Database() # INITIALIZING DATABASE BY CALLING CONSTRUCTOR OF Database CLASS
			display=Gui()    # INVOKING TKINTER GUI 
			
				
	
Parking()    # CALLING PARKING CLASS 
	