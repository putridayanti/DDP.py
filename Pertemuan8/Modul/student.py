# from person import *
from Modul.person import Person

# Extend :=> nurutin sifat dari class person

class Student(Person):

    # Manggil conctructor class person

    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(name, address, age)
        self.nim = nim
        self.jurusan = jurusan
