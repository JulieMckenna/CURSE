# FOR TESTING ONLY
import sqlite3
database = sqlite3.connect("curseDatabase.db")
cursor = database.cursor() 

cursor.execute("""DROP TABLE IF EXISTS STUDENT""")
sql_command = """CREATE TABLE STUDENT (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
GRADYEAR	INT 	NOT NULL,
MAJOR		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL)
;"""

cursor.execute(sql_command) 

cursor.execute("""DROP TABLE IF EXISTS INSTRUCTOR""")
sql_command = """CREATE TABLE INSTRUCTOR (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
HIREYEAR	INT 	NOT NULL,
DEPT		CHAR(4) NOT NULL,
EMAIL		text	NOT NULL)
;"""

cursor.execute(sql_command) 

cursor.execute("""DROP TABLE IF EXISTS ADMIN""")
sql_command = """CREATE TABLE ADMIN (  
ID 		INT 	PRIMARY KEY 	NOT NULL,
NAME		TEXT	NOT NULL,
SURNAME		TEXT 	NOT NULL,
TITLE		TEXT 	NOT NULL,
OFFICE		TEXT 	NOT NULL,
EMAIL		text	NOT NULL)
;"""

cursor.execute(sql_command)

cursor.execute("""DROP TABLE IF EXISTS COURSE""")
sql_command = """CREATE TABLE COURSE (  
CRN 		    INT 	PRIMARY KEY 	NOT NULL,
NAME		    TEXT	NOT NULL,
DEPT		    CHAR(4) NOT NULL,
INSTRUCTOR		TEXT 	NOT NULL,
TIME            TIME    NOT NULL,
DAYS            TEXT    NOT NULL,
SEMESTER	    TEXT 	NOT NULL,
YEAR		    INT     NOT NULL,
CREDITS	    	INT     NOT NULL)
;"""

cursor.execute(sql_command)

cursor.execute("""DROP TABLE IF EXISTS ROSTER""")
sql_command = """CREATE TABLE ROSTER (
CRN		INT		NOT NULL,
ID	INT		NOT NULL);
"""

cursor.execute(sql_command) 

# Student list
cursor.execute("""INSERT INTO STUDENT VALUES(10001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(10010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")
cursor.execute("""INSERT INTO STUDENT VALUES(10011, 'Julie', 'McKenna', 2010, 'BSEE', 'mckennaj');""")
cursor.execute("""INSERT INTO STUDENT VALUES(10012, 'Nathan', 'Taylor', 2020, 'BCOS', 'taylorn');""")
cursor.execute("""INSERT INTO STUDENT VALUES(10013, 'Michael', 'LeBlanc', 2020, 'BSEE', 'leblancm4');""")

# Instructor list
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(20008, 'Eliot', 'Mark', 'Full Prof.', 1994, 'HUSS', 'eliotm');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(30001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""") 
cursor.execute("""INSERT INTO ADMIN VALUES(30002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""") 

# Course List
cursor.execute("""INSERT INTO COURSE VALUES(400001, 'English I', 'HUSS', 'Mandela', '10:15', 'TR', 'Fall', 1994, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(400002, 'English II', 'HUSS', 'Mandela', '10:00', 'MW', 'Spring', 1994, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(400003, 'Prosthetics', 'BSME', 'Bernoulli', '1:00', 'TR', 'Summer', 1764, 3);""")
cursor.execute("""INSERT INTO COURSE VALUES(400004, 'Signals & Systems', 'BSEE', 'Fourier', '8:00', 'MTR', 'Fall', 1822, 4)""")
cursor.execute("""INSERT INTO COURSE VALUES(400005, 'CAD', 'ENGR', 'NA', '9:30', 'TR', 'Spring', 2020, 1)""")

print("Entire table")
cursor.execute("""SELECT * FROM STUDENT""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

print("Entire table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

print("Entire table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

print("Entire table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()

for i in query_result:
	print(i)

database.commit() 

database.close() 
