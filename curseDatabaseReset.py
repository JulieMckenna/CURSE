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
cursor.execute("""INSERT INTO STUDENT VALUES(00010001, 'Isaac', 'Newton', 1668, 'BSAS', 'newtoni');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010002, 'Marie', 'Curie', 1903, 'BSAS', 'curiem');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010003, 'Nikola', 'Tesla', 1878, 'BSEE', 'telsan');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010004, 'Thomas', 'Edison', 1879, 'BSEE', 'notcool');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010005, 'John', 'von Neumann', 1923, 'BSCO', 'vonneumannj');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010006, 'Grace', 'Hopper', 1928, 'BCOS', 'hopperg');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010007, 'Mae', 'Jemison', 1981, 'BSCH', 'jemisonm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010008, 'Mark', 'Dean', 1979, 'BSCO', 'deanm');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010009, 'Michael', 'Faraday', 1812, 'BSAS', 'faradaym');""") 
cursor.execute("""INSERT INTO STUDENT VALUES(00010010, 'Ada', 'Lovelace', 1832, 'BCOS', 'lovelacea');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010011, 'Julie', 'McKenna', 2010, 'BSEE', 'mckennaj');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010012, 'Nathan', 'Taylor', 2020, 'BCOS', 'taylorn');""")
cursor.execute("""INSERT INTO STUDENT VALUES(00010013, 'Michael', 'LeBlanc', 2020, 'BSEE', 'leblancm4');""")

# Instructor list
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020001, 'Joseph', 'Fourier', 'Full Prof.', 1820, 'BSEE', 'fourierj');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020002, 'Nelson', 'Mandela', 'Full Prof.', 1994, 'HUSS', 'mandelan');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020004, 'Alan', 'Turing', 'Associate Prof.', 1940, 'BSCO', 'turinga');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020005, 'Katie', 'Bouman', 'Assistant Prof.', 2019, 'BCOS', 'boumank');""") 
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020006, 'Daniel', 'Bernoulli', 'Associate Prof.', 1760, 'BSME', 'bernoullid');""")
cursor.execute("""INSERT INTO INSTRUCTOR VALUES(00020008, 'Eliot', 'Mark', 'Full Prof.', 1994, 'HUSS', 'eliotm');""")

# Admin list
cursor.execute("""INSERT INTO ADMIN VALUES(00030001, 'Barack', 'Obama', 'President', 'Dobbs 1600', 'obamab');""") 
cursor.execute("""INSERT INTO ADMIN VALUES(00030002, 'Malala', 'Yousafzai', 'Registrar', 'Wentworth 101', 'yousafzaim');""") 

cursor.execute("""INSERT INTO COURSE VALUES(400001, 'English I', 'HUSS', 'Mandela', '10:15', 'T & R', 'Fall', 1994, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(400002, 'English II', 'HUSS', 'Mandela', '10:00', 'M & W', 'Spring', 1994, 4);""")
cursor.execute("""INSERT INTO COURSE VALUES(400003, 'Prosthetics', 'BSME', 'Bernoulli', '1:00', 'T & R', 'Summer', 1764, 3);""")
cursor.execute("""INSERT INTO COURSE VALUES(400004, 'Signals & Systems', 'BSEE', 'Fourier', '8:00', 'M, T & R', 'Fall', 1822, 4)""")
cursor.execute("""INSERT INTO COURSE VALUES(400005, 'CAD', 'ENGR', 'NA', '9:30', 'T & R', 'Spring', 2020, 1)""")

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
