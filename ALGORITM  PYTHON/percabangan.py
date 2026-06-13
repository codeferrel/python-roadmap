# Menggunakan eval atau int agar input terbaca sebagai angka
total_belanja = int(input("Masukkan total belanja : "))
# Inisialisasi variabel awal
diskon = 0

if total_belanja > 100000:
    print("Kamu mendapatkan bonus minuman")
    print("Dan diskon 5%")
    # Hitung diskon hanya jika belanja > 100.000
    diskon = total_belanja * 5/100
else:
    print("Belanja lagi yuk biar dapat bonus!")
    diskon = 0

# Hitung total yang harus dibayar
bayar = total_belanja - diskon

print(f"Total yang harus dibayar: {bayar}")
print("Terima kasih telah berbelanja")
print("Datang lagi yah!\n")


# cek umur 
umur=int(input("Masukkan umur anda :"))
if umur <17 :
    print("Anda tidak bisa membuat sim")
else:
    print(f"anda  bisa membuat sim")