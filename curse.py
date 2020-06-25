#asignment2
import sqlite3

# database file connection 
database = sqlite3.connect("assignment2.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 

class User:
    def __init__(self, fname, lname, uid):
        self.firstname = fname
        self.lastname = lname
        self.id = uid
    def setfName(self,fname):
        self.firstname = fname
    def setLName(self, lname):
        self.lastname = lname
    def setID(self, uid):
        self.id = uid
    def printUser(self):
        print("First name: " + self.firstname +"\tLast name: " + self.lastname + "\tId: " + self.id)
    #all users
    def Login(self, id, usertype):
        cursor.execute("SELECT * FROM STUDENT WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type studnet")
                usertype = 's'
            print(i)
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type instructor")
                usertype = 'i'
            print(i)
        cursor.execute("SELECT * FROM ADMIN WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type admin")
                usertype = 'a'
            print(i)
        return usertype 
    def Logout(self):
        pass
    def SearchAllCourses(self): 
        pass
    def SearchParam(self):
        pass

#student class
class student(User):
    def __init__(self, fname, lname, uid):
        super().__init_(fname, lname, id)
        schedule = [] #save the crns of the courses to list 
    #do 1st
    def addCourse(self):
        pass
    #do 1st
    def dropCourse(self):
        pass
    def printSchedule(self):
        pass

#instructor class
class instructor(User):
    def __init__(self, fname, lname, uid):
        super().__init_(fname, lname, id)
        schedule = [] #save the crns of courses that instructor is teaching
    def printSchedule(self):
        print("print schedule")
    #do 1st
    def printRoster(self):
        print("print roster")
        #for x in schedule:
            #print(schedule[x])
      
#admin class
class admin(User):
    def __init__(self, fname, lname, uid):
        super().__init_(fname, lname, id)
    #do 1st
    def addCourse(self):
        #check for valid crn - not taken by another class
        CRNvalid = False
        while CRNvalid == False:
            crn = input("Enter the CRN")
            cursor.execute("SELECT * FROM COUSRE WHERE CRN=?", (crn,))
            query_result = cursor.fetchall()
            for i in query_result:
                if i != None :
                    print("Not a valid CRN")
                    CRNvalid = False
                else:
                    CRNvalid = True
        Name = input("Enter name of course: \t")
        DEPT = input("Enter course depatment: \t")
        courseInstructor = input("Enter instructor name: \t")
        Time = input("Enter meeting times: \t")
        coursedays = input("Enter meeting days: \t")
        coursesemester = input("Enter class semester: \t")
        courseyear = input("Enter class year: \t")
        credits = input("Enter course credit: \t")
        cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s' );""" % (crn, Name, DEPT, courseInstructor, Time, coursedays, coursesemester, courseyear, credits))
    #do 2nd
    def removeCourser(self):
        pass
    def addUser(self):
        pass
    def removeUser(self):
        pass
    def forceRemoveFromCourse(self):
        pass
    def searchRoster(self):
        pass
    def searchCourse(self):
        pass
    def printRoster(self):
        pass
    def printCourses(self):
        pass

#checks database to see if the userid is in any other user databases(student, instructor, or admin)
def Login(id, usertype):
        cursor.execute("SELECT * FROM STUDENT WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type studnet")
                usertype = 's'
        cursor.execute("SELECT * FROM INSTRUCTOR WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type instructor")
                usertype = 'i'
        cursor.execute("SELECT * FROM ADMIN WHERE ID=?", (userid,))
        query_result = cursor.fetchall()
        for i in query_result:
            if i != None :
                print("type admin")
                usertype = 'a'
        return usertype 

#works
def addCourse():
    #check for valid crn - not taken by another class
    CRNvalid = False
    while CRNvalid == False:
        CRNvalid = True
        crn = input("Enter the CRN")
        cursor.execute("SELECT * FROM COURsE WHERE CRN=?", (crn,))
        query_result = cursor.fetchall()
        for i in query_result:
            print(i)
            if i != None :
                print("Not a valid CRN")
                CRNvalid = False
    Name = input("Enter name of course: \t")
    DEPT = input("Enter course depatment: \t")
    #query for available instructors
    cursor.execute("""SELECT INSTRUCTOR.NAME, INSTRUCTOR.SURNAME, INSTRUCTOR.DEPT FROM INSTRUCTOR
WHERE INSTRUCTOR.DEPT =?""", (DEPT,))
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i)
    courseInstructor = input("Enter instructor name from list above: \t")
    Time = input("Enter meeting times: \t")
    coursedays = input("Enter meeting days: \t")
    coursesemester = input("Enter class semester: \t")
    courseyear = input("Enter class year: \t")
    coursecredits = input("Enter course credit: \t")
    cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s' );""" % (crn, Name, DEPT, courseInstructor, Time, coursedays, coursesemester, courseyear, coursecredits))

#works
def removeCourse():
    #remove based on crn
    #print courses - display all so admin can see what courses there are
    print("Entire Course table")
    cursor.execute("""SELECT * FROM COURSE""")
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i)
    removecrn =input("What is the CRN of the course you would like to remove?")
    cursor.execute("DELETE FROM COURSE WHERE CRN=?", (removecrn, ))
