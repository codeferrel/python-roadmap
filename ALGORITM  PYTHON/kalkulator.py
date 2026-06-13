angkah1=float(input("Masukkan angka pertama :"))
angkah2=float(input("Masukkan angka kedua :" ))


print("Masukkan pilihan")
print("1.bagi")
print("2.tambah")
print("3.Kurang")
print("4.mod")

pilihan=float(input("Masukkan Pilihan"))
if(pilihan==1):
    print(angkah1/angkah2)

elif(pilihan==2):
    print(angkah1+angkah2)

elif(pilihan==3):
    print(angkah1-angkah2)

elif(pilihan==4):
    print(angkah1%angkah2)

else:
    print("Input tidak terdaftar")