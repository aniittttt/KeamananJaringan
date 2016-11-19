# Denial of System


## Latar Belakang Masalah
Denial of Service (DOS) adalah salah satu bentuk serangan dalam jaringan yang bertujuan mematikan pelayanan dari komputer atau jaringan komputer yang diserang


## Permasalahan dan Solusi Masalah
Serangan DOS ini sulit dideteksi, kecuali jika penyerang menggunakan alamat IP yang sama secara berulang-ulang. Tapi saat ini serangan DOS bisa diatasi oleh provider-provider besar dengan cara meng-upgrade patch-patch yang bolong dan juga menambah bandwitch

 
Denial of System :

1. Melayani permintaan

2. Misal x adalah batas maximal jumlah yang bisa dijalani

3.  Jika x+n permintaan maka yang jalan tidak terlayani atau denied

 
Cara Pencegahan :

1.  Menaikan kapasitas layanan tetapi client 2 juga menaikan permintaan server

2. Memblok IP penyerang di firewall

3. Memasukan semua IP penyerang

4. Honeypot dibuat coding


Contoh Denial Of System :

Client 2 request sebesar x dan client 1 request sebesar n. Maka client 2 terlayani dan client 1 denied, karena melebihi kapasitas server. Jika yang request tidak hanya client 2 tetapi ada client yang lain maka disebut distributor DOS.


## Kesimpulan
Jika semua cara sudah dilakukan dan putus asa tidak masuk ke system, maka cara terakhir adalah membuat server sibuk sendiri  sehingga server tidak melayani permintaan yang lain


## Saran
Apabila melakukan suatu akses ke dalam URL di dalam server yang lain sebaiknya berhati-hati agar tidak terjadi Denial of Sistem (DOS)
