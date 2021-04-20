from Command_line_processing import Current_User
import json

def import_database(current_user, input_file= None):
    if not current_user.login_status:
        print("No active Login Session")
        return
    if not current_user.admin_priviliages:
        print("Admin not authorized")
        return
    if input_file == None:
        print("No input file specified")
        return
    try:
        with open(input_file, 'r') as f:
            current_user.database = json.loads(f.readline())
        f.close()
    except FileNotFoundError:
        print("Can't open input file")
        return

    print("OK")
    

def export_database(current_user, file_name= None):
    if not current_user.login_status:
        print("No active Login Session")
        return
    if not current_user.admin_priviliages:
        print("Admin not authorized")
        return
    if file_name == None:
        print("No input file specified")
        return
    try:
        with open(file_name, 'w') as f:
            f.write(json.dumps(current_user.database))
        f.close()
    except FileNotFoundError:
        print("Can't open input file")
        return

    print("OK")

guy = Current_User()
guy.login_status = True
guy.admin_priviliages = True
import_database(guy)