# Pertemuan-11

# Penjelasan

# Latihan-1

a = lambda x: x2**
Mengembalikan kuadrat dari nilai x.
Contoh: a(5) → 25.
b = lambda x, y: math.sqrt(x² + y²)
Menghitung jarak dua dimensi (rumus Pythagoras).
Contoh: b(3, 4) → 5.
*c = lambda args: sum(args)/len(args)
Menghitung nilai rata-rata dari banyak angka (bisa 2, 3, atau lebih).
Contoh: c(2, 4, 6) → 4.
d = lambda s: "".join(set(s))
Menghapus karakter duplikat dari string.
set() menghilangkan duplikasi tanpa mempertahankan urutan.
Contoh:
d("banana") → "ban" atau "nba" (urutan acak).

# Praktikum-6

1. tambah()
Digunakan untuk menambah data mahasiswa berupa:
nama
nilai
Data disimpan ke dictionary bernama data_mahasiswa.
2. tampilkan()
Menampilkan seluruh isi data mahasiswa dalam bentuk:
nama : nilai
Jika kosong akan muncul pesan Belum ada data.
3. hapus(nama)
Menghapus data mahasiswa berdasarkan nama yang dimasukkan.
4. ubah(nama)
Mengubah nilai mahasiswa berdasarkan nama yang diberikan.
Alur Program
Program akan menampilkan menu.
Pengguna memilih menu: tambah, tampilkan, ubah, hapus, atau keluar.
Proses sesuai fungsi.
Kembali ke menu sampai pengguna memilih keluar.
