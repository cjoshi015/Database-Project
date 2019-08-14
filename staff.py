import MySQLdb
from tabulate import tabulate


class staff(object):

	def __init__(self):
		self.columnname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Prajakt@22","ROBOCCON" )
		self.cursor = self.db.cursor()


	def fetch(self):
		sql = "desc STAFF"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])


        def display(self):
        	sql = "desc STAFF"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		
                sql = "select * from STAFF"
                self.cursor.execute(sql)
                self.entries = self.cursor.fetchall()
                print tabulate(self.entries, self.columnname, tablefmt='psql')
                self.columname = []

	def register(self):
		stid = raw_input("Enter staff ID:-	")
		sql = "select * from STAFF where STAFF_ID = %s" %('"'+str(stid)+'"')
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		if len(list(self.entries)) != 0:
			print "Volunteer already registered. with id %s"%(str(stid))

		else:
			name = raw_input("Enter name ID:-	")
			department = raw_input("Enter dept ID:-	")
			
			
			sql = "insert into STAFF values(%s,%s,%s);"%(('"'+str(stid)+'"'),('"'+str(name)+'"'),('"'+str(department)+'"'))
			if self.cursor.execute(sql):
			        self.db.commit()
			        print"Sucessfully registered.."
			else:
			        print "Error.."
			        
			        
			 

			