def addUser():
    table = input("What type of user would you like to add?\n1. Student\t2. Instructor\t3. Admin \n")
    if table == 1:
        uid = input("Enter Studnet ID")
        ufname = input("Enter Student first name")
        ulname = input("Enter Student Last name")
        ugradyear = input("Enter the Student's grad year")
        umajor = input("Enter the students major")
        uemail = input("Enter the studnets email")
        cursor.execute("""INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s','%s','%s' );""" % (uid, ufname, ulname, ugradyear, umajor, uemail))
    else:
        print("Not a valid table name")
    
#menu
usertype = ''
print("Welcome to CURSE databases")
userid = input("Enter your ID to login: \t")
usertype = Login(userid,usertype)
print(usertype)
if usertype == 's':
    #student
    print("Welcome to the student portion")
    #print("Please enter your first name, last name, and id number")
    while True:
        choice = int(input("What would you like to do?\n1. Search courses\n2. Add course\n3. Drop course\n4. Print schedule\n5. Exit\n"))
        if choice == 1:
            #search course
            print("Search course:\n")
        elif choice == 2:
            #add course
            print("Adding a course:\n")
        elif choice == 3:
            #drop course
            print("Dropping a course:\n")
        elif choice == 4:
            #print schedule
            print("Printing schedule:\n")
        elif choice == 5:
            #exit
            print("Exiting")
            exit()
        else:
            print("That is not an allowed option.\n")
elif usertype == 'i':
    print("Welcome to the instructor portion.")
    while True:
        choice = int(input("What would you like to do?\n1. Print Schedule\n2. Print Rosters\n3. Search courses\n4. Exit\n"))
        if choice == 1:
            #print schedule
            print("Printing schedule:\n")
        elif choice == 2:
            #print rosters
            print("Printing rosters:\n")
        elif choice == 3:
            #search courses
            print("Searching courses:\n")
        elif choice == 4:
            #exit
            print("Exiting")
            exit()
        else:
            print("That is not an allowed option")
if usertype == 'a':
    #admin section
    print("Welcome to the admin portion.")
    while True:
        choice = int(input("What would you like to do?\n1. Add course to the system\n2. Remove course from system\n3. Add user\n4. Remove user\n5. Force student out of a course/roster\n6. Search course\n7. Search Roster\n8. Print courses\n9. Print rosters\n10. Exit\n"))
        print(choice)
        if choice == 1 :
            #add course
            print("Add a course to the system:\n")  
            addCourse()
            #used to checking purposes
            #print("Entire Course table")
            #cursor.execute("""SELECT * FROM COURSE""")
            #query_result = cursor.fetchall()
  
            #for i in query_result:
	        #    print(i) 
        elif choice == 2 :
            #remove a course
            print("remove a course from the system:\n")
            removeCourse()
            #used for checking purposes
            #print("Entire Course table")
            #cursor.execute("""SELECT * FROM COURSE""")
            #query_result = cursor.fetchall()
  
            #for i in query_result:
	        #    print(i) """
        elif choice == 3:
            #add user
            print("Add a user:\n")
        elif choice == 4:
            #remove a user
            print("Remove a user:\n")
        elif choice == 5:
            #force a student out of a class
            print("Force a student out of a class/roster")
        elif choice == 6:
            #search course
            print("Search for a course:\n")
        elif choice == 7:
            #search roster
            print("Search for a roster:\n")
        elif choice == 8:
            #print courses
            print("Print courses:\n")
        elif choice == 9:
            #print rosters
            print("Print rosters:\n")
        elif choice == 10:
            print("Exiting")
            database.commit() 
            database.close() 
            exit()
        else:
            print("That is not an allowed option")
else:
    print("That is not an allowed user type")


print("What would you like to do?\t1. Search\t2. Insert data\t3. Print\t4. Create a table\t5. Update table\t6. Remove Table")
choice = int(input())
if choice == 1:
    #search
    print("Searching")
elif choice == 2:
    #insert
    print("Insert")
    table = input("What table would you like to insert into?\n1. Student\t2. Instructor\t3. Admin\t4. Course")
    if table == 1:
        uid = input("Enter Studnet ID")
        ufname = input("Enter Student first name")
        ulname = input("Enter Student Last name")
        ugradyear = input("Enter the Student's grad year")
        umajor = input("Enter the students major")
        uemail = input("Enter the studnets email")
        cursor.execute("""INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s','%s','%s' );""" % (uid, ufname, ulname, ugradyear, umajor, uemail))
    else:
        print("Not a valid table name")
elif choice == 3:
    #print all
    tableprint = input("What table do you wnat to print?")
    # QUERY FOR ALL
    print("Entire Admin table")
    print(tableprint)
    print("SELECT * FROM",(tableprint))
    cursor.execute("""SELECT * FROM""",(tableprint))
    query_result = cursor.fetchall()
  
    for i in query_result:
        print(i)
elif choice == 4:
    #create table
    print("create table")
elif choice == 5:
    #update table
    print("update table")
elif choice == 6:
    #remove table
    tablename = input("What table would you like to remove?")
    cursor.execute("""DROP TABLE %s""", (tablename))
else:
    print("Not a valid option")


cursor.execute("""PRAGMA table_info(STUDENT)""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

#printing tables
# QUERY FOR ALL
print("Entire Student table")
cursor.execute("""SELECT * FROM STUDENT""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

# QUERY FOR ALL
print("Entire Instructor table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

# QUERY FOR ALL
print("Entire Admin table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

print("Entire Course table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)



# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 
