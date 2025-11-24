# Program Penghitungan Total Pendapatan Penjualan

# Data penjualan: list of dictionaries
data_penjualan = [
    {'produk': 'Laptop', 'jumlah_terjual': 5, 'harga_per_unit': 1000},
    {'produk': 'Mouse', 'jumlah_terjual': 20, 'harga_per_unit': 50},
    {'produk': 'Keyboard', 'jumlah_terjual': 10, 'harga_per_unit': 150},
    {'produk': 'Monitor', 'jumlah_terjual': 3, 'harga_per_unit': 500},
    {'produk': 'Printer', 'jumlah_terjual': 2, 'harga_per_unit': 800}
]

def hitung_dan_tampil():
    # Menggunakan list comprehension untuk menghitung total pendapatan per produk
    # dan filter hanya yang > 1000
    produk_filtered = [
        {
            'produk': item['produk'],
            'jumlah_terjual': item['jumlah_terjual'],
            'harga_per_unit': item['harga_per_unit'],
            'total_pendapatan': item['jumlah_terjual'] * item['harga_per_unit']
        }
        for item in data_penjualan
        if item['jumlah_terjual'] * item['harga_per_unit'] > 1000
    ]
    
    # Tampilkan hasil
    if not produk_filtered:
        print("Tidak ada produk dengan total pendapatan > 1000.")
    else:
        print("Produk dengan total pendapatan > 1000:")
        print("-" * 50)
        for item in produk_filtered:
            print(f"Produk: {item['produk']}")
            print(f"Jumlah Terjual: {item['jumlah_terjual']}")
            print(f"Harga Per Unit: Rp. {item['harga_per_unit']:,.0f}")
            print(f"Total Pendapatan: Rp. {item['total_pendapatan']:,.0f}")
            print("-" * 30)

# Jalankan program
if __name__ == "__main__":
    hitung_dan_tampil()
