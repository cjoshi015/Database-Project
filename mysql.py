import MySQLdb
import random
import volunteer
import staff
import team
import comp
from tabulate import tabulate

while True:

	choice = input("\n1.Register\n2.Display Records\n3.Fixtures\n4.Exit\n\n>>>  ")
	if choice == 1:
		choice = input("\n1.Team\n2. Volunteer\n3.Staff\n4.Exit\n\n>>>  ")
		if choice ==  1:
		        while True:
		                s = team.team()
		                s.register()
		                choice = raw_input("Add more? [Y/n] ")
		                if choice.lower() == "y":
		                        pass
		                elif choice.lower() == "n":
		                        break
		                else:
		                        print "Please enter valid choice"
	
		elif choice ==  2:
		        while True:
		                s = volunteer.volunteer()
		                s.register()
		                choice = raw_input("Add more? [Y/n] ")
		                if choice.lower() == "y":
		                        pass
		                elif choice.lower() == "n":
		                        break
		                else:
		                        print "Please enter valid choice"	                
	        elif choice ==  3:
		        while True:
		                s = staff.staff()
		                s.register()
		                choice = raw_input("Add more? [Y/n] ")
		                if choice.lower() == "y":
		                        pass
		                elif choice.lower() == "n":
		                        break
		                else:
		                        print "Please enter valid choice"
	        else:
	                print("\nPlease enter a valid choice")
	elif choice == 2:
		choice = input("\n1.Team\n2. Volunteer\n3.Staff\n4.Exit\n\n>>>  ")
		if choice ==  1:
		                s = team.team()
		                s.display(0)

		elif choice ==  2:
		                s = volunteer.volunteer()
		                s.display()
	                
	        elif choice ==  3:
		                s = staff.staff()
		                s.display()
		                
	        else:
	                print("\nPlease enter a valid choice")
	        
	elif choice == 3:
	        s = comp.comp()
	        s.register()
		choice = raw_input("Show Fixtures ? [Y/n] ")
		if choice.lower() == "y":
		        s.display()
		   
		elif choice.lower() == "n":
		        break
		else:
		        print "Please enter valid choice"
	
	elif choice == 4:
		break
		
	else:
		print("\nPlease enter a valid choice")
			
		
