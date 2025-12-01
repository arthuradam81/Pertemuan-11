data_mahasiswa = {}

def tambah():
    nama = input("Masukkan nama: ")
    nilai = float(input("Masukkan nilai: "))
    data_mahasiswa[nama] = nilai
    print("Data berhasil ditambahkan.\n")

def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data.\n")
    else:
        print("\nDaftar Nilai Mahasiswa:")
        for nama, nilai in data_mahasiswa.items():
            print(f"- {nama}: {nilai}")
        print()

def hapus(nama):
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data {nama} berhasil dihapus.\n")
    else:
        print("Nama tidak ditemukan.\n")

def ubah(nama):
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan nilai baru: "))
        data_mahasiswa[nama] = nilai_baru
        print(f"Data {nama} berhasil diubah.\n")
    else:
        print("Nama tidak ditemukan.\n")


# Program utama
while True:
    print("Menu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Ubah data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        hapus(input("Masukkan nama yang ingin dihapus: "))
    elif pilihan == "4":
        ubah(input("Masukkan nama yang ingin diubah: "))
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.\n")
