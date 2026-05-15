def sapa_user(nama_user):
    """Fungsi untuk menyapa user."""
    print(f"Hallo {nama_user}, Welcome to Python!")

# 1. Input jumlah perulangan dari user
jumlah = int(input("Ingin melakukan pengecekan berapa kali? "))

# 2. Proses perulangan
for i in range(jumlah):
    print(f"\n--- Data ke-{i + 1} ---")
    
    # Input data
    nama = input("Masukkan nama anda: ")
    umur = int(input("Masukkan umur anda: "))

    # Memanggil fungsi sapa
    sapa_user(nama)

    # Logika pengecekan KTP
    if umur >= 17:
        print(f"Hasil: {nama}, Anda sudah bisa punya KTP.")
    else:
        print(f"Hasil: {nama}, Anda belum bisa punya KTP.")

print("\n--- Program Selesai ---")