# Program Pengelolaan Data Pelanggan E-Commerce

pelanggan = {}  # Dictionary: {id: {'nama': nama, 'alamat': alamat, 'total_pembelian': total}}

def tambah_pelanggan():
    id_pelanggan = input("Masukkan ID pelanggan unik: ").strip()
    if id_pelanggan in pelanggan:
        print("ID sudah ada.")
        return
    nama = input("Nama pelanggan: ").strip()
    alamat = input("Alamat pelanggan: ").strip()
    try:
        total_pembelian = float(input("Total pembelian awal: "))
        pelanggan[id_pelanggan] = {'nama': nama, 'alamat': alamat, 'total_pembelian': total_pembelian}
        print("Pelanggan ditambahkan.")
    except ValueError:
        print("Total pembelian harus angka.")

def update_pembelian():
    id_pelanggan = input("Masukkan ID pelanggan: ").strip()
    if id_pelanggan not in pelanggan:
        print("ID tidak ditemukan.")
        return
    try:
        pembelian_baru = float(input("Pembelian baru (akan ditambah ke total): "))
        pelanggan[id_pelanggan]['total_pembelian'] += pembelian_baru
        print("Total pembelian diupdate.")
    except ValueError:
        print("Pembelian harus angka.")

def tampil_pelanggan():
    id_pelanggan = input("Masukkan ID pelanggan: ").strip()
    if id_pelanggan not in pelanggan:
        print("ID tidak ditemukan.")
        return
    data = pelanggan[id_pelanggan]
    print(f"ID: {id_pelanggan}")
    print(f"Nama: {data['nama']}")
    print(f"Alamat: {data['alamat']}")
    print(f"Total Pembelian: Rp. {data['total_pembelian']:,.0f}")

def hapus_pelanggan():
    id_pelanggan = input("Masukkan ID pelanggan: ").strip()
    if id_pelanggan not in pelanggan:
        print("ID tidak ditemukan.")
        return
    del pelanggan[id_pelanggan]
    print("Pelanggan dihapus.")

def tampil_pelanggan_threshold():
    try:
        threshold = float(input("Masukkan threshold total pembelian (misalnya 50): "))
        filtered = {id: data for id, data in pelanggan.items() if data['total_pembelian'] > threshold}
        if not filtered:
            print(f"Tidak ada pelanggan dengan total pembelian > {threshold}.")
        else:
            print(f"Pelanggan dengan total pembelian > {threshold}:")
            print("-" * 50)
            for id, data in filtered.items():
                print(f"ID: {id}")
                print(f"Nama: {data['nama']}")
                print(f"Alamat: {data['alamat']}")
                print(f"Total Pembelian: Rp. {data['total_pembelian']:,.0f}")
                print("-" * 30)
    except ValueError:
        print("Threshold harus angka.")

def main():
    while True:
        print("\nMenu Pengelolaan Pelanggan:")
        print("1. Tambah Pelanggan")
        print("2. Update Pembelian")
        print("3. Tampil Pelanggan berdasarkan ID")
        print("4. Hapus Pelanggan")
        print("5. Tampil Pelanggan dengan Total Pembelian > Threshold")
        print("0. Keluar")
        try:
            pilihan = int(input("Pilih: "))
            if pilihan == 0:
                break
            elif pilihan == 1:
                tambah_pelanggan()
            elif pilihan == 2:
                update_pembelian()
            elif pilihan == 3:
                tampil_pelanggan()
            elif pilihan == 4:
                hapus_pelanggan()
            elif pilihan == 5:
                tampil_pelanggan_threshold()
            else:
                print("Invalid.")
        except ValueError:
            print("Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
