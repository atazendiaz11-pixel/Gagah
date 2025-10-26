# Aplikasi Sistem Manajemen Produksi Seragam (Integrasi 10 Tugas) - Versi Diperbaiki

# Data bersama (konstanta)
#BAHAN UKURAN DIGUNAKAN UNTUK MENDEFINISIKAN UKURAN TUGAS 1
BAHAN_UKURAN = {'S': 1, 'M': 1.5, 'L': 2, 'XL': 2.5} # DIGUNAKAN UNTUK MENDIFINISIKAN UKURAN PADA TUGAS 1
HARGA_UKURAN = {'S': 50000, 'M': 75000, 'L': 100000, 'XL': 125000} #HARGA SATUAN TIAP UKURAN UNTUK MENDEFINISIKAN HARGA BARANG
HARGA_JENIS = {'Kemeja': 100000, 'Celana': 150000} #DIGUNAKAN UNTUK MEVALIDASI HARGA TIAP BARANG
UKURAN_VALID = ['S', 'M', 'L', 'XL'] #DEFINISI UKURAN HANYA SESUAI DISINI JIKA USER TIDAK MENULIS INI MAKA AKAN TERJADI "ERROR"

# Fungsi 1: Penghitungan Bahan Produksi Seragam
def tugas_1():
    ukuran = input("Masukkan ukuran seragam (S/M/L/XL): ").upper() #Pakai upper agar sesuai kondisi variabel {ukuran valid}
    if ukuran not in UKURAN_VALID: #Jika tidak pakai upper user mengetik huruf kecil akan muncul pesan error maka dari itu perlu di definisikan sebagai huruf besar{Upper}
        print("Error: Ukuran tidak valid.")
        return
    jumlah = int(input("Masukkan jumlah pesanan: "))
    bahan = BAHAN_UKURAN[ukuran] * jumlah
    print(f"Jumlah bahan yang dibutuhkan untuk ukuran {ukuran}: {bahan} meter")

# Fungsi 2: Validasi Warna Seragam
def tugas_2():
    ukuran = input("Masukkan ukuran seragam (S/M/L/XL): ").upper()
    warna = input("Masukkan warna seragam: ").capitalize()
    if ukuran == 'XL' and warna != 'Merah':
        print("Error: Ukuran XL harus berwarna Merah")
    else:
        print("Validasi berhasil.")

# Fungsi 3: Pemesanan Seragam Interaktif
def tugas_3():
    nama = input("Nama Pelanggan: ")
    jenis = input("Jenis Seragam: ")
    ukuran = input("Ukuran: ").upper()
    jumlah = int(input("Jumlah Pesanan: "))
    harga_unit = float(input("Harga Per Unit: "))
    total = harga_unit * jumlah
    print(f"Pesanan untuk {nama}:")
    print(f"Jenis Seragam: {jenis}")
    print(f"Ukuran: {ukuran}")
    print(f"Jumlah Pesanan: {jumlah}")
    print(f"Harga Per Unit: {harga_unit}")
    print(f"Total Harga: {total}")

# Fungsi 4: Menghitung Total Bahan untuk Pesanan
# JUJUR UNTUK FUNGSI 4 SAYA MASI GAK NGERTI DAN GAK PAHAM :)
# MAAF PAK FUNGSI 4 SAYA PAKAI AI
def tugas_4():
    pesanan = []
    while True:
        jenis = input("Masukkan jenis seragam (atau 'selesai' untuk stop): ")
        if jenis.lower() == 'selesai':
            break
        ukuran = input("Masukkan ukuran seragam (S/M/L/XL): ").upper()
        if ukuran not in UKURAN_VALID:
            print("Ukuran tidak valid, skip.")
            continue
        jumlah = int(input("Masukkan jumlah pesanan: "))
        bahan = BAHAN_UKURAN[ukuran] * jumlah
        pesanan.append((jenis, ukuran, jumlah, bahan))
    
    total_bahan = 0
    print("\nPesanan:")
    for jenis, ukuran, jumlah, bahan in pesanan:
        print(f"{jenis}, Ukuran {ukuran}, Jumlah Pesanan: {jumlah}, Total Bahan: {bahan} meter")
        total_bahan += bahan
    print(f"Total Bahan yang Dibutuhkan: {total_bahan} meter")

