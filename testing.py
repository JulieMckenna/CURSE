#testing plan

"""
Things to test
1. Log in
    a. Admin login
        i. 30001
            Brack Obama
    b. Instructor Login 
        i. 20001
            Joseph Fourier
    c. Student login
        i. 10001
            Issac Newton
    d. Not in the system log in
        i. 10010 - valid 5 int
        ii. 0225 - not 5 int
2. Log out
    a. make sure it prints log out line before exits program
3. Add class to system
    a. try taken crn
        i. 400001
    b. try crn that isnt correct lenght of numbers
        i. 5000
        ii. 500088
    c. try not valid semester
        i. Winter
    d. try not valid course credits
        i. -1
        ii. 6
    e. add a course
        i. 400008, Comp Sci I, BSCO, Turing, Fall, 9:30, O, 2020, 4
4. Drop class from system
    a. check class is in system before - check it is gone after
        i. 400008
    b. try to remove course that isnt there
        i. 4006
        ii. 400010
5. Add user to system
    a. add student
    b. add instructor
    c. add admin
    d. add none of the above
6. Drop user form system
    a. check that user is in before, check that they are gone after
    b. try to remove student that isnt in the system
7. Search courses
    a. make sure all of the courses display
8. Search courses my parameter
    a. search by meeting time
        i. 8:00
    b. search by meeting day
        i. MW
    c. search by department
        i. HUSS
    d. search by teacher
        i. Fourier
    e. search by class name
        i. English
    f. search for something with no reuslts
        i. Science 
9. Add course - student
10. Drop course - student
11. Assemble print roster 
"""
