# Sniffer menggunakan Python di Window

## Latar Belakang Masalah 
Sniffing merupakan caa melihat seluruh paket data yang lewat pada sebuah media komunikasi yang terhubung dengan yang lain lalu paket - paket tersebut disusun ulang sehingga data dikirimkan yang dikirimkan oleh seseorang dapat dilihat oleh orang yang melakukan sniffer

## Penjelasan dan Solusi Masalah
Sniffing bisa koneksi yang bersifat broadcast dimana semua komputer host dalam sebuah jaringan akan menerima paket yang dikirimkan oleh sebuah komputer host. Ada 2 macam sniffing, yaitu :
1. Aktif
Kegiatan yang dapat melakukan perubahan paket data dalam jaringan . Alat yang digunakan sniffing aktif yaitu Switch yang bertugas menghindari bentrokan yang terjadi pada Hub dengan membaca MAC address komputer
2. Pasif
Kegiatan tanpa merubah data atau paket apapun dijaringan. Alat yang digunakan sniffing pasif yaitu Hub, karena Hub hanya bertugas meneruskan signal ke semua komputer (broadcast)

Contoh Sniffing di Kampus
Wifi kampus dipakai oleh dosen dan mahasiswa menggunakan laptop di dalam 1 akses point. Mahasiswa membuka sniffer di laptop, lalu dosen login dengan memakai hotspot itu artinya memakai paket dijaringan wifi kampus berupa HTML 4. Sniffer di laptop mahasiswa menangkap data tersebut. Mahasiswa memakai uset butuh login hotspot menggunakan akun dosen.

## Kesimpulan 
Sniffing adalah kegiatan membaca jaringan  ip paket dikirim ke jaringan lalu ke kabel

## Saran
Sebaiknya dalam melakukan sniffing perlu diperhatikan lebih dalam agar hak akses masuk ke dalam jaringan tidak diretas oleh orang lain

## Daftar Pustaka :
[1] https://docs.python.org/2/library/socket.html
[2] https://docs.python.org/2/library/struct.html

## Scan Plagiarisme
[1] https://drive.google.com/file/d/0B3mytGJbyhIhUWRuZXVQcU82YTA/view <br>
[2] https://drive.google.com/file/d/0B3mytGJbyhIhQVlmNWIxOUtjbEk/view