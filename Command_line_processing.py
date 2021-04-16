
class Current_User:
    login_status = False
    current_id = 0
    user_dict = {}
    admin_dict = {}


    def initialization(self):
        pass

    def main_loop(self):
        user_input = input("Welcome, input help at any time for assistance")
        
        while(True):
            if user_input == "help":
                

            if(login_status == False):
                print("Please login to proceed")
                # user_login(user_dict, user_input)
                # admin_login(admin_dict, user_input)
                pass
            else:
                pass
            input("Command Input:")




main_loop()
