#asignment2
import sqlite3

# database file connection 
database = sqlite3.connect("assignment2.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 


#make a 3rd database - hold crns and user ids - too keep track of what users have been added to what classes
#to do(assign 5)
"""
1. add/remove course form sem schedule - studnet
2. assemble and print course roster
3. add/remove courses from system - done
4. login - done
5. log out
6. search all courses - done
7. search courses based on parameteres - done
8. menu - done
"""

#print functions for all of the tables
def printCourses():
    # QUERY FOR ALL
    print("Entire course table")
    cursor.execute("""SELECT * FROM COURSE""")
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i) 
def printStudents():
    # QUERY FOR ALL
    print("Entire student table")
    cursor.execute("""SELECT * FROM STUDENT""")
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i) 
def printInstructors():
    # QUERY FOR ALL
    print("Entire instructor table")
    cursor.execute("""SELECT * FROM INSTRUCTOR""")
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i) 
def printAdmins():
    # QUERY FOR ALL
    print("Entire admin table")
    cursor.execute("""SELECT * FROM ADMIN""")
    query_result = cursor.fetchall()
    for i in query_result:
	    print(i) 

class User:
    def __init__(self):
       pass
    def setfName(self,fname):
        self.firstname = fname
    def setLName(self, lname):
        self.lastname = lname
    def setID(self, uid):
        self.id = uid
    def printUser(self):
        print("First name: " + self.firstname +"\tLast name: " + self.lastname + "\tId: " + self.id)
    #all user functions
    #checks database to see if the userid is in any other user databases(student, instructor, or admin)
    def Login(self, id, usertype): #works
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
        #create new type of user instance that logged in as?
        return usertype 
    #need to do  
    def Logout(self):
        print("Exiting")
        database.commit() 
        database.close() 
        exit()
    #shows all courses - works
    def SearchAllCourses(self):
        print("Showing all courses")
        printCourses()
    #lets user search by parameter
    def SearchParam(self, param):
        if param == 1:
            #search by class name - done
            searchparm = "%" + str(input("Please enter the class name:\t")) + "%"
            cursor.execute("SELECT * FROM COURSE WHERE NAME LIKE ?", (searchparm,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif param == 2:
            #search by meeting days - done
            searchparm = "%" + str(input("Please enter the meeting days(ex. MW or TR).\nM=Monday\tT=Tuesday\tW=Wednesday\tR=Thursday\tF=Friday\t\O=Online\t")) + "%"
            print(searchparm)
            cursor.execute("SELECT * FROM COURSE WHERE DAYS LIKE ?", (searchparm,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif param == 3:
            #search by meeting times - done
            searchparm = "%" + (input("Please enter the meeting times(start time): \t")) +"%"
            cursor.execute("SELECT * FROM COURSE WHERE TIME LIKE ?", (searchparm,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif param == 4:
            #serach by department/major - done
            searchparm = "%" + str(input("Please enter the major/department name: \t")) + "%"
            cursor.execute("SELECT * FROM COURSE WHERE DEPT LIKE ?", (searchparm,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        elif param == 5:
            #search by instructor - done
            searchparm = "%" + str(input("Please enter the instructor name: \t")) + "%"
            cursor.execute("SELECT * FROM COURSE WHERE INSTRUCTOR LIKE ?", (searchparm,))
            query_result = cursor.fetchall()
            for i in query_result:
                print(i)
        else:
            print("Not a valid parameter to search by")

#student class
class student(User):
    def __init__(self, uid, fname, lname):
        self.id = uid
        self.firstname = fname
        self.lastname = lname
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
    def __init__(self, uid, fname, lname):
        self.id = uid
        self.firstname = fname
        self.lastname = lname
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
    def __init__(self, uid, fname, lname):
        self.id = uid
        self.firstname = fname
        self.lastname = lname
    #do 1st - done
    def addCourse(self):
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
        #check dept make sure 4 chars - save them as uppercase
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
        #make sure only fall, spring, or summer
        coursesemester = input("Enter class semester: \t")
        #must be 4 number year
        courseyear = input("Enter class year: \t")
        #make sure only 4 credits and whole numbers
        coursecredits = input("Enter course credit: \t")
        cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s','%s','%s','%s','%s','%s' );""" % (crn, Name, DEPT, courseInstructor, Time, coursedays, coursesemester, courseyear, coursecredits))
    #do 2nd - done
    def removeCourse(self):
        #remove based on crn 
        #print courses - display all so admin can see what courses there are
        print("Entire Course table")
        cursor.execute("""SELECT * FROM COURSE""")
        query_result = cursor.fetchall()
        for i in query_result:
	        print(i)
        removecrn =input("What is the CRN of the course you would like to remove?")
        cursor.execute("DELETE FROM COURSE WHERE CRN=?", (removecrn, ))
    def addUser(self, table): #done
        #need to create the class instance
        #add error checking - not if already same id, id != 5 num, cant have same emails(check all user tables)
        if table == 's':
            sid = input("Enter studnet's ID - 5 numbers (starts with 1)")
            sfname = input("Enter student's first name")
            slname = input("Enter student's last name")
            sgradyear = input("Enter the student's grad year")
            smajor = input("Enter the student's major")
            semail = input("Enter the studnet's email")
            cursor.execute("""INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s','%s','%s' );""" % (sid, sfname, slname, sgradyear, smajor, semail))
            print("\nYou have enrolled %s %s", sfname, slname)
        elif table == 'i':
            iid = input("Enter instructor's ID -  5 numbers (starts with 1)")
            ifname = input("Enter instructor's first name")
            ilname = input("Enter instructor's Last name")
            ititle = input("Enter the instructor's title")
            iyear = input("What year was the instructor employed?")
            idept = input("Enter the instructor's departemnt?")
            iemail = input("Enter the instructor's email")
            cursor.execute("""INSERT INTO INSTRCUTOR VALUES('%s', '%s', '%s', '%s','%s','%s','%s' );""" % (iid, ifname, ilname, ititle, iyear, idept, iemail))
            print("\nYou have hired instructor %s %s", ifname, ilname)
        elif table == 'a':
            aid = input("Enter admin's ID -  5 numbers (starts with 1)")
            afname = input("Enter admin's first name")
            alname = input("Enter admin's Last name")
            atitle = input("Enter the admin's title")
            aoffice = input("Where is the admin's office?")
            aemail = input("Enter the admin's email")
            cursor.execute("""INSERT INTO INSTRCUTOR VALUES('%s', '%s', '%s', '%s','%s','%s' );""" % (aid, afname, alname, atitle, aoffice, aemail))
            print("\nYou have hired admin %s %s", afname, alname)
        else:
            print("Not a valid user type")
    #done
    def removeUser(self, table):
        if table == 's':
            print("These are the current students in the system.")
            printStudents()
            removeid = input("Please enter the ID of the student you would like to remove.\t")
            cursor.execute("DELETE FROM STUDENT WHERE ID=?", (removeid, ))       
        elif table == 'i':
            print("These are the current instructors in the system.")
            printInstructors()
            removeid = input("Please enter the ID of the instructor you would like to remove.\t")
            cursor.execute("DELETE FROM INSTRUCTOR WHERE ID=?", (removeid, ))  
        elif table == 'a':
            print("These are the current admins in the system.")
            printAdmins()
            removeid = input("Please enter the ID of the admin you would like to remove.\t")
            cursor.execute("DELETE FROM ADMIN WHERE ID=?", (removeid, ))  
        else:
            print("Not a valid table name")
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

#menu
user1 = User()
usertype = ''
print("Welcome to CURSE databases")
userid = input("Enter your ID to login: \t")
usertype = user1.Login(userid,usertype)
print(usertype)
if usertype == 's':
    #student
    print("Welcome to the student portion")
    #getting values from table to create instance of the class
    cursor.execute("""SELECT * FROM STUDENT WHERE ID=?""", (userid,))
    query_result = cursor.fetchall()
    for i in query_result:
        i = str(i).split(',')
        #print(i)
        id = str(i[0]).replace("(","")
        #print(id)
        fname = str(i[1]).replace("'","")
        fname = fname.replace(" ", "")
        #print(fname)
        lname = str(i[2]).replace("'","")
        lname = lname.replace(" ", "")
        #print(lname)
    stud1 = student(id, fname, lname)
    #print("Please enter your first name, last name, and id number")
    while True:
        choice = int(input("What would you like to do?\n1. Search courses\n2. Add course\n3. Drop course\n4. Print schedule\n5. Logout\n"))
        if choice == 1:
            #search course
            print("Search course:\n")
            searchtype = input("Would you like to search by a parameter or not?(y or n)")
            #show all courses -
            if searchtype == 'n': 
                print("Search for a course:\n")
                #go to function
                inst1.SearchAllCourses()
            #show courses based on param
            elif searchtype == 'y':
                #ask for which param - go to function
                param = input("What would you like to search by(Enter number)?\n1. Class Name\t2. Meeting Days\t3. Metting Times\t4. Department\t5. Instructor")
                inst1.SearchParam(int(param))
            else :
                print("Not a valid input")
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
            stud1.Logout()
        else:
            print("That is not an allowed option.\n")
elif usertype == 'i':
    print("Welcome to the instructor portion.")
    #getting values from table to create instance of the class
    cursor.execute("""SELECT * FROM INSTRUCTOR WHERE ID=?""", (userid,))
    query_result = cursor.fetchall()
    for i in query_result:
        i = str(i).split(',')
        #print(i)
        id = str(i[0]).replace("(","")
        #print(id)
        fname = str(i[1]).replace("'","")
        fname = fname.replace(" ", "")
        #print(fname)
        lname = str(i[2]).replace("'","")
        lname = lname.replace(" ", "")
        #print(lname)
    inst1 = instructor(id, fname, lname)
    while True:
        choice = int(input("What would you like to do?\n1. Print Schedule\n2. Print Rosters\n3. Search courses\n4. Logout\n"))
        if choice == 1:
            #print schedule
            print("Printing schedule:\n")
        elif choice == 2:
            #print rosters
            print("Printing rosters:\n")
        elif choice == 3:
            #search courses
            print("Searching courses:\n")
            searchtype = input("Would you like to search by a parameter or not?(y or n)")
            #show all courses -
            if searchtype == 'n': 
                print("Search for a course:\n")
                #go to function
                inst1.SearchAllCourses()
            #show courses based on param
            elif searchtype == 'y':
                #ask for which param - go to function
                param = input("What would you like to search by(Enter number)?\n1. Class Name\t2. Meeting Days\t3. Metting Times\t4. Department\t5. Instructor")
                inst1.SearchParam(int(param))
            else :
                print("Not a valid input")
        elif choice == 4:
            #exit
            inst1.Logout()
        else:
            print("That is not an allowed option")
if usertype == 'a':
    #admin section
    print("Welcome to the admin portion.")
    #getting values from table to create instance of the class
    cursor.execute("""SELECT * FROM ADMIN WHERE ID=?""", (userid,))
    query_result = cursor.fetchall()
    for i in query_result:
        i = str(i).split(',')
        #print(i)
        id = str(i[0]).replace("(","")
        #print(id)
        fname = str(i[1]).replace("'","")
        fname = fname.replace(" ", "")
        #print(fname)
        lname = str(i[2]).replace("'","")
        lname = lname.replace(" ", "")
        #print(alname)
    admin1 = admin(id, fname, lname)
    while True:
        choice = int(input("What would you like to do?\n1. Add course to the system\n2. Remove course from system\n3. Add user\n4. Remove user\n5. Force student out of a course/roster\n6. Search course\n7. Search Roster\n8. Print courses\n9. Print rosters\n10. Logout\n"))
        print(choice)
        if choice == 1 :
            #add course
            print("Add a course to the system:\n")  
            admin1.addCourse()
            #printCourses()
        elif choice == 2 :
            #remove a course
            print("remove a course from the system:\n")
            admin1.removeCourse()
            #used for checking purposes
            #printCouses()
        elif choice == 3:
            #add user
            print("Add a user:\n")
            table = input("What type of user would you like to add?\nStudent(s)\tInstructor(i)\t3. Admin(a)\n")
            admin1.addUser(table)
            #for checking purposes
            if table == 's':
                printStudents()
            elif table == 'i':
                printInstructors()
            elif table == 'a':
                printAdmins()
        elif choice == 4:
            #remove a user
            print("Remove a user:\n")
            table = input("What type of user would you like to remove?\nStudent(s)\tInstructor(i)\t3. Admin(a)\n")
            admin1.addUser(table)
            #for checking purposes
            if table == 's':
                printStudents()
            elif table == 'i':
                printInstructors()
            elif table == 'a':
                printAdmins()
        elif choice == 5:
            #force a student out of a class
            print("Force a student out of a class/roster")
        elif choice == 6:
            #search course
            searchtype = input("Would you like to search by a parameter or not?(y or n)")
            if searchtype == 'n': 
                print("Search for a course:\n")
                #show all courses - go to function
                admin1.SearchAllCourses()
            elif searchtype == 'y':
                #show courses based on param
                #ask for which param - go to function
                param = input("What would you like to search by(Enter number)?\n1. Class Name\t2. Meeting Days\t3. Metting Times\t4. Department\t5. Instructor")
                admin1.SearchParam(int(param))
            else :
                print("Not a valid input")
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
            admin1.Logout()
        else:
            print("That is not an allowed option")
else:
    print("That is not an allowed user type")

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 
