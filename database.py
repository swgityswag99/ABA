import json
from User import Record


#        No active login session
#                 Admin not authorized
#                 No Input_file specified
#                 Can’t open Input_file
#                 Input_file invalid format
#                 Duplicate recordID
#                 Number of records exceeds maximum
# OK
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
            try:
                lines = f.readlines()
                used_id = []
                for line in lines:
                    new_record = Record()
                    line = line.strip().split(":")
                    record_line = line[1].strip("\"").split(";")
                    length = 0
                    list_strings = []
                    if record_line[0] not in used_id:
                        used_id.append(record_line[0])
                    else:
                        print("Duplicate ID")
                        continue
                    string = "LN=" + record_line[1]
                    list_strings.append(string)
                    string = "FN=" + record_line[2]
                    list_strings.append(string)
                    string = "PEA=" + record_line[3]
                    list_strings.append(string)
                    string = "WEM=" + record_line[4]
                    list_strings.append(string)
                    string = "PPH=" + record_line[5]
                    list_strings.append(string)
                    string = "WPH=" + record_line[6]
                    list_strings.append(string)
                    string = "SA=" + record_line[7]
                    list_strings.append(string)
                    string = "CITY=" + record_line[8]
                    list_strings.append(string)
                    string = "STP=" + record_line[9]
                    list_strings.append(string)
                    string = "CTY=" + record_line[10]
                    list_strings.append(string)
                    string = "PC=" + record_line[11]
                    list_strings.append(string)
                    for item in list_strings:
                        new_record.edit(item)
                    new_record.id = record_line[0]
                    current_user.database[record_line[0]] = new_record
                    if len(used_id) > 256:
                        print("Exceeding maximum")
            except IndexError:
                print("Input_file invalid format")
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
        print("No Output file specified")
        return
    try:
        with open(file_name, 'w') as f:
            for keys in current_user.database.keys():
                f.write(json.dumps(keys) + ":" + json.dumps(current_user.database[keys].to_string()) + "\n")
        f.close()
    except FileNotFoundError:
        print("Can't open input file")
        return

    print("OK")
