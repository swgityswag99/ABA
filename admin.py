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
                current_user.audit.set_items(2, current_user.current_id)
                current_user.update_audit = True
                print("OK")
            else:
                current_user.audit.set_items(1, current_user.current_id)
                current_user.update_audit = True
                print("Invalid Credentials")
        elif ID in current_user.user_dict.keys():
            if passwd == current_user.user_dict[ID]:
                current_user.login_status = True
                current_user.admin_priviliages = False
                current_user.current_id = ID
                if ID in current_user.newly_created:
                    current_user.newly_created.remove(ID)
                    current_user.audit.set_items([2,3], current_user.current_id)
                else:
                    current_user.audit.set_items(3, current_user.current_id)
                current_user.update_audit = True
                print("OK")
            else:
                current_user.audit.set_items(1, current_user.current_id)
                current_user.update_audit = True
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
            current_user.audit.set_items(8, current_user.current_id)
            current_user.update_audit = True
            print("OK")


#change password
def adminChangePassword(current_user, oldpassword):

    if current_user.login_status == True:
        if oldpassword == current_user.admin_dict[current_user.current_id]:
            newpassword = input("new password: ")
            if newpassword == oldpassword or newpassword == "":
                current_user.audit.set_items(5, current_user.current_id)
                current_user.update_audit = True
                print("new password cannot be old password or nothing")
            else:
                current_user.admin_dict[current_user.current_id] = newpassword
                current_user.audit.set_items(4, current_user.current_id)
                current_user.update_audit = True
                print("password changed")
        else:
            current_user.audit.set_items(5, current_user.current_id)
            current_user.update_audit = True
            print("Invalid Credentials")
    else:
        print("No Active login Session")





#add user
def addUser(current_user, userID):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if userID in current_user.user_dict.keys():
            print("User ID already taken")
        else:
            newPassword = input("Password: ")
            if newPassword == "":
                print("Must have password")
            else:
                current_user.user_dict[userID] = newPassword
                current_user.current_id = userID
                current_user.newly_created.append(userID)
                current_user.audit.set_items(6, current_user.current_id)
                current_user.update_audit = True
    else:
        print("Invalid Credentials")




#delete user
def deleteUser(current_user, userID):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if userID in current_user.user_dict.keys():
            current_user.audit.set_items(7, current_user.current_id)
            current_user.update_audit = True
            current_user.user_dict.pop(userID, None)
        else:
            print("User does not exist")
    else:
        print("Invalid Credentials")


#display audit log
def auditLog(current_user, userID=None):
    if current_user.login_status == True and current_user.admin_priviliages == True:
        if userID != None:
            for item in current_user.audit_log:
                if item.current_id == userID:
                    item.print_record()
        else:
            for item in current_user.audit_log:
                item.print_record()
    else:
        print("Invalid Credentials")

def listUsers(current_user):    
    if current_user.login_status == True and current_user.admin_priviliages == True:        
        for key in current_user.user_dict:            
            print(key)
            print("\n")
        print("OK")
    else:        
        print("Invalid Credentials")
        