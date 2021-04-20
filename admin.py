#login
def Login(current_user, ID):

    if current_user.login_status == True:
        print("Already logged in")

    else:
        passwd = input("Password: ")

        if ID in current_user.admin_dict.keys():
            if passwd == current_user.admin_dict[ID]:
                current_user.login_status = True
                current_user.admin_priviliages = True
                current_user.current_id = ID
                print("OK")
            else:
                print("Invalid Credentials")
        elif ID in current_user.user_dict.keys():
            if passwd == current_user.user_dict[ID]:
                current_user.login_status = True
                current_user.admin_priviliages = False
                current_user.current_id = ID
                print("OK")
            else:
                print("Invalid Credentials")
        else:
            print("Invalid Credentials")

#logout
def Logout(current_user):
    if current_user.login_status == False:
        print("No login session")

    else:
        logoutCheck = input("Are you sure you want to logout? (Y/N)")
        if logoutCheck in ["Y","y","yes","Yes"]:
            current_user.login_status = False
            current_user.admin_priviliages = False
            current_user.current_id = 0
            print("OK")


#change password
def adminChangePassword(current_user, oldpassword):

    if current_user.login_status == True:
        if oldpassword == current_user.admin_dict[current_user.current_id]:
            newpassword = input("new password: ")
            if newpassword == oldpassword or newpassword == "":
                print("new password cannot be old password or nothing")
            else:
                current_user.admin_dict[current_user.current_id] = newpassword
                print("password changed")
        else:
            print("Invalid Credentials")
    else:
        print("No Active Admin Session")





#add user
def addUser(current_user, userID=None):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if userID == None:
            print("Must have User ID")
        if userID in current_user.user_dict.keys():
            print("User ID already taken")
        else:
            newPassword = input("Password: ")
            if newPassword == "":
                print("Must have password")
            else:
                current_user.user_dict[userID] = newPassword
                current_user.current_id = userID
                current_user.audit_log[current_user.current_id] = []
    else:
        print("Invalid Credentials")




#delete user
def deleteUser(current_user, userID):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if userID in current_user.user_dict.keys():
            current_user.user_dict.pop(userID, None)
        else:
            print("User does not exist")
    else:
        print("Invalid Credentials")


#display audit log
def auditLog(current_user, userID):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if 
        for item in current_user.audit_log[userID]:
            print(item)

def listUsers(current_user):    
    if current_user.login_status == True and current_user.admin_priviliages == True:        
        for key in current_user.user_dict:            
            print(key)
            print("\n")
        print("OK")
    else:        
        print("Invalid Credentials")
        