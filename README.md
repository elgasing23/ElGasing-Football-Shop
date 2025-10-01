# TUGAS INDIVIDU
Nama: M Naufal Zhafran Rabiul Batara

NPM: 2406361694

Kelas: F

Link PWS: https://m-naufal41-elgasingshop.pbp.cs.ui.ac.id/




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
   1. Membuat 4 fuction baru di views dengan menggunakan Httpresponse dan seriaizers untuk menampilkan data dalam format XML, JSON, XML by ID, dan JSON by ID.
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

<details>
   <summary>
      Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django
   </summary>

## Pertanyaan di README

<details>
  <summary>1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.</summary>
  
  **AuthenticationForm** adalah form bawaan Django untuk proses login.  
  - **Kelebihan**: Mudah digunakan, langsung terintegrasi dengan sistem autentikasi Django.  
  - **Kekurangan**: Kurang fleksibel jika butuh customisasi form login yang kompleks.
</details>

<details>
  <summary>2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?</summary>
  
  - **Autentikasi**: Proses memverifikasi identitas pengguna (misalnya login dengan username & password).  
  - **Otorisasi**: Proses menentukan hak akses pengguna setelah berhasil diautentikasi.  
  Django menggunakan `django.contrib.auth` untuk autentikasi dan `permissions`/`groups` untuk otorisasi.
</details>

<details>
  <summary>3. Kelebihan & Kekurangan Session dan Cookies</summary>
  
  - **Session**  
    - **Kelebihan**: Data tersimpan di server → lebih aman.  
    - **Kekurangan**: Membutuhkan manajemen penyimpanan di server.  
  - **Cookies**  
    - **Kelebihan**: Ringan, langsung tersimpan di browser.  
    - **Kekurangan**: Rentan dimanipulasi/diintip jika tidak dienkripsi.
</details>

<details>
  <summary>4. Apakah penggunaan Cookies aman secara default?</summary>
  
  - **Cookies** tidak selalu aman secara default.  
  - Potensi risiko: *session hijacking*, *cross-site scripting (XSS)*.  
  - **Django** menyediakan mitigasi:  
    - `HttpOnly=True` → mencegah akses JavaScript.  
    - `Secure=True` → hanya dikirim lewat HTTPS.  
    - `SESSION_COOKIE_AGE` → atur waktu kadaluarsa.
</details>

## Implementasi Checklist Step by Step

<details>
  <summary>1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sesuai dengan status login/log out-nya.</summary>
  1. membuat function regist, login ,logout
  2. membuat tampilan page untuk registrasi, login. untuk logout cuman ditambahkan button pada main.html
  3. Merestriksi Akses Halaman Main dan item Detail dengan menggunakan @loginrequired
  4. menambahkan info last login
</details>

<details>
  <summary>2. Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.</summary>
  1. elgasing
     - Jersey
     - El gasing de la Goat
     - onananananna
    
  2. decul
     - Jersey
     - Barca
     - Bangku
     
</details>

<details>
  <summary>3. Menghubungkan model Product dengan User</summary>
  1. import user di models.py dengan menambahkan line command "from django.contrib.auth.models import User"
  2. define user sebagai "user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)" ini berfungsi untuk menghubungkan satu items dengan satu user melalui sebuah relationship
  3. buat migrasi model lalu migrasi
  4. edit views.py di bagian create_items
   
@login_required(login_url='/login')
def create_items(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form_entry = form.save(commit = False)
        form_entry.user = request.user
        form_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items.html", context)

Parameter commit=False pada potongan kode di atas digunakan agar Django tidak langsung menyimpan objek hasil form ke database. Dengan begitu, kita memiliki kesempatan untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan.

  5. membuat filter type di show main untuk tampilan default kita set ke all (semua barang yang dijual oleh semua user)
  6. menambahkan tombol all and my items di main_html
  7. menambah info seller di item detail
</details>

<details>
  <summary>4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.</summary>
  1. mengubah bagian kode di fungsi login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login.
  2. menambah lastlogin pada context variable di show_main
  3. mengubah fungsi logout agar menghapus cookie setelah logout
  4. menambah info lastlogin di main html
  
</details>

   
   

</details>

<details>
   <summary>Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS</summary>
   <details>
      <summary>Jawaban Pertanyaan</summary>
      <details>
         <summary>Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!</summary>
         Urutan prioritas menentukan style mana yang akan diterapkan jika ada beberapa CSS yang menargetkan elemen yang sama. urutannya sebagai berikut:
         1. Inline style (<div style="color: red;">)
         2. ID selector (#id)
         3. Class, pseudo-class, attribute selector (.class, :hover, [type="text"]) 
         4. Element selector (div, p, h1)
         5. Universal selector (*)
      </details>
      <details>
         
      <summary> Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!</summary>
      
      </details>

      <details>
         
      <summary> Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!</summary>
      
      </details>

      <details>
         
      <summary> Jelaskan konsep flex box dan grid layout beserta kegunaannya!</summary>
      
      </details>

   </details>

   <details>
      <summary>Penjelasan Step by Step</summary>
   </details>
</details>


