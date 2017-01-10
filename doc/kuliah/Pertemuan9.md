##  Intrusion Detection System (IDS) dan Intrusion Prevention System (IPS)

# Latar Belakang Masalah 
Intrusion Detection System (IDS) adalah sebuah metode yang dapat digunakan untuk mendeteksi aktivitas yang mencurigakan dalam sebuah sistem atau jaringan. Intrusion Prevention System (IPS) adalah kombinasi antara fasilitas blocking dari firewall dan kedalaman inspeksi paket data dari Intrusion Detection System (IDS).

# Permasalahan dan Solusi Masalah
IDS dapat melakukan inspeksi terhadap lalu lintas inbound dan outbound dalam sebuah sistem atau jaringan, melakukan analisis dan mencari bukti dari percobaan intrusi (penyusupan). IPS membuat akses kontrol dengan cara melihat konten aplikasi, darpada melihat IP Address atau port yang biasa dilakukan oleh firewall.
 
Ada 2 jenis IDS,yaitu :
1. Network-based intrusion detection system (NIDS) 
Semua lalu lintas yang megalir ke sebuah jaringan akan dianalisis apakah ada percobaan perseorangan atau penyusupan ke dalam sistem jaringan 
2. Host-based intrusion detection system (HIDS)
Aktivitas sebuah host jaringan individual akan dipantau apakah terjadi sebuah percobaan serangan atau penyusupan kedalamnya ataua tidak

Ada 2 jenis IPS, yaitu :
1. Host-based intrusion prevention system (HIPS)
System pencegahan yang terdiri dari banyak layer menggunakan packet filtering, inspeksi status dan metode pencegahan intrusi yang bersifat real-time untuk menjaga host berada dibawah keadaan dari efisiensi performansi yang layak
2. Network-based intrusion prevention system (NIPS)
Mengawasi isi dari paket-paket yang berlalu lalang dan mencari urutan yang unik dari paket-paket tersebut 
 
* Cara kerja IDS
Menggunakan pendeteksian berbasis signature yang melibatkan percocokan lalu lintas jaringan dengan basis data berisi cara-cara serangan dan penyusupan yang sering dilakukan oleh penyerang
 
* Cara kerja IPS
 Menerapkan kebijakan kntrol akses yang memeriksa trafik data yang lalu lalang dan memblok paket data yang tidak sesuai dengan kebijakan keamanan

# Kesimpulan  
IDS dan IPS dapat melakukan pencegahan dan pendeteksi dalam sistem keamanan jaringan

# Saran 
Sebaiknya selalu diadakan praktik setiap minggu agar mahasiswa dapat lebih mengetahui tentang materi keamanan jaringan