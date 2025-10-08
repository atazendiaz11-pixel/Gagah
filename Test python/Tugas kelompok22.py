#sistem absensi
print("Kehadiran siswa!")

kehadiran = input("Masukkan status kehadiran (hadir/izin/alfa): ").lower()

input_hadir = "hadir"
input_izin = "izin"
input_alfa = "alfa"

if kehadiran == input_hadir:
    print("Kehadiran dicatat")
elif kehadiran == input_izin:
    print("Izin tercatat, harap lengkapi surat izin!")
elif kehadiran == input_alfa:
    print("Tidak hadir tanpa keterangan! ")
else:
    print("Input tidak dikenali")
