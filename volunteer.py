import MySQLdb
from tabulate import tabulate


class volunteer(object):

	def __init__(self):
		self.columnname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Prajakt@22","ROBOCCON" )
		self.cursor = self.db.cursor()


	def fetch(self):
		sql = "desc VOLUNTEER"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		self.columname = []
        def display(self):
        	sql = "desc VOLUNTEER"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
                sql = "select * from VOLUNTEER"
                self.cursor.execute(sql)
                self.entries = self.cursor.fetchall()
                print tabulate(self.entries, self.columnname, tablefmt='psql')
                
                self.columname = []

	def register(self):
		volid = raw_input("Enter volunteer ID:-	")
		sql = "select * from VOLUNTEER where VOL_ID = %s" %('"'+str(volid)+'"')
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		if len(list(self.entries)) != 0:
			print "Volunteer already registered. with id %s"%(str(volid))

		else:
			name = raw_input("Enter name ID:-	")
			department = raw_input("Enter dept ID:-	")
			year = raw_input("Enter year ID:-	")
			
			sql = "insert into VOLUNTEER values(%s,%s,%s,%s);"%(('"'+str(volid)+'"'),('"'+str(name)+'"'),('"'+str(department)+'"'),str(year))
			if self.cursor.execute(sql):
			        self.db.commit()
			        print"Sucessfully registered.."
			else:
			        print "Error.."
			        
			        
			 

			

