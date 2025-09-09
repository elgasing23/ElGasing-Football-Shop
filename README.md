# Tugas 2 PBP

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

   






   
