from gempa import *
#buat object
g1 = gempa("Banten",1.2)
g2 = gempa("Palu",6.1)
g3 = gempa("Cianjur",5.6)
g4 = gempa("Jayapura",3.3)
g5 = gempa("Garut",4.0)

#panggil fungsi di class Gempa
g1.dampak()
g2.dampak()
g3.dampak()
g4.dampak()
g5.dampak()