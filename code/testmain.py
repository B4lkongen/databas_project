import sql

def auth(userName):
    global current_user
    global current_role
    current_user = userName
    current_role = sql.check_user(userName)


def run():
    keep_alive = True
    while keep_alive:
        command = input('Input command: ')
        if command == 'q':
            keep_alive = False
        choose_action(command)

def choose_action(command):
    if command == '1':
        sql.show_all_student(current_user)
    elif command == '2':
        sql.add_user()
    elif command == '3':
        sql.add_course(current_user)
    elif command == '4':
        sql.add_registration()
    elif command == '5':
        sql.add_assignment()

def choose_action_student(command):
    if command == '1':
        sql.show_all()
    elif command == '2':
        sql.add_user()
    elif command == '3':
        sql.add_course(current_user)
    elif command == '4':
        sql.add_registration()
    elif command == '5':
        sql.add_assignment()





global current_user
global current_role
current_user = None
current_role = None
auth(input('Username: '))

if current_role != None:
    run()
else:
    print('Could not authenticate')