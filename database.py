import json
from User.py import record

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
            lines = f.readlines()
            for line in lines:
                line = line.strip().split(":")
                print(line[0])
                record = line[1].strip("[").strip("]").strip("\"").split(",")
                
                
                # current_user[line[0]] = line[1]
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
            for keys in current_user.database.keys():
                f.write(json.dumps(keys) + ":" + json.dumps(current_user.database[keys].to_list()) + "\n")
        f.close()
    except FileNotFoundError:
        print("Can't open input file")
        return

    print("OK")
