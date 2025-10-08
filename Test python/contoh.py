harga_barang = [100000, 200000, 150000, 100000, 100000, 100000] 
total_belanja = 0  
for harga in harga_barang: 
    total_belanja += harga 
if total_belanja >= 500000:
    potongan = total_belanja * 0.1
    total_akhir = total_belanja - potongan
    print(f"Total belanja sebelum diskon: Rp {total_belanja}")
    print(f"Diskon 10%: Rp {potongan}")
    print(f"Total belanja setelah diskon: Rp {total_akhir}")
else:
    print(f"Total belanja: Rp {total_belanja} (Tidak ada diskon, minimal Rp 500.000)")
