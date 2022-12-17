from Animals import Animals


animal = Animals(["guguk", "meong", "singa"])

#enampilkan semua data animals
animal.index()
print()
#menampilkan animals dengan index : urutan

print("Menampilkan animals dengan index")
animal.show(2)
print()


# Menambahkan data animals
print("Menambahkan data animals")
animal.store("unta")
print()

#Mengubah data animals
print("Mengubah data animal")
animal.update(1, "gorila")
print()

#Menghapus data animals
print("Menghapus data animal")
animal.delate(0)
print()