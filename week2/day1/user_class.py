class User:
    def __init__(self, first_name, last_name, address=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def addAddress(address):
        address.append(address)

class Address:
     def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

address1 = Address("Cherry St", "Dallas", "TX", 12345)
olivia = User("Olivia", "Smith")


