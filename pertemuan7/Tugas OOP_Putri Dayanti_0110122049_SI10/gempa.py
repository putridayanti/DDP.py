class gempa :
    #memberi variabel
    lokasi = ""
    skala = 0
    #memberi konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
    #member3 method
    def dampak (self):
        if(self.skala < 2 ) :
            ket = "tidak terasa"
        elif(self.skala >= 2 and self.skala < 4) :
            ket = "Bangunan retak-retak"
        elif(self.skala >= 4 and self.skala < 6) :
            ket = "Bangunan roboh"
        else :
            ket = "Berpotensi tsunami"
        print(
            "Lokasi Gempa\t:",self.lokasi,
            "\nSkala\t\t:",self.skala,"richer"
            "\nDampak\t\t:",ket,
            "\n-------------------------------------"
        )
        
       


        



