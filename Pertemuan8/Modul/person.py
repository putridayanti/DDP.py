class Person():

    # Definisikan awal variabel

    name = ""
    address = ""
    age = ""

    # Constructor :=> pembungkus

    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    # Methodn / Function
    def sayHello(self):
        print("Hello nama saya ", self.name, "usia saya ", self.age, "alamat saya di ", self.address)
