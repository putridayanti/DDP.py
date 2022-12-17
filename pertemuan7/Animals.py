class Animals :
    #Property anmals dengan type : List
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def index(self):
        #Perulangan
        for animal in self.animals:
            print(f"Nama hewan : {animal}")

    def show(self, position):
        print(f"Menampilkan animal ke - {position} :  {self.animals[position]}")

    def store(self, animalsName):
        self.animals.append(animalsName)

        self.index()

    def update (self, position, animalName):
        self.animals[position] = animalName
        #panggil fungsi index
        self.index()

    

    def delate(self, position):
        #Cara menghapus data animal ke 1
        del self.animals[position]

        #Cara menghapus data animal ke 2

