# TUGAS INDIVIDU
Nama: M Naufal Zhafran Rabiul Batara

NPM: 2406361694

Kelas: F

<details>
   <summary>
      Tugas 2
   </summary>
   Link: https://m-naufal41-elgasingshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   - Membuat sebuah proyek Django baru.
langkah pertama saya membuat direktori baru bernama footballshop lalu saya       masuk kedalam direktori tersebut menggunakan command "cd footballshop" lalu     setelah itu saya membuat virtual environment dan mengaktifkannya, tujuannya agar package dan dependencies dari projek kita tidak nabrak dengan versi lain yang terinstall di komputer saya, setelah itu saya menyiapkan dependencies yang ingin saya gunakan di requirements.txt lalu menginstalasi dependencies tersebut dengan menggunakan command "pip install -r requirements.txt" lalu setelah itu baru saya membuat projek djangonya yang bernama football_shop dengan perintah "django-admin startproject football_shop ."

   - Membuat aplikasi dengan nama main pada proyek tersebut.
     menggunakan command "python manage.py startapp main" 
     
   -Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    mendaftarkannya ke INSTALLED_APPS di settings.py

    -Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut.
   pertama saya buka file models.py di main lalu saya mengisi filenya seperti di tutorial namun saya mengganti isi pilihan categorynya sesuai dengan kebutuhan saya yaitu toko bola jadi saya menggantinya dengan jenis item yang ingin saya jual lalu saya mendefine id field bertipe UUIDField yang digunakan sebagai primary key, name field bertipe charfield untuk nama item yang akan saya jual dengan panjang maksimal 255 char, price field bertipe integerfield yang menyimpan harga dari item, description field bertipe textfield yang menyimpan deskripsi dari item yang akan dijual, thumbnail field bertipe URL yang menyimpan URL gambar thumbnail item, category field bertipe charfield untuk menyimpan kategori dari item, is_featured untuk menentukan apakah item ini akan ditampilkan sebagai barang unggulan atau tidak, created_at yang otomatis berisi tanggal dan waktu saat data dibuat, dan yang terakhir method __str__ yang emngembalikan representasi string dari nama dan harga item.

-Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
di view saya membuat variable npm nama kelas nama projek yang akan saya gunakan di template html saya

-Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
proses mengonfirugasi routing diawali dengan membuat file urls.py di main lalu membuat urlpatterns (list berisi objek URLPATTERN yang dihasilkan fungsi path()) tidak lupa juga menambahkan urls yang kita buat tadi di main ke urlpatterns di urls.py direktori djangonya (football_shop).

-Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
buka web pws lalu create new project (elgasingshop) setelah itu saya mengisi tab environs sesuai dengan isi .env.prod project saya lalu menambahkan url deployment pws ke allowed host setelah itu saya jalankan perintah yang terdapat di project command lalu mengisi git credential manager setelah itu saya push dan selesai.

2. <img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/bf8fd7bb-71d6-4fa3-a7c1-762a1e06fd14" />
source: https://www.dothedev.com/blog/what-is-django-used-for/

 -urls.py berfungsi untuk menentukan ke mana request HTTP diarahkan. saat user mengakses URL di browser, django memeriksa urlpattern di urls.py jika ada yang cocok, request diteruskan ke fungsi tertentu di views.py
 -views.py berfungsi untuk menangani request dan menentukan respon. awalnya dia menerima request dari urls.py setelah itu mengambil data dari models.py lalu memilikih template HTML untuk response.
- models.py berfungsi sebagai representasi database. models.py berisi class yang mempresentasikan tabel di database, lalu views.py menggunakan model ini untuk membaca/menulis data dari atau ke databse.
- template berfungsi untuk menyusun tampilan yang akan dikirim ke user. template menerima data dari views.py lalu menggabungkan data ke dalam HTML lalu hasil akhirnya adalah HTML response yang dikirim ke browser.

3. ada banyak peran dan fungsi settings.py yang pertama menentukan jenis database yang digunakan dan cara menghubungkannya, berisi daftar aplikasi django yang aktif dan akan digunakan dalam proyek, berisi daftar domain yang diperbolehkan mengakses app, mengatur direktori yang digunakan untuk memproses template HTML.


4. Bagaimana cara kerja migrasi database di Django?
   migrasi database di gjango adalah proses untuk membuat dan mengubah struktur database. django memakai 2 command, yang pertama "python manage.py makemigrations" yang berfungsi membaca perubahan di models.py dan membuat folder migrations, yang kedua "python manage.py migrate" yang berfungsi untuk menjalankan file migration yang sudah dibuat ke database, django akan membuat atau mengubah tabel di database sesuai intruksi migration

