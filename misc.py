def print_help(current_user, command=None):

    if (command == "lin"): print("LIN <userID>") 
    elif (command == "lou"): print("LOU <>") 
    elif (command == "chp"): print("CHP <old password>") 
    elif (command == "adu"): print("ADU <userID>") 
    elif (command == "deu"): print("DEU <userID>") 
    elif (command == "lsu"): print("LSU <>") 
    elif (command == "dal"): print("DAL [<userID>]") 
    elif (command == "adr"): print("ADR <recordID> [<field1=value1> <field2=value2> ...]") 
    elif (command == "der"): print("DER <recordID>") 
    elif (command == "edr"): print("EDR <recordID> [<field1=value1> <field2=value2> ...]") 
    elif (command == "rer"): print("RER <recordID> [<fieldname> ...]") 
    elif (command == "imd"): print("IMD <Input_File>") 
    elif (command == "exd"): print("EXD <Output_File>") 
    elif (command == "hlp"): print("HLP <command name>") 
    elif (command == "ext"): print("EXT <>") 
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