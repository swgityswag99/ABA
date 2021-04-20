version = 0.1

#Login parameters
active_login = False #At startup, there is no active login
account_exists = False #Default is that admin account exists with ID 0, should change for new user accounts
account_used = False #Checks if account has been used before or not
current_password = "" #Account password, needs to be kept secret
password_check = "" #Verify actual password with this user input
user_id = 0 #Default admin ID is 0
user_id_check = ""

#Change password parameters
new_password = ""
new_password_check = ""

#Admin-only, Add/Delete User, Audit parameters
is_admin = True
new_user_id = -1
del_user_id_check = -1
audit_user_id = -1

#Non-admin only, Add/Edit/Delete/Read Record parameters
new_record_id = -1
del_record_id = -1
edit_record_id = -1
read_record_id = -1

#Import/export Database parameters
import_database = ""
export_database = ""
max_records = 10

print("Address Book Application, version %.1f. Type HLP for a list of commands." % version)

while True:
    command = input("ABA> ")

    #All commands:
    #Syntax - (command code) <parameters> <field1=value1> [<field1=value2> ...]
    #       - command[0]    command[1]     command[2], etc...
    command = list(map(str, command.split())) #Creates list of parameters
    command.append("") #Avoid out of index error

    #############Authentication Commands#############

    #Login command: Syntax - LIN <userID>
    if (command[0] == "LIN"):
        
        if (command[1] == ""):
            print("Please input a user id")
            continue

        user_id_check = command[1] #Current user ID

        if (user_id_check == str(user_id)):
            account_exists = True

        #Insert check for user id, set LIN parameters (!)
        #Currently only checks for default admin ID of 0

        #LIN Case 1 - There is a currently active login
        if (active_login == True):
            print("An account is currently active; logout before proceeding")
            continue
        
        #LIN Case 2 - There is no currently active login but the account does not exist
        elif (active_login == False and account_exists == False):
            print("Invalid credentials")
            continue
        
        #LIN Case 3 - There is no currently active login, the account exists, and this is NOT the first time the account has been used.
        elif (active_login == False and account_exists == True and account_used == True):
            password_check = input("Enter your password: ") #Password defaults to string, can change if needed

            if (password_check == current_password):
                print("OK") #All completion codes are printed simply as strings, can change to actual variables if desired
                active_login = True
                account_used = True
                continue

            else: 
                print("Invalid credentials")
                continue

        #LIN Case 4 - There is no currently active login, the account exists, and this is the first time that the account has been used.
        #In the initial system state, the default user (admin), first defaults to this state to create password
        elif (active_login == False and account_exists == True and account_used == False):
            print("This is the first time the account is being used. You must create a new password.")
            print("Passwords may contain 1-24 upper- or lower-case letters or numbers. Choose an uncommon password that would be difficult to guess.")

            current_password = input("Enter a password: ")
            password_check = input("Reenter the same password: ")

            #Completion status codes are returned in the following order:
            if (current_password != password_check):
                print("Passwords do not match")
                continue
            elif (type(current_password) != str): #Does not check for non-alphanumeric characters
                print("Password contains illegal characters")
                continue
            elif (current_password == "password"): #Should refer to list of common passwords or adhere to set criteria
                print("Password is too easy to guess")
                continue

            else:
                print("OK")
                active_login = True
                account_used = True 
                continue


    #Logout command: Syntax - LOU
    elif (command[0] == "LOU"):

        #LOU Case 1 - If no active login session, do nothing
        if (active_login is False):
            print("No active login session")
            continue
        #LOU Case 2 - If there is an active login session, terminate the session
        else:
            #Delete own user ID from active login list
            print("OK")
            continue


    #Change password command: Syntax - CHP <old password>
    elif (command[0] == "CHP"):

        if (command[1] == ""):
            print("Please input your old password.")
            continue
        else:
            password_check = command[1] #Set old password check

        #CHP Case 1 - There is no active login
        if (active_login == False):
            print("No active login session")
            continue
        
        #CHP Case 2 - User input does not match current password
        elif(password_check != current_password):
            print("Invalid credentials")
            continue

        else:
            #Authentication credentials are correct, prompt the user to create a new password
            #Same procedure as with LIN
            print("Create a new password.")
            print("Passwords may contain 1-24 upper- or lower-case letters or numbers. Choose an uncommon password that would be difficult to guess.")

            new_password = input("Enter a password: ")
            new_password_check = input("Reenter the same password: ")

            #Completion status codes are returned in the following order:
            if (new_password != new_password_check):
                print("Passwords do not match")
                continue
            elif (type(new_password) != str): #Does not check for non-alphanumeric characters
                print("Password contains illegal characters")
                continue
            elif (new_password == "password"): #Should refer to list of common passwords or adhere to set critera
                print("Password is too easy to guess")
                continue
            else:
                print("OK")
                current_password = new_password #Set new password
                continue
        
    #############Admin-only Commands#############

    #Add User command: Syntax - ADU <userID>
    #Delete User command: Syntax - DEU <userID>
    #Display Audit Log command: Syntax - DAL <userID>
    #List Users command: Syntax - LSU
    elif ((command[0] == "ADU" or command[0] == "DEU" or command[0] == "DAL" or command[0] == "LSU") and is_admin == True):

        if (command[0] == "ADU"): 
            new_user_id = command[1] #New user ID to create
        elif (command[0] == "DEU"):
            del_user_id_check = command[1] #Check for user ID to delete
        elif (command[0] == "DAL"):
            audit_user_id = command[1] #Optional

        #ADU/DEU/DAL/LSU Case 1 - There is no active login
        if (active_login == False):
            print("No active login session")
            continue

        #ADU/DEU/DAL/LSU Case 2 - Admin not active (might not need this, since cannot use command without being admin)
        elif (active_login == True and is_admin == False):
            print("Admin not active")
            continue

        #ADU/DEU/DAL Case 3 - Invalid user ID, incorrect form
        elif (type(new_user_id) != str or type(del_user_id_check) != str): #Does not check for non-alphanumeric characters
            print("Invalid userID")
            continue

        #ADU Case 4 - Invalid user ID, pre-existing account
        if (command[0] == "ADU" and new_user_id == user_id): #Should point to list of current IDs
            print("Account already exists")
            continue

        #DEU Case 4 - Invalid user ID, account does not exist
        elif (command[0] == "DEU" and del_user_id_check != user_id): #Should point to list of current IDs
            print("Account does not exist")
            continue

        
        #Admin operations, success status codes
        #If we reach this stage, assume all conditions for the given command are satisfied
        if (command[0] == "ADU"):
            #Create new account with given user ID
            print("OK")
            continue

        elif (command[0] == "DEU"):
            #Delete the account associated with the given ID
            print("OK")
            continue
        
        elif (command[0] == "LSU"):
            #List all user account names, each on a seperate line
            print("OK")
            continue

        elif (command[0] == "DAL"):
            #DEU Case 4 - Invalid user ID, account does not exist
            if (audit_user_id == user_id): #Should point to list of current IDs
                print("OK")
                #Print out all audit records for this user
                continue
            else:
                print("Account does not exist")
                #Print out all audit records for all users
                print("OK")
                continue
    

    #############Database Commands (Non-Admin)#############

    #Add Record command: Syntax - ADR <recordID> [<field1=value1> <field2=value2> ...]
    #Delete Record command: Syntax - DER <recordID>
    #Edit Record command: Syntax - EDR <recordID> [<field1=value1> <field2=value2> ...]
    #Read Record command: Syntax - RER <recordID> [<fieldname> ...]
    elif ((command[0] == "ADR" or command[0] == "DER" or command[0] == "EDR" or command[0] == "RER") and is_admin == False):
        
        #ADR/DER/EDR/RER Case 1 - There is no active login
        if (active_login == False):
            print("No active login session")
            continue

        #ADR/DER/EDR/RER Case 2 - Non-admin actions
        elif (active_login == True and is_admin == False):
            print("Admin not authorized")
            continue

        if (command[0] == "ADR"): 
            new_record_id = command[1] #Unique ID for new record
        elif (command[0] == "DER"):
            del_record_id = command[1] #Check for record ID to delete
        elif (command[0] == "EDR"):
            edit_record_id = command[1] #Record ID to edit
        elif (command[0] == "RER"):
            read_record_id = command[1] #Record ID to read


        #No recordID
        #Invalid recordID
        #One or more invalid record data fields
        #Number of records exceeds maximum
        #Duplicate recordID


        #User operations, success status codes
        #If we reach this stage, assume all conditions for the given command are satisfied

        elif (command[0] == "ADR"):
            #Record in database for active user that matches the recordID is created
            print("OK")
            continue

        elif (command[0] == "DER"):
            #Record in database for active user that matches the recordID is deleted
            print("OK")
            continue

        elif (command[0] == "EDR"):
            #Record in database for active user that matches the recordID is edited
            print("OK")
            continue

        elif (command[0] == "RER"):
            #Record in database for active user that matches the recordID is dislayed
            print("OK")
            continue

    #Import Database command: Syntax - IMD <Input_File>
    #Export Database command: Syntax - EXD <Output_File>
    elif ((command[0] == "IMD" or command[0] == "EXD") and is_admin == False):

        #IMD/EXD Case 1 - There is no active login
        if (active_login == False):
            print("No active login session")
            continue

        #IMD/EXD Case 2 - Non-admin actions
        elif (active_login == True and is_admin == False):
            print("Admin not authorized")
            continue

        elif (command[0] == "IMD" and command[1] == ""):
            print("No Input_file specified")
            continue
        elif (command[0] == "EXD" and command[1] == ""):
            print("No Output_file specified")
            continue

        if (command[0] == "IMD"): 
            import_database = command[1] #Input filename
        elif (command[0] == "DER"):
            export_database = command[1] #Output filename

        #Cannot open input/output file
        #Input file invalid format, error writing output_file
        #Duplicate recordID
        #Number of records exceeds maximum, max_records


        #User operations, success status codes
        #If we reach this stage, assume all conditions for the given command are satisfied
              
        elif (command[0] == "IMD"):
            #Records are added to database for active user
            print("OK")
            continue
        elif (command[0] == "EXD"):
            #Records are written to the file specified
            print("OK")
            continue

    
    #############Miscellaneous Commands#############
    #Help command: Syntax - HLP
    if (command[0] == "HLP"):
        if (command[1] == "LIN"): print("LIN <userID>") 
        elif (command[1] == "LOU"): print("LOU <>") 
        elif (command[1] == "CHP"): print("CHP <old password>") 
        elif (command[1] == "ADU"): print("ADU <userID>") 
        elif (command[1] == "DEU"): print("DEU <userID>") 
        elif (command[1] == "LSU"): print("LSU <>") 
        elif (command[1] == "DAL"): print("DAL [<userID>]") 
        elif (command[1] == "ADR"): print("ADR <recordID> [<field1=value1> <field2=value2> ...]") 
        elif (command[1] == "DER"): print("DER <recordID>") 
        elif (command[1] == "EDR"): print("EDR <recordID> [<field1=value1> <field2=value2> ...]") 
        elif (command[1] == "RER"): print("RER <recordID> [<fieldname> ...]") 
        elif (command[1] == "IMD"): print("IMD <Input_File>") 
        elif (command[1] == "EXD"): print("EXD <Output_File>") 
        elif (command[1] == "HLP"): print("HLP <command name>") 
        elif (command[1] == "EXT"): print("EXT <>") 
        else:
            print("Login: LIN <userID>") 
            print("Logout: LOU <>") 
            print("Change Password: CHP <old password>") 
            print("Add User: ADU <userID>") 
            print("Delete User: DEU <userID>") 
            print("List Users: LSU <>") 
            print("Display Audit Log: DAL [<userID>]") 
            print("Add Record: ADR <recordID> [<field1=value1> <field2=value2> ...]") 
            print("Delete Record: DER <recordID>") 
            print("Edit Record: EDR <recordID> [<field1=value1> <field2=value2> ...]") 
            print("Read Record: RER <recordID> [<fieldname> ...]") 
            print("Import Database: IMD <Input_File>") 
            print("Export Database: EXD <Output_File>") 
            print("Help: HLP <command name>") 
            print("Exit: EXT <>") 
            continue



    #Exit command: Syntax - EXT: closes open session, if any, and always exists program
    elif (command[0] == "EXT"):
        print("OK")
        break

    #Last case: invalid commands
    else:
        print("Unrecognized command")
        continue
