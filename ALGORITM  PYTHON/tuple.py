
# A tuple is created by placing all the items inside parentheses (), separated by commas. A tuple can have any number of items.

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


###########################################
# Dictionary dengan tuple sebagai key
lokasi_points = {
    (1, 2): "Point A",
    (3, 4): "Point B",
    (5, 6): "Point C"
}

# Mengakses nilai
print(lokasi_points[(1, 2)])  # Output: "Point A"

# Contoh kompleks: mapping koordinat ke informasi
peta_kota = {
    (3.595, 98.678): "Kantor Pusat",
    (3.597, 98.680): "Gudang Utama",
    (3.600, 98.675): "Cabang Timur"
}

#######################################
