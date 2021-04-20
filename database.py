import json
from User import record as Record

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
                record_line = line[1].strip("[").strip("]").strip("\"").split(",")

                record = Record(record_line[0],record_line[1],record_line[2])
                current_user.database[line[0]] = record
        f.close()
        print(current_user.database)
        print(len(current_user.database.keys()))
        print(len(current_user.database))
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
