#Adrian Adborn, Viktor Listi
import mysql.connector

# Backend functions ------------------------------------------------------------------------------


def connect_to_db():
	cnx = mysql.connector.connect(user='balko', password='DHjsKl!!l34', host='192.120.12.220', database='main')
	mycursor = cnx.cursor()
	return cnx, mycursor


def check_user (user_name):
	cnx, mycursor = connect_to_db() 
	y = 0
	try:
		ret = mycursor.callproc('check_user', [user_name, y])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	cnx.close()
	return ret[1]


# Admin actions ------------------------------------------------------------------------------
 
    #Functions
        #show_users - shows all users and their role
		#check_user - Shows information about a user
		#add_student - adds a student user
		#remove_student - removes a student user
		#add_teacher - adds a teacher user
		#remove_teacher - removes a teacher user

def show_users ():
	cnx, mycursor = connect_to_db()
	print('Users:')

	try:
		mycursor.execute("SELECT * FROM users")
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	for x in mycursor:
		print(x)
	print('')
	cnx.close()
	return 0


def add_student ():
	name = input('Name: ')
	cnx, mycursor = connect_to_db() 

	try:
		result = mycursor.callproc('add_student', [name])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0


def add_teacher ():
	name = input('Name: ')
	cnx, mycursor = connect_to_db()
	
	try:
		result = mycursor.callproc('add_teacher', [name])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0

	
def remove_user():
	cnx, mycursor = connect_to_db()
	user_name = input('user name: ')

	try:
		mycursor.callproc('remove_user', [user_name])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0


# Teacher actions ------------------------------------------------------------------------------
 
    #Functions
        #show_your_courses - 
		#show_students - 
		#add_course - 
		#remove_course -
		#add_assignment - 
		#remove_assignment - 
		#add_registration - 
		#remove_registration -
		#add_grade -


def show_your_courses(u_name):
	cnx, mycursor = connect_to_db()
	try:
		mycursor.callproc('courses_teacher', [u_name])
		for result in mycursor.stored_results():
			courses = result.fetchall()
		print("Id"+ "| " + "Name" + "       " + "Hp")
		for i in courses:
			print(str(i[1]) + " | " + i[0] + "   | " + str(i[2]))
			print("  └─ Assignments")
			mycursor.callproc('assignments_course', [i[0]])
			for result in mycursor.stored_results():
				assignments = result.fetchall()
			for a in assignments:
				print("  "+str(a[1]) + " | " + a[0] + "   | " + str(a[2]))
	except mysql.connector.Error as e:
		print("Something went wrong... Try again later or contact the administrator: {}".format(e))
		cnx.close()
		return 1

	cnx.close()
	return 0


def show_students():
	cnx, mycursor = connect_to_db()
	print('Users:')

	try:
		mycursor.callproc('show_students', [])
	except mysql.connector.Error as e:
		print("Something went wrong... Try again later or contact the administrator{}".format(e))
		cnx.close()
		return 1
	
	for result in mycursor.stored_results():
		print(result.fetchall())
	print('')
	cnx.close()
	return 0


def add_course (user_name):
	course_name = input('CourseName: ')
	cnx, mycursor = connect_to_db()
	y = 0

	try:
		mycursor.callproc('add_course', [user_name,course_name,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	for result in mycursor.stored_results():
		print(result.fetchall())
	cnx.close()
	return 0


def remove_course ():
	cnx, mycursor = connect_to_db()

	courseName = input('Course Name: ')

	try:
		mycursor.callproc('remove_course', [courseName,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0


def add_assignment ():
	cnx, mycursor = connect_to_db()

	aName = input('Assignment Name: ')
	courseId = input('Course Id: ')
	hp = input("How many hp is the assignment? ")

	try:
		results = mycursor.callproc('add_assignment', [courseId, aName, hp,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	print('Added '+aName+' to course '+str(courseId) +' hp = '+ str(hp))
	cnx.commit()
	cnx.close()
	return 0


def remove_assignment ():
	cnx, mycursor = connect_to_db()

	assignment_name = input('Assignment Name: ')
	course_name = input('Course Name: ')
	
	try:
		mycursor.callproc('remove_assignment', [assignment_name,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0


def add_registration ():
	cnx, mycursor = connect_to_db()

	user_name = input('User Name: ')
	courseId = input('Course Name: ')
	
	try:
		results = mycursor.callproc('add_registration', [user_name,courseId,0])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	print('Added '+user_name+' to course '+str(courseId))
	cnx.commit()
	cnx.close()
	return 0


def remove_registration ():
	user_name = input('User Name: ')
	courseId = input('Course name: ')
	cnx, mycursor = connect_to_db()

	try:
		results = mycursor.callproc('remove_registration', [courseId, user_name])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	print('Removed '+user_name+' from course '+str(courseId))
	cnx.commit()
	cnx.close()
	return 0


def change_grade():
	cnx, mycursor = connect_to_db()

	user_name = input('Students username: ')
	assignment_id = input('AssignmentId: ')
	grade = input("Grade(1 for U and 2 for G): ")
	
	try:
		mycursor.callproc('change_grade', [user_name, assignment_id, grade,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	cnx.commit()
	cnx.close()
	return 0
	

#Student actions ------------------------------------------------------------------------------
 
    #Functions
        #show_all_student - 
		#show_users - 


def show_all_student(user_name):
	print('Here are all youre courses and assignments: ')
	cnx, mycursor = connect_to_db()

	try:
		mycursor.callproc('student_get_data', [user_name,])
	except:
		print("Something went wrong... Try again later or contact the administrator")
		cnx.close()
		return 1
	
	for result in mycursor.stored_results():
		arr = (result.fetchall())
	parse_courses_assignments(arr)


def parse_courses_assignments(arr):
	prev_item = None
	print("Name"+ "		| HP |	Grade(for assignments)")
	for item in arr:
		course = item[0]
		course_hp = str(item[1])
		assignment = item[2]
		assignment_hp = str(item[3])
		grade = "G" if item[4] == 2 else "U" if item[4] == 1 else "Not graded"
		
		if prev_item == None or prev_item[0] != item[0]:
			prev_item = item
			print(course+' | '+ course_hp)
		print('└─'+assignment+' | '+ assignment_hp+' | '+ grade)
		prev_item = item
