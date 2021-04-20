import json
from User import edit_database, record
from database import import_database, export_database

Func_Dict = {"database":edit_database, "imd":import_database, "exd":export_database}


class Current_User():
    def __init__(self):
        self.login_status = False
        self.admin_priviliages = False
        self.current_id = 0
        self.user_dict = {}
        self.admin_dict = {}
        self.database = {}
        self.audit_log = {}

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
            else:
                print("Incorrect usage, input help for assistance")

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
guy.login_status = True
guy.admin_priviliages = True
new_record = record("wut","the","fuk")
guy.database["1"] = new_record
new_record = record("wut2","the2","fuk2")
guy.database["2"] = new_record
guy.main_loop()