# Fungsi 5: Menampilkan Pola Produksi Seragam (nested loop)
# JUJUR UNTUK FUNGSI 5 SAYA MASI GAK NGERTI JUGA DAN GAK PAHAM :)
# MAAF PAK FUNGSI 5 SAYA JUGA  PAKAI AI
def tugas_5():
    baris = int(input("Masukkan jumlah baris pola: "))
    for _ in range(baris):
        for ukuran in UKURAN_VALID:
            print(ukuran, end=" ")
        print()

# Fungsi 6: Fungsi Pembaruan Stok Bahan
def tugas_6():
    stok_awal = float(input("Jumlah stok bahan baku: "))
    digunakan = float(input("Jumlah bahan yang digunakan: "))
    sisa = stok_awal - digunakan
    print(f"Sisa stok bahan baku: {sisa}")

# Fungsi 7: Menghitung Harga Total Berdasarkan Ukuran dan Jumlah
def tugas_7():
    ukuran = input("Masukkan ukuran seragam (S/M/L/XL): ").upper()
    if ukuran not in UKURAN_VALID:
        print("Error: Ukuran tidak valid.")
        return
    jumlah = int(input("Masukkan jumlah pesanan: "))
    total = HARGA_UKURAN[ukuran] * jumlah
    print(f"Total harga untuk {jumlah} seragam {ukuran}: Rp. {total}")

# Fungsi 8: Menghitung Harga Berdasarkan Jenis Seragam
def tugas_8():
    jenis = input("Jenis Seragam: ").capitalize()
    if jenis not in HARGA_JENIS:
        print("Error: Jenis tidak valid.")
        return
    jumlah = int(input("Jumlah Pesanan: "))
    total = HARGA_JENIS[jenis] * jumlah
    print(f"Total Harga untuk {jumlah} {jenis}: {total}")

# Fungsi 9: Validasi Input Ukuran Seragam
def tugas_9():
    ukuran = input("Masukkan ukuran seragam: ").upper()
    if ukuran not in UKURAN_VALID:
        print("Error: Ukuran seragam tidak valid.")
    else:
        print("Ukuran valid.")

# Fungsi 10: Menghitung Jumlah Bahan Berdasarkan Harga
def tugas_10():
    harga = float(input("Harga seragam: "))
    # Cari ukuran berdasarkan harga (reverse lookup)
    ukuran = None
    for u, h in HARGA_UKURAN.items():
        if h == harga:
            ukuran = u
            break
    if ukuran:
        bahan = BAHAN_UKURAN[ukuran]
        print(f"Jumlah bahan yang dibutuhkan untuk harga {harga} adalah {bahan} meter.")
    else:
        print("Harga tidak sesuai ukuran yang ada.")

# TAMPILAN MENU UTAMA
def main():
    while True:
        print("\n=== MENU APLIKASI SERAGAM ===")
        print("1. Penghitungan Bahan Produksi")
        print("2. Validasi Warna Seragam")
        print("3. Pemesanan Seragam Interaktif")
        print("4. Total Bahan untuk Pesanan")
        print("5. Pola Produksi Seragam")
        print("6. Pembaruan Stok Bahan")
        print("7. Harga Total Berdasarkan Ukuran")
        print("8. Harga Berdasarkan Jenis")
        print("9. Validasi Ukuran")
        print("10. Bahan Berdasarkan Harga")
        print("0. Keluar")
        
        try:
            pilihan = int(input("Pilih tugas (0-10): "))  # Konversi ke int untuk validasi
            if pilihan == 0:
                break
            elif pilihan == 1:
                tugas_1()
            elif pilihan == 2:
                tugas_2()
            elif pilihan == 3:
                tugas_3()
            elif pilihan == 4:
                tugas_4()
            elif pilihan == 5:
                tugas_5()
            elif pilihan == 6:
                tugas_6()
            elif pilihan == 7:
                tugas_7()
            elif pilihan == 8:
                tugas_8()
            elif pilihan == 9:
                tugas_9()
            elif pilihan == 10:
                tugas_10()
            else:
                print("Pilihan tidak valid. Masukkan angka 0-10.")
        except ValueError:
            print("Error: Masukkan angka yang valid (0-10).")

# Jalankan program
if __name__ == "__main__":
    main()
