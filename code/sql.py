import mysql.connector
def connect_to_db():
	cnx = mysql.connector.connect(user='balko', password='DHjsKl!!l34', host='192.120.12.220', database='main')
	mycursor = cnx.cursor()
	return cnx, mycursor


def check_user (uName):
	cnx, mycursor = connect_to_db() 
	y = 0
	ret = mycursor.callproc('check_user', [uName, y])
	cnx.close()
	return ret[1]


def add_student ():
	name = input('Name: ')
	cnx, mycursor = connect_to_db() 
	y = 0
	result = mycursor.callproc('add_student', [name])
	cnx.commit()
	print(result)
	cnx.close()

def add_teacher ():
	name = input('Name: ')
	cnx, mycursor = connect_to_db() 
	result = mycursor.callproc('add_teacher', [name])
	cnx.commit()
	print(result)
	cnx.close()


def add_course (uName):
	courseName = input('CourseName: ')

	cnx, mycursor = connect_to_db()
	y = 0
	mycursor.callproc('add_course', [uName,courseName, y])
	cnx.commit()
	for result in mycursor.stored_results():
		print(result.fetchall())
	cnx.close()


def add_registration ():
	uName = input('UserName: ')
	courseId = input('CourseId: ')

	cnx, mycursor = connect_to_db()
	y = 0
	results = mycursor.callproc('add_registration', [uName,courseId, y])
	print('Added '+uName+' to '+str(courseId) +' = '+ str(y))
	cnx.commit()

	print(results)
	cnx.close()

def add_assignment ():
	aName = input('AssignmentName: ')
	courseId = input('CourseId: ')

	cnx, mycursor = connect_to_db()
	y = 0
	results = mycursor.callproc('add_registration', [courseId, aName, y])
	print('Added '+aName+' to '+str(courseId) +' = '+ str(y))
	cnx.commit()
	cnx.close()


def show_users ():
	print('Users:')
	cnx, mycursor = connect_to_db()
	mycursor.execute("SELECT * FROM users")
	for x in mycursor:
		print(x)
	print('')
	cnx.close()
	
def show_courses ():
	print('Courses:')
	cnx, mycursor = connect_to_db()
	mycursor.execute("SELECT * FROM courses")
	for x in mycursor:
		print(x)
	print('')
	cnx.close()


def show_your_courses (u_name):
	cnx, mycursor = connect_to_db()
	y = 0
	mycursor.callproc('courses_teacher', [u_name])
	cnx.commit()
	for result in mycursor.stored_results():
		print(result.fetchall())
	cnx.close()
	cnx.close()


def show_assignments():
	print('assignments:')
	cnx, mycursor = connect_to_db()
	mycursor.execute("SELECT * FROM assignments")
	for x in mycursor:
		print(x)
	print('')
	cnx.close()


def show_registrations():
	print('registrations:')
	cnx, mycursor = connect_to_db()
	mycursor.execute("SELECT * FROM registrations")
	for x in mycursor:
		print(x)
	print('')
	cnx.close()


def show_all_student(uName):
	print('Here are all youre courses and assignments: ')
	cnx, mycursor = connect_to_db()
	res = mycursor.callproc('student_get_data', [uName,])
	cnx.close()
	for result in mycursor.stored_results():
		arr = result.fetchall()
	parse_courses_assignments(arr)

def parse_courses_assignments(arr):
    prev_item = None
    for item in arr:
        if prev_item == None or prev_item[0] != item[0]:
            prev_item = item
            print(item[0]+' '+ str(item[1]))
        print('└─'+item[2]+' '+ str(item[3])+' '+ str(item[4]))
        prev_item = item
			


def show_all():
	show_users()
	show_courses()
	show_registrations()
	show_assignments()