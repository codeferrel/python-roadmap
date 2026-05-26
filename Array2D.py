# Membuat array 2 dimensi
array_input = [
    [10, 12, 14],
    [0, 1, 2]
]

# Menampilkan seluruh baris
print(array_input[0])   # baris pertama
print(array_input[1])   # baris kedua

print()

# Mengakses elemen tertentu
print("Elemen baris 0 kolom 0 :", array_input[0][0])
print("Elemen baris 0 kolom 1 :", array_input[0][1])
print("Elemen baris 1 kolom 2 :", array_input[1][2])

print()

# Menampilkan semua isi array menggunakan perulangan
print("Semua isi array :")

for baris in array_input:
    for kolom in baris:
        print(kolom, end=" ")
    print()

print()

# Menambahkan data baru ke dalam array
array_input.append([5, 6, 7])

print("Array setelah ditambah :")
print(array_input)

print()

# Mengubah nilai array
array_input[0][1] = 100

print("Array setelah diubah :")
print(array_input)