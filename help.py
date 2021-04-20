def help():
    help_dict = {"HLP": "Login: LIN <userID> \n Logout: LOU <> \n Change Password: CHP <old password> \n Add User: ADU <userID> \n Delete User: DEU <userID> \n List Users: LSU <> \n Display Audit Log: DAL [<userID>] \n Add Record: ADR <recordID> [<field1=value1> <field2=value2> ...] \n Delete Record: DER <recordID> \n Edit Record: EDR <recordID> [<field1=value1> <field2=value2> ...] \n Read Record: RER <recordID> [<fieldname> ...] \n Import Database: IMD <Input_File> \n Export Database: EXD <Output_File> \n Help: HLP <command name> \n Exit: EXT <>"}
    print(help_dict)
    
    
    
    help_dict2 = {"LIN":"LIN <userID>", "LOU":"LOU <>", "CHP": "CHP <old pass>", "ADU": "ADU <userID>", "DEU": "DEU <userID>", "LSU": "LSU <>", "DAL": "DAL [<userID>]", "ADR": "ADR <recordID> [<field1=value1> <field2=value2> ...]", "DER": "DER <recordID>", "EDR" : "EDR <recordID> [<field1=value1> <field2=value2> ...]", "RER": "RER <recordID> [<fieldname> ...]", "IMD":"IMD <Input_File>", "EXD" :"EXD <Output_File>", "HLP": "HLP <command name>", "EXT": "EXT <>",}
    


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
      