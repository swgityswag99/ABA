

#10 digit alpha numerics randomly generated
#list with the username and password (need to put these in a file)
adminPSSWD = [["happyfish", "bobbyfish", "wiqhmx01ri"], ["armara367", "coffeelover86", "83qmd2sp48"], ["katieMarie", "iloveBrad23", "vl8fazbe3f"]]
userPSSWD = [["bobbyjean", "ilovepizza"], ["missycopeland", "ilovefred24"], ["katieMarie", "iloveBrad23"]]

#text files of data
file = open("admindoc.txt", "w")

loggedin = False
passwordtries = 0

#login
passwordflag = True
usernameflag = True
while(passwordflag):

    while(usernameflag):
        username = input("Username: ")
        for k in adminPSSWD:
            if username == k[0]:
                usernameflag = False
        if usernameflag == True:
            print("No username recorded")

    password = input("Password: ")

    for i in adminPSSWD:
        if username == i[0]:
            if password == i[1]:
                adminverify = input("Admin ID: ")
                if i[2] == adminverify:
                    loggedin = True
                    print("Access Granted")
                    passwordflag = False
                else:
                    print("Admin ID not verifiable")
            else:
                print("Incorrect Password\n")
                passwordtries += 1
                if passwordtries > 2:
                    print("Too many login attempts")
                    passwordflag = False

#everything else can only happen when loggedin
while (loggedin):
    command = input("What next? ")
    #will make a command list here to keep track of all admin commands

#logout
    if command == "logout":
        logoutCheck = input("Are you sure you want to logout? (Y/N)")
        if logoutCheck in ["Y","y","yes","Yes"]:
            loggedin = False


#change password
    if command == "changepassword":
        checkwho = True
        while(checkwho):
            who = ""
            print(who)
            who = input("user or admin? ")
            print(who)

            #user password change
            if who in ["user","User"]:
                print(who, "hit")
                userchange = input("username: ")
                oldpassword = input("old password: ")
                for i in userPSSWD:
                    if userchange == i[0]:
                        if oldpassword == i[1]:
                            passcheck = True
                            while(passcheck):
                                newpassword = input("new password: ")
                                if newpassword == oldpassword or newpassword == "":
                                    print("new password cannot be old password or nothing")

                                else:
                                    i[1] = newpassword
                                    print("password changed")
                                    passcheck = False
                                    checkwho = False
                        else:
                            print("Incorrect password")

            #admin password change
            elif who in ["admin","Admin"]:
                adminchange = input("Admin: ")
                adminIDchange = input("Admin ID: ")
                oldpassword = input("old password: ")
                for i in adminPSSWD:
                    if userchange == i[0]:
                        if oldpassword == i[1] and i[2] == adminIDchange:
                            passcheck = True
                            while(passcheck):
                                newpassword = input("new password: ")
                                if newpassword == oldpassword or newpassword == "":
                                    print("new password cannot be old password or nothing")

                                else:
                                    i[1] = newpassword
                                    print("password changed")
                                    passcheck = False
                                    checkwho = False
                        else:
                            print("Incorrect password or Admin ID")
                            break

            else:
                print(who)
                print("choose user or admin")




#add user
    if command == "adduser":
        correctcheck = True
        finduser = True
        while(correctcheck):  #need to check if username is already taken
            while(finduser):
                alreadyuser = False
                newUser = input("Username: ")
                if newUser == "":
                    print("Must have username")
                for b in userPSSWD:
                    if newUser == b[0]:
                        alreadyuser = True
                        print("Username already taken")
                if alreadyuser == False:
                    finduser = False
            newPassword = input("Password: ")
            if newPassword == "":
                print("Must have password")

            else:
                newUseradd = [newUser, newPassword]
                userPSSWD.append(newUseradd)
                print("New User Added!")
                correctcheck = False
        print("check user")
        print(userPSSWD)



#delete user
    if command == "deleteuser":
        checkuser = True
        userFlag = True
        while(checkuser):
            while(userFlag):
                delUser = input("Username: ")
                for k in userPSSWD:
                    if delUser == k[0]:
                        userFlag = False
                if userFlag == True:
                    print("User does not exist")
            delPassword = input("Password: ")
            for i in userPSSWD:
                if delUser == i[0]:
                    if delPassword == i[1]:
                        userPSSWD.remove(i)
                        print("user removed")
                        checkuser = False
                    else:
                        print("Incorrect Password\n")
        print("check user")
        print(userPSSWD)


#display audit log
    #could add another part to the list that stores all of the user's commands?


    else:
        print("invalid command")
