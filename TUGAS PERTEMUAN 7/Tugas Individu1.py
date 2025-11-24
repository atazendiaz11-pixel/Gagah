# Aplikasi Sistem Inventaris Barang

inventaris = {}  # Dictionary: {id: {'nama': nama, 'stok': stok, 'harga': harga}}

def tambah_barang():
    id_barang = input("Masukkan ID barang unik: ").strip()
    if id_barang in inventaris:
        print("ID sudah ada.")
        return
    nama = input("Nama barang: ").strip()
    try:
        stok = int(input("Jumlah stok: "))
        harga = float(input("Harga per unit: "))
        inventaris[id_barang] = {'nama': nama, 'stok': stok, 'harga': harga}
        print("Barang ditambahkan.")
    except ValueError:
        print("Stok dan harga harus angka.")

def update_stok():
    id_barang = input("Masukkan ID barang: ").strip()
    if id_barang not in inventaris:
        print("ID tidak ditemukan.")
        return
    try:
        stok_baru = int(input("Stok baru: "))
        inventaris[id_barang]['stok'] = stok_baru
        print("Stok diupdate.")
    except ValueError:
        print("Stok harus angka.")

def tampil_info():
    id_barang = input("Masukkan ID barang: ").strip()
    if id_barang not in inventaris:
        print("ID tidak ditemukan.")
        return
    barang = inventaris[id_barang]
    print(f"ID: {id_barang}")
    print(f"Nama: {barang['nama']}")
    print(f"Stok: {barang['stok']}")
    print(f"Harga: Rp. {barang['harga']:,.0f}")

def hapus_barang():
    id_barang = input("Masukkan ID barang: ").strip()
    if id_barang not in inventaris:
        print("ID tidak ditemukan.")
        return
    del inventaris[id_barang]
    print("Barang dihapus.")

def main():
    while True:
        print("\nMenu Inventaris:")
        print("1. Tambah Barang")
        print("2. Update Stok")
        print("3. Tampil Info Barang")
        print("4. Hapus Barang")
        print("0. Keluar")
        try:
            pilihan = int(input("Pilih: "))
            if pilihan == 0:
                break
            elif pilihan == 1:
                tambah_barang()
            elif pilihan == 2:
                update_stok()
            elif pilihan == 3:
                tampil_info()
            elif pilihan == 4:
                hapus_barang()
            else:
                print("Invalid.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
