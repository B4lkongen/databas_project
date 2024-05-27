#Adrian Adborn, Viktor Listi
import sql
import inquirer

admin_command_help = [("Show all users", 1),
                        ("add a student",2),
                        ("Add a teacher",3),
                        ("remove a user",4),
                        ("Quit", 0)]

teacher_command_help = [("Show your courses", 1),
                        ("Show users",2),
                        ("add a course",3),
                        ("remove a course",4),
                        ("Add assignment to course",5),
                        ("Remove assignment to course",6),
                        ("Register student on course",7),
                        ("Deregister student on course",8),
                        ("Grade assignment",9),
                        ("Quit", 0)]

student_command_help = [("Show Your courses and assignments", 1),
                        ("Quit", 0)]

def auth(userName):
    global current_user
    global current_role
    current_user = userName      
    current_role = sql.check_user(userName)


def run():
    global current_role
    if current_role == 'admin':
        choose_action_admin()
    elif current_role == 'teacher':
        choose_action_teacher()
    elif current_role == 'student':
        choose_action_student()


def choose_action_admin():
    keep_alive = True
    while keep_alive:
        q = [inquirer.List("command", message="Here are the avalible commands\n", choices=admin_command_help)]
        a = inquirer.prompt(q)
        command = a["command"]
        if command == 0:
            keep_alive = False
        elif command == 1:
            sql.show_users()
        elif command == 2:
            sql.add_student()
        elif command == 3:
            sql.add_teacher()
        elif command == 4:
            sql.remove_user()


def choose_action_teacher():
    keep_alive = True
    while keep_alive:
        q = [inquirer.List("command", message="", choices=teacher_command_help)]
        a = inquirer.prompt(q)
        command = a["command"]
        if command == 0:
            keep_alive = False
        elif command == 1:
            sql.show_your_courses(current_user)
        elif command == 2:
            sql.show_students()
        elif command == 3:
            sql.add_course(current_user)
        elif command == 4:
            sql.remove_course(current_user)
        elif command == 5:
            sql.add_assignment()
        elif command == 6:
            sql.remove_assignment()
        elif command == 7:
            sql.add_registration()
        elif command == 8:
            sql.remove_registration()
        elif command == 9:
            sql.change_grade()
        

def choose_action_student():
    keep_alive = True
    while keep_alive:
        q = [inquirer.List("command", message="", choices=student_command_help)]
        a = inquirer.prompt(q)
        command = a["command"]
        if command == 0:
            keep_alive = False
        elif command == 1:
            sql.show_all_student(current_user)


global current_user
global current_role
current_user = None
current_role = None
auth(input('Username: '))
print(current_role)
if current_role != None:
    run()
else:
    print('Could not authenticate')