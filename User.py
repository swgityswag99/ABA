class record:
    def __init__(self, fn, ln, address):
        self.fn = fn 
        self.ln = ln
        self.address = address

    def edit_fn(self, new_name):
        self.fn = new_name
    def edit_ln(self, new_name):
        self.ln = new_name
    def edit_address(self, new_address):
        self.address = new_address 


def edit_database(address_database):
#    record = input("Enter record id to manipulate: ")
    option = input("Would you like to: \n 1) add record \n 2) delete record \n 3) edit record \n")
        #add record
    
    if option == "1":
        hello = True
        if option == "1":
            while(hello):
                key = input("Enter Unique ID: ")
                if key in address_database and key:
                    continue
                else:
                    hello = False
        key = input("Enter Unique ID: ")
        first = input("Enter First Name: ")
        last = input("Enter Last Name: ")
        address = input("Enter Address: ")
        obj = record(first, last, address)
        address_database[key] = obj
    #delete record
    elif option == "2":
        deleter = input("Enter id of item to delete: ")
        address_database.pop(deleter)
    #edit record
    elif option == "3":
        user = input("Enter User ID: ")
        option2 = input("Would you like to: \n 1) edit first name \n 2) edit last name \n 3) edit address \n ")
        if option2 == "1":
            name = input("Enter new first name: ")
            address_database[user].fn = name
        elif option == "2":
            namee = input("Enter new last name: ")
            address_database[user].ln = namee
        elif option == "3":
            address = input("Enter new address: ")
            address_database[user].address = address
