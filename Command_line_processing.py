import json

def wut():
    print("wutwut")

def wutwut(yes):
    print(yes)

Func_Dict = {"wut": wut, "wutwut": wutwut}

class Current_User:
    self.login_status = False
    self.admin_priviliages = False
    self.current_id = 0
    self.user_dict = {}
    self.admin_dict = {}
    self.database = None

    def initialization(self):
        #load your dict and stuff
        try:
            with open("user.txt", 'r') as f:
                self.user_dict = json.loads(f.readline())
            f.close()
        except FileNotFoundError:pass

        try:
            with open("user.txt", 'r') as f:
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
                    Func_Dict.get(user_input[0])()
                elif num_args == 1:
                    Func_Dict.get(user_input[0])(user_input[1])
                elif num_args == 2:
                    Func_Dict.get(user_input[0])(user_input[1], user_input[2])
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
guy.main_loop()
