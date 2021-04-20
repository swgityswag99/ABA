import json
from User import edit_database, record
from database import import_database, export_database
from admin import Login, Logout, adminChangePassword, addUser, deleteUser, auditLog, listUsers
Func_Dict = {"database":edit_database, "imd":import_database, "exd":export_database,
                "lin":Login, "lou":Logout, "chp":adminChangePassword,
                "adu":addUser, "deu":deleteUser, "dal":auditLog,"lsu":listUsers}
from datetime import date, datetime 

class Audit_BS():
    def __init__(self):
        self.date = None
        self.time = None
        self.type = None
        self.id = None
        self.messages = {1:"LF", 2:"LS", 3:"L1", 4:"SPC", 5:"FPC",
                        6:"FPC", 7:"AU", 8:"DU"}

    def print_record(self):
        string = self.date + ";" + self.time + ";"
        if(type(self.type) == list):
            for item in self.type:
                string += item + ";"
        else:
            string += item + ";"
        string += self.id
        print(string)
    
    def set_items(self, record_type, ID):
        self.date = date.today()
        self.time = datetime.now().strftime("%H:%M:%S")
        self.type = record_type
        self.id = ID


#  Failed logins (LF)
# • Successful logins (LS)
# • First logins (L1) - when passwords are first created; both L1 and LS records are generated
# • Logouts (LO)
# • Successful password changes (SPC)
# • Failed password changes (FPC)
# • Added users (AU)
# • Deleted users (DU)
# Audit records shall have the following fields:
#       Date, Time, Audit record type, UserID
class Current_User():
    def __init__(self):
        self.login_status = False
        self.admin_priviliages = False
        self.current_id = 0
        self.user_dict = {}
        self.admin_dict = {"1":"passwd"}
        self.database = {}
        self.audit_log = []
        self.audit = Audit_BS


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
        print("Welcome, input help at any time for assistance")
        while(True):
            user_input = input("Command Input:")
            user_input = user_input.lower().strip().split(" ")
            num_args = len(user_input) - 1
            if user_input[0] in Func_Dict.keys():
                try:
                    if user_input[0] == "exit":
                        print("Thank you and good bye")
                        self.exit()
                    elif num_args == 0:
                        Func_Dict.get(user_input[0])(self)
                    elif num_args == 1:
                        Func_Dict.get(user_input[0])(self, user_input[1])
                    elif num_args == 2:
                        Func_Dict.get(user_input[0])(self, user_input[1], user_input[2])
                    else:
                        print("Incorrect usage, input help for assistance")
                except TypeError:
                    print("Incorrect number of parameters, input help for assistance")
            else:
                print("Incorrect usage, input help for assistance")
            self.audit_log[self.current_id].append(str(user_input))

    def exit(self):
        with open("user.txt", 'w') as f:
            f.write(json.dumps(self.user_dict))
        f.close()
        with open("admin.txt", 'w') as f:
            f.write(json.dumps(self.admin_dict))
        f.close()
        if self.database is not None:
            with open("database.txt", 'w') as f:
                f.write(json.dumps(self.database))
            f.close()

guy = Current_User()
# guy.login_status = True
# guy.admin_priviliages = True
# new_record = record("wut","the","fuk")
# guy.database["1"] = new_record
# new_record = record("wut2","the2","fuk2")
# guy.database["2"] = new_record
guy.main_loop()
