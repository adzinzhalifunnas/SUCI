<p align="center">
  <img src="https://i.ibb.co/Ttq052d/20211103-113304.png" width=500/><br>
  <img src="https://i.ibb.co/GQH0rxw/Screenshot-30.png" width=500/><br>
  <img src="https://i.ibb.co/1r8CnNY/Screenshot-27.png" width=500/><br>
  <img src="https://i.ibb.co/YbtDZDR/Screenshot-29.png" width=500/>
</p>

## Table of Contents
- [Apa Itu SUCI?](#apa-itu-suci)
- [Kenapa Harus Menggunakan SUCI?](#kenapa-harus-menggunakan-suci)
- [Fungsinya SUCI Apa?](#apa-fungsi-suci)
- [Meginstall Dan Menjalankan SUCI](#menginstall-dan-menjalankan-suci)
	- [Requirements](#requirements)
	- [Memilih Payment Gateway](#memilih-payment-gateway)
	- [Mensetting Environment Variabel](#mensetting-environment-variabel)
	- [Migrate](#migrate)
	- [Menjalankan Suci](#menjalankan-suci)
	- [Membuat User Untuk Login Admin](#membuat-user-untuk-login-admin)
	- [Memakai SUCI](#memakai-suci)
- [Mengubah Text Di SUCI](#mengubah-text-di-suci)

## Apa Itu SUCI?
SUCI adalah project open source yang bisa kamu cek disini.
Dibuat untuk memudahkan para content creator untuk mengumpulkan donasi/charity.
Tidak hanya untuk charity kamu juga bisa menggunakan SUCI untuk keuntungan pribadi ^_^.

## Kenapa Harus Menggunakan SUCI?
SUCI dibuat bukan untuk keuntungan author. Jadi author membuatnya sebisa mungkin "tanpa pajak".
Dengan menggunakan SUCI dana yang dikirim donatur akan langsung masuk ke payment gateway/rekening kamu tanpa campur tangan author ^_^.

## Apa Fungsi SUCI?
Kamu tau saweria? nah SUCI berfungsi seperti itu

## Menginstall Dan Menjalankan SUCI
### Requirements
- python 3.7+
- django 3.2.*
- module lainnya di requirements.txt
### Memilih Payment Gateway
ada dua payment gateway yang dipakai SUCI
#### 1. Tripay
daftar di https://tripay.co.id
- Kelebihan
	 - Pendaftaran mudah dan cepat
- Kekurangan
	- Pajak QRIS cukup besar 0.7% + Rp. 750
#### 2. Cekmutasi
daftar di https://cekmutasi.co.id
- Kelebihan
	- Pendaftaran mudah tanpa verifikasi identitas
	- Donasi langsung masuk ke rekening tanpa kriling
	- tanpa potongan pajak
- Kekurangan
	- Tidak support QRIS
	- Bayar harian
	- Memerlukan username dan password ibanking
### Mensetting Environment Variabel
#####	DEBUG
isi'True' jika development 'False' jika production
##### ALLOWED_HOSTS
diisi dengan domain website kamu, contoh: '127.0.0.1,salism3.herokuapp.com'
##### SECRET_KEY
diisi dengan password rahasia kamu
##### DATABASE_URL
isi dengan database url, contoh: 'postgres://USER:PASSWORD@HOST:PORT/NAME'
##### PUSHER_APP_ID
#### PUSHER_KEY
##### PUSHER_SECRET
##### PUSHER_CLUSTER
didapatkan di https://pusher.com
##### PAYMENT_GATEWAY
isi 'tripay' atau 'cekmutasi' sesuai pilihan kamu.
##### SANDBOX
isi 'True' jika sedang menggunakan sandbox payment gateway, 'False' jika sebaliknya
##### TRIPAY_MERCHANT_CODE
##### TRIPAY_API_KEY
##### TRIPAY_PRIVATE_KEY
skip langkah ini jika tidak menggunakan tripay. didapat dari https://tripay.co.id
##### CEKMUTASI_API_SIGNATURE
skip langkah ini jika tidak menggunakan cekmutasi, didapat dari https://cekmutasi.co.id
##### NOREK
skip langkah ini jika tidak menggunakan cekmutasi, isi dengan nomor rekening yang kamu daftarkan di cekmutasi
##### OWNERNAME
skip langkah ini jika tidak menggunakan cekmutasi, isi dengan nama pemilik rekening

### Migrate
```
python manage.py migrate
```

### Menjalankan SUCI
- development
 ```
 python manage.py runserver
```
- production
```
gunicorn suci.wsgi
```
### Membuat User Untuk Login Admin
```
python manage.py createsuperuser
```
login di https://domainkamu.com/admin

### Memakai SUCI
Setelah suci berjalan tambahkan url berikut ke obs dengan sumber browser.
- https://domainkamu.com/donation/notif (untuk melihat realtime orang yang berdonasi)
- https://domainkamu.com/donation/rank (untuk melihat peringkat donasi)
- https://domainkamu.com/donation/milestone (untuk melihat total donasi)
-  https://domainkamu.com/donation/qrcode (untuk mendapatkan qrcode)


## Mengubah Text Di Suci
Login ke admin dashboard di https://domainkamu.com/admin<br>
<img src="https://user-images.githubusercontent.com/50546233/140598278-ee5d6d14-759d-4615-a56d-78ec67d3aac0.png" width=500/><br>
