

import json
from record import add_record, Record, delete_record, edit_record, get_record
from misc import print_help
from misc import print_help
from database import import_database, export_database
from admin import Login, Logout, adminChangePassword, addUser, deleteUser, auditLog, listUsers
Func_Dict = {"imd":import_database, "exd":export_database,
                "lin":Login, "lou":Logout, "chp":adminChangePassword, "adr":add_record,
                "adu":addUser, "deu":deleteUser, "dal":auditLog,"lsu":listUsers, "hlp":print_help,
                "der":delete_record, "edr":edit_record, "rer":get_record}
from datetime import date, datetime 
messages = {1:"LF", 2:"LS", 3:"L1", 4:"SPC", 5:"FPC",
                        6:"AU", 7:"DU", 8:"LO"}
class Audit():
    def __init__(self):
        self.time = None
        self.type = None
        self.id = None

    def print_record(self):
        string = self.time + ";"
        if(type(self.type) == list):
            for item in self.type:
                string += messages[item] + ";"
        else:
            string += messages[self.type] + ";"
        string += str(self.id)
        print(string)
    
    def set_items(self, record_type, ID):
        self.time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.type = record_type
        self.id = ID


class Current_User():
    def __init__(self):
        self.login_status = False
        self.admin_priviliages = False
        self.current_id = 0
        self.user_dict = {"2":"bob"}
        self.admin_dict = {"1":"passwd"}
        self.database = {}
        self.audit_log = []
        self.audit = Audit()
        self.update_audit = False
        self.newly_created = []
        
    def initialization(self):
        #load your dict and stuff
        try:
            with open("user.txt", 'r') as f:
                self.user_dict = json.loads(f.readline())
            f.close()
        except FileNotFoundError:pass

        try:
            with open("admin.txt", 'r') as f:
                self.user_dict = json.loads(f.readline())
            f.close()
        except FileNotFoundError:pass

    def main_loop(self):
        print("Address Book Application, version <1>. Type \"HLP\" for a list of commands.")
        while(True):
            user_input = input("ABA>")
            user_input = user_input.lower().strip().split(" ")
            num_args = len(user_input) - 1
            if user_input[0] == "ext":
                print("Okay")
                self.exit()
            if user_input[0] in Func_Dict.keys():
                try:
                    if user_input[0] == "adr" or user_input[0] == "edr":
                        temp = []
                        for item in user_input[2:]:
                            temp.append(item)
                        del user_input[2:-1]
                        num_args = 2
                    if num_args == 0:
                        Func_Dict.get(user_input[0])(self)
                    elif num_args == 1:
                        Func_Dict.get(user_input[0])(self, user_input[1])
                    elif num_args == 2:
                        Func_Dict.get(user_input[0])(self, user_input[1], user_input[2])
                    else:
                        print("Unrecognized command")
                except TypeError:
                    print("Incorrect number of parameters, input help for assistance")
            else:
                print("Unrecognized command")
            if self.update_audit == True:
                if len(self.audit_log) > 512:
                    print("aduit log exceeding maximum size")
                    self.update_audit = False
                    continue
                self.audit_log.append(self.audit)
                self.audit = Audit()
                self.update_audit = False

    def exit(self):
        with open("user.txt", 'w') as f:
            f.write(json.dumps(self.user_dict))
        f.close()
        with open("admin.txt", 'w') as f:
            f.write(json.dumps(self.admin_dict))
        f.close()
        exit(0)

guy = Current_User()
guy.main_loop()
