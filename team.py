import MySQLdb
from tabulate import tabulate


class team(object):

	def __init__(self):
		self.columnname = []
		self.teamname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Prajakt@22","ROBOCCON" )
		self.cursor = self.db.cursor()


	def fetch(self):
		sql = "desc TEAM"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		self.columname = []

        def display(self,flag):
        	if flag == 0:
                	sql = "desc TEAM"
			self.cursor.execute(sql)
			self.entries = self.cursor.fetchall()
			for x in self.entries:
				self.columnname.append(x[0])
		
        	        sql = "select * from TEAM"
        	        self.cursor.execute(sql)
        	        self.entries = self.cursor.fetchall()
        	        print tabulate(self.entries, self.columnname, tablefmt='psql')
        	        for x in self.entries:
        	                self.teamname.append(x[1])
        	        self.columname = []
        	                
        	        return self.teamname
        	else:
        		sql = "desc TEAM"
			self.cursor.execute(sql)
			self.entries = self.cursor.fetchall()
			for x in self.entries:
				self.columnname.append(x[0])
		
        	        sql = "select * from TEAM"
        	        self.cursor.execute(sql)
        	        self.entries = self.cursor.fetchall()
        	        for x in self.entries:
        	                self.teamname.append(x[1])
        	        self.columname = []
        	                
        	        return self.teamname

	def register(self):
		tid = raw_input("Enter team ID:-	")
		sql = "select * from TEAM where TEAM_ID = %s" %('"'+str(tid)+'"')
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		if len(list(self.entries)) != 0:
			print "TEAM already registered. with id %s"%(str(tid))

		else:
			name = raw_input("Enter name ID:-	")
			college = raw_input("Enter college ID:-	")
			
			
			sql = "insert into TEAM values(%s,%s,%s);"%(('"'+str(tid)+'"'),('"'+str(name)+'"'),('"'+str(college)+'"'))
			if self.cursor.execute(sql):
			        self.db.commit()
			        print"Sucessfully registered.."
			else:
			        print "Error.."
			        
			        
			 

			

