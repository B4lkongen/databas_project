import sql
import inquirer

admin_command_help = [("Show all users", 1),
                        ("Show all courses", 2),
                        ("add teacher",3),
                        ("add student",4),
                        ("Quit", 0)]

teacher_command_help = [("Show all students", 1),
                        ("Add course",3),
                        ("Register student on course",4),
                        ("Add assignment to course",5),
                        ("show your courses",6),
                        ("Quit", 0)]

student_command_help = [("Show courses", 1),
                        ("Add student",2),
                        ("Add course",3),
                        ("Register student on course",4),
                        ("Add assignment to course",5),
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
            sql.show_courses()
        elif command == 3:
            sql.add_teacher()
        elif command == 4:
            sql.add_student()

def choose_action_teacher():
    keep_alive = True
    while keep_alive:
        q = [inquirer.List("command", message="Here are the avalible commands\n", choices=teacher_command_help)]
        a = inquirer.prompt(q)
        command = a["command"]
        if command == 0:
            keep_alive = False
        elif command == 1:
            sql.show_all_student(current_user)
        elif command == 2:
            sql.add_user()
        elif command == 3:
            sql.add_course(current_user)
        elif command == 4:
            sql.add_registration()
        elif command == 5:
            sql.add_assignment()
        elif command == 6:
            sql.show_your_courses(current_user)

def choose_action_student(command):
    keep_alive = True
    while keep_alive:
        q = [inquirer.List("command", message="Here are the avalible commands\n", choices=teacher_command_help)]
        a = inquirer.prompt(q)
        command = a["command"]
        if command == 0:
            keep_alive = False
        elif command == 1:
            sql.show_assignments()
        elif command == 2:
            sql.add_user()
        elif command == 3:
            sql.add_course(current_user)
        elif command == 4:
            sql.add_registration()
        elif command == 5:
            sql.add_assignment()


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