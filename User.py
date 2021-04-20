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
        if(len(more_new_str[1]) > 64):
            print("record data field too long for " + more_new_str[0])
            return
        if more_new_str[0] == "gn":
            self.fn = more_new_str[1]
        elif more_new_str[0] == "sn":
            self.ln = more_new_str[1]
        elif more_new_str[0] == "sa":
            self.sa = more_new_str[1]
        elif more_new_str[0] == "pea":
            self.pea = more_new_str[1]
        elif more_new_str[0] == "wem":
            self.wem = more_new_str[1]
        elif more_new_str[0] == "pph":
            self.pph = more_new_str[1]
        elif more_new_str[0] == "wph":
            self.wph = more_new_str[1]
        elif more_new_str[0] == "city":
            self.city = more_new_str[1]
        elif more_new_str[0] == "stp":
            self.stp = more_new_str[1]
        elif more_new_str[0] == "cty":
            self.cty = more_new_str[1]
        elif more_new_str[0] == "pc":
            self.pc = more_new_str[1]
        else:
            print("one or more invalid record data fields")
            return -1

    def getter(self, info_string):
        more_new_str = info_string.split('=')
        if more_new_str[0] == "gn":
            return self.fn
        elif more_new_str[0] == "sn":
            return self.ln
        elif more_new_str[0] == "sa":
            return self.sa
        elif more_new_str[0] == "pea":
            return self.pea
        elif more_new_str[0] == "wem":
            return self.wem
        elif more_new_str[0] == "pph":
            return self.pph
        elif more_new_str[0] == "wph":
            return self.wph
        elif more_new_str[0] == "city":
            return self.city
        elif more_new_str[0] == "stp":
            return self.stp
        elif more_new_str[0] == "cty":
            return self.cty
        elif more_new_str[0] == "stp":
            return self.stp
        elif more_new_str[0] == "pc":
            return self.pc
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

    def print_all(self):
        return_string = ""
        if self.ln != None:
            return_string += "SN:" + str(self.ln) + ";"
        else:
            return_string += ";"
        if self.fn != None:
            return_string += "GN:" + str(self.fn) + ";"
        else:
            return_string += ";"
        if self.pea != None:
            return_string += "PEA:" + str(self.pea) + ";"
        else:
            return_string += ";"
        if self.wem != None:
            return_string += "WEM:" + str(self.wem) + ";"
        else:
            return_string += ";"
        if self.pph != None:
            return_string += "PPH:" + str(self.pph) + ";"
        else:
            return_string += ";"
        if self.wph != None:
            return_string += "WPH:" + str(self.wph) + ";"
        else:
            return_string += ";"
        if self.sa != None:
            return_string += "SA:" + str(self.sa) + ";"
        else:
            return_string += ";"
        if self.city != None:
            return_string += "CITY:" + str(self.city) + ";"
        else:
            return_string += ";"
        if self.stp != None:
            return_string += "STP" + str(self.stp) + ";"
        else:
            return_string += ";"
        if self.cty != None:
            return_string += "CTY" + str(self.cty) + ";"
        else:
            return_string += ";"
        if self.pc != None:
            return_string += "PC:" + str(self.pc) + ";"
        else:
            return_string += ";"
        print(return_string)



def add_record(current_user, record_ID, info_list):
    if(type(info_list) == list):
        for x in range(len(info_list)):
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
    if record_ID in current_user.database.keys():
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

def get_record(current_user, record_ID, info_list=None):
    if current_user.login_status == False:
        print("No Active Login Session")
        return
    if record_ID in current_user.database.keys():
        if(type(info_list) == list):
            for x in range(info_list.len()):
                new_str = info_list[x]
                new_record = current_user.database[record_ID]
                new_record.edit_fn(new_str)
                current_user.database[record_ID] = new_record
        elif info_list == None:
            current_user.database[record_ID].print_all()
        else:
            new_record = current_user.database[record_ID]
            print(new_record.getter(info_list))
    else:
        print("Record ID Not Found")
        return