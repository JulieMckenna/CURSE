import filecmp

check = input("Checking against which template?(s = student, i = instructor, a = admin, v = invalid): ")
if check == 's':
    result = filecmp.cmp('result.txt', 'testStudentResults.txt')
    if result == True:
        print("Results consistent with template.")
    if result == False:
        print("Results inconsistent with template. Whatever was changed don't commit it.")
if check == 'i':
    result = filecmp.cmp('result.txt', 'testInstructorResults.txt')
    if result == True:
        print("Results consistent with template.")
    if result == False:
        print("Results inconsistent with template. Whatever was changed don't commit it.")
if check == 'a':
    result = filecmp.cmp('result.txt', 'testAdminResults.txt')
    if result == True:
        print("Results consistent with template.")
    if result == False:
        print("Results inconsistent with template. Whatever was changed don't commit it.")
if check == 'v':
    result = filecmp.cmp('result.txt', 'testInvalidResults.txt')
    if result == True:
        print("Results consistent with template.")
    if result == False:
        print("Results inconsistent with template. Whatever was changed don't commit it.")