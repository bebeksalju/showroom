# Assessment Junior Programmer

Membuat aplikasi manajemen showroom sederhana dengan menggunakan fitur CRUD, pembiayaan bank, dan riwayat servis.  

## API
```bash
GET / # Daftar mobil
GET /tambah/ # Form tambah mobil
GET /<mobil_id>/ # Detail mobil
GET /<mobil_id>/service/ # Form tambah service
POST /<mobil_id>/edit/ # Edit mobil
POST /<mobil_id>/ # Simpan mobil baru
POST /<mobil_id>/service/ # Simpan service baru
POST /<mobil_id>/hapus/ # Hapus mobil
```

## Database
Menggunakan SQLite untuk menyimpan data (bawaan Django).
