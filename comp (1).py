import MySQLdb
import team
import random
from tabulate import tabulate


class comp(object):

	def __init__(self):
		self.columnname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Prajakt@22","ROBOCCON" )
		self.cursor = self.db.cursor()


	def fetch(self):
		sql = "desc COMPETITION"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		self.columnname=[]


        def display(self):
                sql = "desc COMPETITION"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
                sql = "select * from COMPETITION"
                self.cursor.execute(sql)
                self.entries = self.cursor.fetchall()
                print tabulate(self.entries, self.columnname, tablefmt='psql')
                self.columnname=[]
                sql="delete from COMPETITION"
                self.cursor.execute(sql)
                self.db.commit()
                
                
                
	def register(self):
		s1 = team.team()
		red = []
		blue = []
		arena = ["Balewadi","Pandharpur","Registhan"]
	        teamname = s1.display(1)
		for i in range(len(teamname)):
		        if i%2 == 0:
		                red.append(teamname[i])
		        else:
		                blue.append(teamname[i])
		        
		if len(red) > len(blue):
		        blue.append("BY")
		else:
		        red.append("BY")
			                
		i=0
		j=0
		counter = 1
		while i < len(red) and j < len(blue):
		        
		        sql = "insert into COMPETITION values(%s,%s,%s,%s);"%(('"'+"C 0"+str(counter)+'"'),('"'+str(random.choice(arena))+'"'),('"'+str(red[i])+'"'),('"'+str(blue[j])+'"'))
		        counter+=1
		        i+=1
		        j+=1
		        self.cursor.execute(sql)
		        self.db.commit()
		        
	        print "Fixtures Preapared Successful.."
			        
			        
			        
			 

			