5. dalam software development menurut saya lebih baik untuk mempelajari backend terlebih dahulu karena frontend menurut saya adalah hal yang mudah dipelajari bahkan bisa dengan bantuan AI, tidak dengan backend yang berisi logic yang rumit dan berhubungan databse yang dimana bersifat pribadi jadi menurut saya kita harus paham backend terlebih dahulu. namun kenapa harus memakai Django? karena yang pertama django menggunakan bahasa python yang dimana bahasa yang paling mudah untuk dipahami (mendekati bahasa manusia) lalu django menggunakan pola MVT dimana sangat bagus untuk belajar memisahkan logika view, data, dan tampilan yang merupakan dasar dari software development.

6. amann

   






   


   
</details>


<details>
   <summary>Tugas 3: Implementasi Form dan Data Delivery pada Django</summary>


1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan agar data dari server dapat diakses oleh client atau aplikasi lain dalam format yang terstandarisasi. hal ini memungkinkan aplikasi untuk:
- Melakukan integrasi dengan sistem lain.
- Mengirim dan menerima data secara real-time.
- Memisahkan logika backend dan frontend, sehingga frontend bisa mengambil data tanpa harus terikat dengan template HTML.

2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- XML cocok untuk data yang memiliki struktur kompleks dan membutuhkan validasi ketat.  
- sedangkan JSON Lebih ringkas, mudah dibaca manusia maupun mesin, lebih cepat diparsing, dan sudah menjadi standar dalam komunikasi API modern.  
JSON lebih populer karena lebih efisien, simpel, dan didukung luas di berbagai bahasa pemrograman.

3. Fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkannya?
Method is_valid() digunakan untuk:
- Mengecek apakah data yang dikirim user melalui form sesuai dengan aturan yang didefinisikan di model atau form.
- Menghindari error ketika data disimpan ke database.
kita membutuhkan is_valid() karena tanpa is_valid(), data yang tidak sesuai bisa masuk ke database dan menimbulkan inkonsistensi.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkannya?
- csrf_token digunakan untuk mencegah CSRF (Cross-Site Request Forgery), yaitu serangan di mana penyerang mencoba mengirim permintaan palsu ke server dengan identitas user yang sedang login.
- Jika csrf_token tidak ditambahkan, form Django akan ditolak secara default (Forbidden 403).
- Tanpa proteksi ini, penyerang bisa mengeksploitasi user yang sedang login untuk melakukan aksi berbahaya, misalnya menghapus data atau melakukan transaksi tanpa izin.

5. Bagaimana cara mengimplementasikan checklist tugas ini secara step-by-step?
1. Membuat 4 fungsi views untuk menampilkan data dalam format XML, JSON, XML by ID, dan JSON by ID.  
2. Menambahkan routing URL di urls.py untuk masing-masing view.
3. membuat base.html (direktori templates pada root) yang berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya
4. menambahkan base.html tadi ke list TEMPLATES di settings.py
5. edit main.html pada dir main/templates agar menggunakan template utama
6. membuat forms.py
7. menambahkan function create_items & show_items pada views.py dan membuat list item pada fuction show_main
8. import function yang telah dibuat ke urls.py
9. membuat tampilan baru untuk main.html (buat button add items dan juga menampilkan daftar berita dan juga button detail).
10. Membuat create_items & items_detail (.html) untuk halaman ketika button additems di klik dan juga button detail.

6. Feedback untuk Asdos di Tutorial 2
amann

Dokumentasi Postman
Berikut hasil akses endpoint menggunakan Postman:

<img width="1470" height="919" alt="Screenshot 2025-09-17 at 03 56 59" src="https://github.com/user-attachments/assets/91fb4f94-561c-4d44-afdd-0fea11b29762" />
<img width="1470" height="919" alt="Screenshot 2025-09-17 at 03 57 03" src="https://github.com/user-attachments/assets/a459f6f8-f10b-4d1c-8280-61aa4b06577e" />
<img width="1470" height="919" alt="Screenshot 2025-09-17 at 03 57 06" src="https://github.com/user-attachments/assets/bc1b547b-b007-408e-b20f-08da01317b82" />
<img width="1470" height="919" alt="Screenshot 2025-09-17 at 03 57 08" src="https://github.com/user-attachments/assets/06f1fc9e-58a3-4a28-a377-cb3845220bb6" />




</details>



