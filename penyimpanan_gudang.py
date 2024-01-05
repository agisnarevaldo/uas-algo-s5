# Nama : Muhamad Agisna Revaldo
# NIM  : 2203010405
# Inisialisasi gudang sebagai dictionary untuk menyimpan informasi barang
gudang = {}

# Fungsi untuk menambahkan barang ke gudang
def tambah_barang(kode, nama, jumlah):
    if kode not in gudang:
        gudang[kode] = {'nama': nama, 'jumlah': jumlah}
        print(f"Barang dengan kode {kode} berhasil ditambahkan ke gudang.")
    else:
        print("Barang dengan kode tersebut sudah ada di gudang.")

# Fungsi untuk mencari barang berdasarkan nama atau kode barang
def cari_barang():
    kata_kunci = input("Masukkan nama atau kode barang yang ingin dicari: ")
    ditemukan = False
    for kode, info in gudang.items():
        if kata_kunci.lower() in info['nama'].lower() or kata_kunci.lower() == kode.lower():
            print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}")
            ditemukan = True
    if not ditemukan:
        print("Barang tidak ditemukan.")

# Fungsi untuk memperbarui stok barang
def update_stok(kode, jumlah):
    if kode in gudang:
        gudang[kode]['jumlah'] = jumlah
        print(f"Stok barang dengan kode {kode} berhasil diubah.")
        print(f"Stok saat ini: {gudang[kode]['jumlah']}")
    else:
        print("Barang dengan kode tersebut tidak ditemukan di gudang.")
        
# Fungsi untuk menghapus barang dari gudang
def hapus_barang(kode):
    if kode in gudang:
        del gudang[kode]
        print(f"Barang dengan kode {kode} berhasil dihapus dari gudang.")
    else:
        print("Barang dengan kode tersebut tidak ditemukan di gudang.")

# Fungsi untuk menampilkan seluruh barang di gudang
def tampilkan_barang():
    if gudang:
        print("Daftar Barang di Gudang:")
        for kode, info in gudang.items():
            print(f"Kode: {kode}, Nama: {info['nama']}, Jumlah: {info['jumlah']}")
    else:
        print("Gudang kosong.")

# Fungsi untuk menghitung total nilai semua barang di gudang
def hitung_total_nilai():
    total = 0
    for kode, info in gudang.items():
        total += info['jumlah']
    print(f"Total nilai semua barang di gudang: {total}")

# Main program
while True:
    print("\n=== PROGRAM MANAJEMEN GUDANG ===")
    print("1. Tambah Barang")
    print("2. Tampilkan Barang")
    print("3. Cari Barang")
    print("4. Edit Stok Barang")
    print("5. Hapus Barang")
    print("6. Hitung Total Nilai Barang")
    print("7. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

    if pilihan == '1':
        kode = input("Masukkan kode barang: ")
        nama = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah barang: "))
        tambah_barang(kode, nama, jumlah)
    elif pilihan == '2':
        tampilkan_barang()
    elif pilihan == '3':
        cari_barang()
    elif pilihan == '4':
        kode_barang = input("Masukkan kode barang yang akan diperbarui stoknya: ")
        jumlah_baru = int(input("Masukkan jumlah baru untuk stok barang tersebut: "))
        update_stok(kode_barang, jumlah_baru)
    elif pilihan == '5':
        kode = input("Masukkan kode barang yang akan dihapus: ")
        hapus_barang(kode)
    elif pilihan == '6':
        hitung_total_nilai()
    elif pilihan == '7':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")
