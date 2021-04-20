import json
from User import Record


import base64
import os
from cryptography.fernet import Fernet
  
# key is generated
key = Fernet.generate_key()
  
# value of key is assigned to a variable
f_key = Fernet(key)
  
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
        with open(input_file, 'rb') as f:
            original_message = b""
            try:
                byte = f.read(1)
                while byte != b"":
                    original_message += byte
                    byte = f.read(1)
                d = f_key.decrypt(original_message)
                used_id = []
                for line in d.decode().split("\n"):
                    if(len(line) > 0):
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
                        string = "sn=" + record_line[1]
                        list_strings.append(string)
                        string = "gn=" + record_line[2]
                        list_strings.append(string)
                        string = "pea=" + record_line[3]
                        list_strings.append(string)
                        string = "wem=" + record_line[4]
                        list_strings.append(string)
                        string = "pph=" + record_line[5]
                        list_strings.append(string)
                        string = "wph=" + record_line[6]
                        list_strings.append(string)
                        string = "sa=" + record_line[7]
                        list_strings.append(string)
                        string = "city=" + record_line[8]
                        list_strings.append(string)
                        string = "stp=" + record_line[9]
                        list_strings.append(string)
                        string = "cty=" + record_line[10]
                        list_strings.append(string)
                        string = "pc=" + record_line[11]
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
        with open(file_name, 'wb') as f:
            original_message = ""
            for keys in current_user.database.keys():
                original_message += str(keys) + ":" + str(current_user.database[keys].to_string()) + "\n"
            token = f_key.encrypt(original_message.encode("utf-8"))
            f.write(token)
        f.close()
    except FileNotFoundError:
        print("Can't open output file")
        return

    print("OK")
