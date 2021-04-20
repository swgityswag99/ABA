class Record:
    def __init__(self):
        self.id = None
        self.fn = None
        self.ln = None
        self.sa = None
        self.pea = None
        self.wem = None
        self.pph = None
        self.wph = None
        self.city = None
        self.stp = None
        self.cty = None
        self.pc = None

    def edit(self, info_string):
        more_new_str = info_string.split('=')
        print(more_new_str)
        print(len(more_new_str))
        if more_new_str[0] == "FN":
            self.fn = more_new_str[1]
        elif more_new_str[0] == "LN":
            self.ln = more_new_str[1]
        elif more_new_str[0] == "SA":
            self.sa = more_new_str[1]
        elif more_new_str[0] == "PEA":
            self.pea = more_new_str[1]
        elif more_new_str[0] == "WEM":
            self.wem = more_new_str[1]
        elif more_new_str[0] == "PPH":
            self.pph = more_new_str[1]
        elif more_new_str[0] == "WPH":
            self.wph = more_new_str[1]
        elif more_new_str[0] == "CITY":
            self.city = more_new_str[1]
        elif more_new_str[0] == "STP":
            self.stp = more_new_str[1]
        elif more_new_str[0] == "CTY":
            self.cty = more_new_str[1]
        elif more_new_str[0] == "STP":
            self.stp = more_new_str[1]
        elif more_new_str[0] == "PC":
            self.pc = more_new_str[1]
        else:
            print("one or more invalid record data fields")
            return -1

    def getter(self, info_string):
        more_new_str = info_string.split('=')
        if more_new_str[0] == "FN":
            return new_record[recordID].fn
        elif more_new_str[0] == "LN":
            return new_record[recordID].ln
        elif more_new_str[0] == "SA":
            return new_record[recordID].sa
        elif more_new_str[0] == "PEA":
            return new_record[recordID].pea
        elif more_new_str[0] == "WEM":
            return new_record[recordID].wem
        elif more_new_str[0] == "PPH":
            return new_record[recordID].pph
        elif more_new_str[0] == "WPH":
            return new_record[recordID].wph
        elif more_new_str[0] == "CITY":
            return new_record[recordID].city
        elif more_new_str[0] == "STP":
            return new_record[recordID].stp
        elif more_new_str[0] == "CTY":
            return new_record[recordID].cty
        elif more_new_str[0] == "STP":
            return new_record[recordID].stp
        elif more_new_str[0] == "PC":
            return new_record[recordID].pc
        else:
            print("one or more invalid record data fields")
            return


    def to_string(self):
        return_string = ""
        if self.id != None:
            return_string += str(self.id) + ";"
        else:
            return_string += ";"
        if self.ln != None:
            return_string += str(self.ln) + ";"
        else:
            return_string += ";"
        if self.fn != None:
            return_string += str(self.fn) + ";"
        else:
            return_string += ";"
        if self.pea != None:
            return_string += str(self.pea) + ";"
        else:
            return_string += ";"
        if self.wem != None:
            return_string += str(self.wem) + ";"
        else:
            return_string += ";"
        if self.pph != None:
            return_string += str(self.pph) + ";"
        else:
            return_string += ";"
        if self.wph != None:
            return_string += str(self.wph) + ";"
        else:
            return_string += ";"
        if self.sa != None:
            return_string += str(self.sa) + ";"
        else:
            return_string += ";"
        if self.city != None:
            return_string += str(self.city) + ";"
        else:
            return_string += ";"
        if self.stp != None:
            return_string += str(self.stp) + ";"
        else:
            return_string += ";"
        if self.cty != None:
            return_string += str(self.cty) + ";"
        else:
            return_string += ";"
        if self.pc != None:
            return_string += str(self.pc) + ";"
        else:
            return_string += ";"
        return return_string
       
       # return_string = str(self.id) + ";" + str(self.ln) +";" + str(self.fn) + ";" + str(self.pea) + ";"
       # return_string += str(self.wem) + ";" + str(self.pph) + ";" + str(self.wph) + ";" + str(self.sa) + ";" + str(self.city) + ";"
       # return_string += str(self.stp) + ";" + str(self.cty) + ";" + str(self.pc) + ";"

def add_record(current_user, record_ID, info_list):
    if(type(info_list) == list):
        for x in range(info_list.len()):
            new_str = info_list[x]
            new_record = Record()
            new_record.edit_fn(new_str)
            current_user.database[record_ID] = new_record
    else:
        new_record = Record()
        val = new_record.edit(info_list)
        if val == -1:
            return
        current_user.database[record_ID] = new_record
    new_record.id = record_ID
    print("OK")

def delete_record(current_user, record_ID):
    if current_user.login_status == False:
        print("No Active Login Session")
        return
    if current_user.admin_priviliages == False:
        print("Admin Not Active")
        return
    if record_ID in current_user.database:
        print("OK")
        del current_user.database[record_ID]
    else:
        print("Record ID Not Found")
        return

def edit_record(current_user, record_ID, info_list):      
    if current_user.login_status == False:
        print("No Active Login Session")
        return
    if current_user.admin_priviliages == False:
        print("Admin Not Active")
        return
    if record_ID in current_user.database:
        print("OK")
        if(type(info_list) == list):
            for x in range(info_list.len()):
                new_str = info_list[x]
                new_record = current_user.database[record_ID]
                new_record.edit_fn(new_str)
                current_user.database[record_ID] = new_record
        else:
            new_record = current_user.database[record_ID]
            new_record.edit(info_list)
            current_user.database[record_ID] = new_record
            new_record.id = record_ID
    else:
        print("Record ID Not Found")
        return

def get_record(current_user, record_ID, info_list):
    if(type(info_list) == list):
            for x in range(info_list.len()):
                new_str = info_list[x]
                new_record = current_user.database[record_ID]
                new_record.edit_fn(new_str)
                current_user.database[record_ID] = new_record
    else:
        new_record = current_user.database[record_ID]
        print(new_record.getter(info_list))
        
