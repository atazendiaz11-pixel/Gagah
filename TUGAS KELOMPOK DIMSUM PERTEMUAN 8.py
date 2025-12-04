# Program Binary Search untuk Kasus String (Mencari Kata dalam List Terurut) - Diperbaiki

# List kata terurut (diubah ke lowercase untuk konsistensi case-insensitive)
kata_list = ["jelek", "dadang", "danang", "dean", "ganteng", "dudung"]

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Tidak ditemukan
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid  # Ditemukan, return index
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Cari di kiri
    else:
        return binary_search(arr, target, mid + 1, high)  # Cari di kanan

def main():
    if not kata_list:
        print("List kata kosong.")
        return
    
    print("List kata terurut:", kata_list)
    target = input("Masukkan kata yang ingin dicari (misalnya 'dean' atau 'ganteng'): ").strip().lower()
    
    if not target:
        print("Input kata tidak boleh kosong.")
        return
    
    # Jalankan Binary Search
    result = binary_search(kata_list, target, 0, len(kata_list) - 1)
    
    if result != -1:
        print(f"Kata '{target}' ditemukan di index {result}.")
    else:
        print(f"Kata '{target}' tidak ditemukan dalam list.")

if __name__ == "__main__":
    main()
