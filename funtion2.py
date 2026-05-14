def ringkasan_transaksi(nama_toko, *item, **detail_tambahan):
    print(f"--- Nota {nama_toko} ---")
    
    # Memproses banyak item sekaligus dengan List Comprehension
    list_item = [f"- {i.capitalize()}" for i in item]
    print("\n".join(list_item))
    
    print("\nDetail Pengiriman:")
    for kunci, nilai in detail_tambahan.items():
        print(f"{kunci.replace('_', ' ').title()}: {nilai}")

# Memanggil fungsi dengan jumlah argumen fleksibel
ringkasan_transaksi("Toko Maju Jaya", 
                    "laptop", "mouse", "keyboard", 
                    alamat="Jakarta", kurir="JNE", estimasi="2 Hari")