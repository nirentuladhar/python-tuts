class Address():
    def __init__(self, street, num):
        self.street_name = street
        self.number = num

class CampusAddress(Address):
    def __init__(self, office_number):
        self.office_number = office_number
        self.street_name ="Massachusetts Ave"
        self.number = 77

addr = CampusAddress("344")

print(addr.street_name)
