total_belanja = 0
nomor_barang = 1

print("=== PROGRAM KASIR SEDERHANA ===")
print("Ketik '0' jika sudah selesai memasukkan semua harga barang.\n")
while True:

    harga = int(input(f"Masukkan harga barang ke-{nomor_barang}: Rp "))
  
    if harga == 0:
        print("\nInput selesai. Menghitung total...")
        break 
  
    if harga < 0:
        print("Harga tidak boleh minus! Silakan masukkan ulang.")
        continue 
    
    total_belanja += harga
    nomor_barang += 1 
print("-" * 30)
print(f"Total yang harus dibayar: Rp {total_belanja:,}")
print("Terima kasih telah berbelanja!") 
