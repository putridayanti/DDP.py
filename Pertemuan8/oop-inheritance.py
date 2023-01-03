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

# Extend :=> nurutin sifat dari class person

class Student(Person):

    # Manggil conctructor class person

    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(name, address, age)
        self.nim = nim
        self.jurusan = jurusan

# Instance object

fauzan = Student("fauzan ", "Bogor, Jabar", 20, "0110122231", "Sistem Informasi") 

fauzan.sayHello( )
print("Nim: ", fauzan.nim)
print("Jurusan: ", fauzan.jurusan)