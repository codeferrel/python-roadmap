from typing import Any

def cetak_nota_digital(nama_toko: str, *items: str, **informasi: Any) -> None:
    
    # Header dengan format string yang presisi
    print(f"{' NOTA PEMBELIAN ':=^40}")
    print(f"Merchant: {nama_toko.upper()}")
    print("-" * 40)

    # Memproses item (List Comprehension)
    # Jika tidak ada item, berikan pesan default
    daftar_belanja = [f"• {item.title():<20}" for item in items]
    print("\n".join(daftar_belanja) if items else "Tidak ada item.")

    # Memproses detail tambahan (Dictionary Unpacking)
    if informasi:
        print(f"\n{' INFORMASI PENGIRIMAN ':-^40}")
        for kunci, nilai in informasi.items():
            label = kunci.replace('_', ' ').capitalize()
            print(f"{label:<15} : {nilai}")
    
    print("=" * 40)

# Pemanggilan fungsi
cetak_nota_digital(
    "Toko Maju Jaya", 
    "laptop", "mouse", "keyboard", "monitor ultra-wide",
    alamat_tujuan="Jakarta Selatan", 
    jasa_kurir="Sicepat Express", 
    estimasi_tiba="Esok Hari"
)