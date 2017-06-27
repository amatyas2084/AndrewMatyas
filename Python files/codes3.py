'''
Author: Andrew Matyas
Date: 2/12


Description:
<summary of this program>
'''
import sqlite3
import os,sys

class Person:

	def __init__(self,first="",last="",bday="",email=""):
		if first == "":
			first = input("Enter person's first name: ")
		if last == "":
			last = input("Enter person's last name: ")
		if bday == "":
			bday = input("Enter person's birthday: ")
		if email == "":
			email = input("Enter person's e-mail: ")
		self.first = first
		self.last = last
		self.bday = bday
		self.email = email
	
	def __repr__(self):
		return self.first+" "+self.last+": "+self.bday+", "+self.email

	@classmethod	
	def read_person(cls,file):
		x = file.readline().strip()
		if not x :
			return False

		first = x
		last = file.readline().strip()
		bday = file.readline().strip()
		email = file.readline().strip()
		return Person(first,last,bday,email)
		
	def write_person(self,wfile):
		wfile.write(self.first +"\n")
		wfile.write(self.last +"\n")
		wfile.write(self.bday +"\n")
		wfile.write(self.email +"\n")
	
def open_persons_db():

	exists = os.path.exists("persons.db")
	db = sqlite3.connect("persons.db")
	db.row_factory = sqlite3.Row
	if exists == False:
		db.execute('CREATE TABLE friends (first TEXT,last TEXT, bday TEXT,email TEXT PRIMARY KEY)')
		db.execute('CREATE TABLE colleagues (first TEXT,last TEXT, bday TEXT,email TEXT PRIMARY KEY)')
	db.commit()
	return db
	
def add_person(person_db,person,friend=True,colleague=False):
	if friend == False and colleague == False:
		print("Warning: " +person.email+ " not added - must be friend or colleague",file=sys.stderr)
		return False
	else:
		if friend == True:
			person_db.execute('INSERT INTO friends(first,last,bday,email) VALUES(?,?,?,?);',(person.first,person.last,person.bday,person.email))
		if colleague == True:
			person_db.execute('INSERT INTO colleagues(first,last,bday,email) VALUES(?,?,?,?);',(person.first,person.last,person.bday,person.email))
		person_db.commit()
		return True

def delete_person(person_db,person):
	person_db.execute('DELETE FROM friends WHERE email = ?;',(person.email,))
	person_db.execute('DELETE FROM colleagues WHERE email = ?;',(person.email,))
	person_db.commit()
	


def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    

    

if __name__ == '__main__':
    main()
