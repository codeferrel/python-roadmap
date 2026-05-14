def sapa_user(nama):

    print(f"Hallo {nama},selamat belajar python ")
sapa_user("Bro")

def cek_diskon(total_belanja):
    if total_belanja >= 100000:
        potongan = total_belanja * 0.1  # Diskon 10%
        return total_belanja - potongan
    else:
        return total_belanja

# Menggunakan hasil fungsi untuk perhitungan lain
harga_akhir = cek_diskon(150000)
print(f"Total yang harus dibayar: Rp{harga_akhir}")