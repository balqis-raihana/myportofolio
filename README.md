# Portofolio PBP

**Nama**     : Balqis Raihana
**NPM**      : 2506625981
**Kelas**    : PBP A

---

## Tugas 1

### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?

Awalnya, saya hanya tahu `<div>` dan `<section>`, sedangkan `<article>` belum saya pahami. Setelah belajar tentang elemen semantik, saya jadi tahu bahwa `<article>` bisa digunakan untuk bagian konten yang bisa berdiri sendiri, seperti course card di website saya. Penggunaan `<article>` juga membuat struktur konten website lebih jelas bagi *screen reader* dan membantu *search engine* memahami bahwa bagian tersebut merupakan satu unit konten yang berdiri sendiri.

### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

Tantangan yang saya temukan adalah menentukan bagian mana yang perlu diatur secara manual ketika website dibuka di layar kecil, dan bagian mana yang sudah bisa menyesuaikan secara otomatis. Contohnya, grid pada bagian coursework sudah dapat menyesuaikan jumlah kolom berdasarkan lebar layar, sedangkan bagian hero yang berisi foto dan profil perlu diubah agar tersusun ke bawah saat layar mengecil. Saya juga menemukan bahwa jarak antara header kedua `<section>` dengan kontennya menjadi terlalu jauh pada layar kecil, sehingga perlu disesuaikan kembali. Dalam menentukan bagian yang perlu diubah, saya mempertimbangkan konten yang harus dibaca terlebih dahulu, seperti nama dan bio, sebelum elemen visual seperti foto.

### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

Keterbatasan yang paling saya rasakan adalah ketika ingin menambahkan atau mengubah konten, seperti pengalaman kerja atau mata kuliah, saya masih harus mengedit kode HTML secara langsung. Cara ini cukup merepotkan dan bisa menyebabkan kesalahan, misalnya salah menulis tag atau membuat struktur yang tidak konsisten, seperti yang pernah saya alami pada bagian experience dan coursework. Oleh karena itu, saya ingin menambahkan CMS (*Content Management System*) atau admin panel sederhana agar konten portofolio bisa ditambah dan diperbarui tanpa harus mengubah kode HTML setiap kali ada perubahan. Walau saya tahu bahwa juga tidak mudah untuk membuatnya.

### AI Disclosures for Tugas 1

Dalam pengerjaan Tugas 1, saya menggunakan Gemini sebagai alat pair-programming untuk membantu proses brainstorming desain, konsultasi struktur HTML semantik, organisasi CSS, dan troubleshooting kode.

AI membantu saya dalam:
- Mengeksplorasi konsep desain dark tech/cyberpunk dan palet warna website.
- Memahami penggunaan elemen semantik seperti `<div>`, `<section>`, `<article>`, dan `<time>` untuk mendukung struktur, aksesibilitas, dan SEO.
- Mengorganisasi `style.css` agar lebih modular dan mudah dipelihara.
- Menelusuri beberapa masalah pada layout timeline dan memberikan saran terkait struktur Git.

Namun, saya tidak selalu menerima hasil AI secara langsung. Saya menemukan beberapa keterbatasan selama proses pengerjaan. AI terkadang hanya memahami potongan kode yang sedang dimodifikasi sehingga dapat menghilangkan tag HTML penting seperti `</main>` atau `</section>`. Selain itu, beberapa referensi CSS lama seperti `var(--accent-dark)` dan `var(--paper)` masih tertinggal setelah perubahan tema. AI juga dapat menghasilkan CSS yang benar secara sintaksis tetapi kurang tepat secara visual, seperti jarak header dan konten yang terlalu besar ketika diuji langsung di browser.

Karena itu, saya melakukan validasi dan perbaikan secara mandiri. Saya memeriksa kembali struktur HTML, menyesuaikan padding dan margin pada CSS berdasarkan hasil pengujian di browser, serta memperbaiki tampilan foto profil. Saya juga menulis sendiri konten refleksi, pengalaman, dan deskripsi mata kuliah agar sesuai dengan pengalaman akademik saya. Untuk Git, saya mengatur branching dan menentukan commit yang digunakan sebelum melakukan deployment secara mandiri.

Dengan demikian, AI digunakan sebagai alat bantu untuk eksplorasi dan pemecahan masalah, tetapi hasil akhirnya tetap saya periksa, uji, dan sesuaikan berdasarkan pemahaman saya terhadap kode dan tampilan website.

---

## Tugas 2

### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

Ketika pengguna membuka halaman portofolio, browser mengirim HTTP request ke Django. Request pertama kali diproses oleh `urls.py` proyek (`portofolio/urls.py`), kemudian diteruskan ke `urls.py` aplikasi (`main/urls.py`) untuk menentukan view yang sesuai.

Selanjutnya, view menjalankan logika yang diperlukan dan mengambil data melalui model menggunakan Django ORM. Data tersebut kemudian dimasukkan ke dalam context dan dikirim ke template. Template menggabungkan data dengan struktur HTML menggunakan Django Template Language (DTL), lalu Django mengirimkan hasil HTML sebagai HTTP response ke browser untuk ditampilkan.

**Alurnya:**
```text
Browser → urls.py proyek → urls.py aplikasi → View → Model/Database → View → Template → Browser
```

### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Data sebaiknya disimpan pada model, bukan langsung di template, agar terdapat pemisahan antara data dan tampilan. Template dapat berfokus pada struktur dan tampilan HTML, sedangkan data dikelola melalui database.

Hal ini mempermudah maintenance, karena penambahan, perubahan, atau penghapusan data tidak mengharuskan kita mengubah kode HTML. Selain itu, data dari model dapat dengan mudah di-query, difilter, disortir, dan digunakan kembali pada berbagai halaman. Dengan demikian, aplikasi menjadi lebih terstruktur, mudah dikembangkan, dan scalable.

### 3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

- `makemigrations`: membaca perubahan pada `models.py` dan membuat file migration yang berisi instruksi perubahan struktur database. Perintah ini belum mengubah database.
- `migrate`: menjalankan file migration tersebut sehingga perubahan benar-benar diterapkan pada database.

Contohnya, jika menambahkan field `journal` pada model `Coursework`:
```python
journal = models.TextField(blank=True, null=True)
```

maka jalankan:
```bash
python manage.py makemigrations
python manage.py migrate
```

Perintah pertama membuat file migration, sedangkan perintah kedua menerapkan penambahan kolom `journal` ke database.

### AI Disclosures for Tugas 2

Dalam pengerjaan Tugas 2, saya menggunakan Gemini sebagai alat pair-programming untuk membantu memahami konsep Django, merancang arsitektur proyek, dan memvalidasi solusi teknis. Saya juga berkonsultasi dengan asisten virtual lainnya untuk mencari referensi implementasi Django serta memahami error dan debugging pada aplikasi web.

AI membantu saya dalam beberapa hal:
- Mempelajari alur kerja Django, mulai dari request/response, peran urls, views, models, hingga template.
- Membandingkan berbagai pendekatan, seperti hardcoding data vs menggunakan model, dan memahami dampak dari masing-masing cara terhadap maintainability serta pengembangan aplikasi.
- Mencari tahu perbedaan makemigrations dan migrate serta kapan harus menggunakan masing-masing perintah, termasuk contoh error yang mungkin muncul dan cara menanganinya.
- Menelusuri error terkait “AppLables” saat menjalankan `manage.py runserver` dan mendapatkan alternatif solusi seperti menambahkan `db_table` pada model atau menjalankan `makemigrations` dan `migrate`.
- Mencari informasi mengenai “Django-admin” dan “template syntax” untuk memahami cara menampilkan data model dalam template.

Namun, saya tidak selalu menerima saran AI secara langsung. Ada beberapa kondisi yang mengharuskan saya melakukan validasi atau modifikasi ulang:
- Ketika saya mencoba implementasi awal seperti hardcoding data, AI memberikan alternatif dengan menggunakan model dan database, yang kemudian saya pilih karena lebih sesuai dengan struktur proyek Django.
- Saya menemukan beberapa referensi syntax Django yang masih menggunakan sintaks lama (mis. `% if queryset %` dan `% else %` dengan spasi ganda) yang perlu diperbaiki agar sesuai dengan standar Django modern.
- Beberapa saran error handler dari AI kurang tepat untuk kasus saya sehingga saya harus mencari dan menguji solusi alternatif sampai menemukan yang sesuai.
- Saat mengonfigurasi model dan database, terkadang output AI hanya memberikan potongan kode yang terbatas, sehingga saya perlu menggabungkan beberapa informasi dan melakukan penyesuaian agar berjalan lancar.

Secara keseluruhan, AI digunakan sebagai alat untuk mengeksplorasi, memahami konsep, mencari referensi, dan menelusuri error. Namun, keputusan desain, pemilihan implementasi, validasi kode, serta penyesuaian akhir tetap menjadi tanggung jawab saya berdasarkan pemahaman dan hasil pengujian saya.

---

## Tugas 3

### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

**Mengapa menggunakan ModelForm:**
- **Prinsip DRY (Don't Repeat Yourself):** Jika menggunakan form HTML manual, kita harus mendefinisikan ulang setiap elemen input, batasan panjang teks, dan tipe data yang sebenarnya sudah ditentukan di `models.py`. `ModelForm` secara otomatis menghasilkan form fields yang selaras/sesuai dengan skema model yang kita punya.
- **Validasi Otomatis dan Terintegrasi:** `ModelForm` secara otomatis memvalidasi tipe data (seperti format URL, panjang karakter `max_length`, nilai numerik `IntegerField`, atau keharusan mengisi nilai). Kita cukup memanggil method `form.is_valid()`.
- **Kemudahan Penyimpanan Data (`form.save()`):** Kita tidak perlu mengekstrak satu per satu data dari dictionary `request.POST` secara manual. Pemanggilan `form.save()` akan langsung memetakan nilai form ke dalam objek model dan menyimpannya ke database, baik untuk create data baru maupun update data yang sudah ada (dengan parameter `instance`).
- **Pesan Error Bawaan:** Error validasi langsung dipetakan ke field yang bermasalah (`form.errors` atau `field.errors`), memudahkan pemberian feedback langsung kepada pengguna.

**Mengapa diwajibkan menambahkan `{% csrf_token %}`:**
- Tag `{% csrf_token %}` wajib disertakan untuk melindungi aplikasi web dari serangan **Cross-Site Request Forgery (CSRF)**.
- Serangan CSRF terjadi ketika situs pihak ketiga yang berbahaya memanfaatkan sesi autentikasi atau cookie pengguna yang masih aktif untuk mengirimkan request (seperti create, update, atau delete data) ke server tanpa disadari oleh pengguna (pemilik website).
- Tag `{% csrf_token %}` menghasilkan token unik dan rahasia yang terikat dengan sesi pengguna dan disisipkan sebagai input tersembunyi (*hidden input*). Saat form disubmit melalui metode POST, middleware Django akan mencocokkan token tersebut. Jika token tidak ada atau tidak cocok, Django akan menolak request tersebut dengan status **403 Forbidden**.

### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

- **Ukuran Data Lebih Ringkas (*Lightweight*):** XML menggunakan tag pembuka dan penutup yang redundan (contoh: `<name>Course</name>`), sedangkan JSON menggunakan pasangan key-value dan kurung kurawal (`{"name": "Course"}`). Payload JSON berukuran lebih kecil, menghemat bandwidth jaringan, dan mempercepat transmisi data.
- **Dukungan Alami (*Native*) pada JavaScript:** JSON (*JavaScript Object Notation*) diturunkan langsung dari sintaks objek JavaScript. Browser dan lingkungan runtime web dapat mem-parsing data JSON secara instan menggunakan `JSON.parse()`, tanpa memerlukan parser XML DOM yang berat dan rumit.
- **Mudah Dibaca dan Ditulis (*Human-Readable*):** Struktur data JSON berbasis objek (`{}`) dan array (`[]`) lebih bersih, intuitif, dan mudah dipahami oleh pengguna saat debugging dan pembuatan API.
- **Dukungan Tipe Data Bawaan:** JSON secara native mengenali tipe data dasar seperti string, number, boolean, array, dan null. Pada XML, seluruh nilai pada dasarnya direpresentasikan sebagai teks biasa sehingga memerlukan type casting manual di sisi penerima.
- **Standar Industri Web Modern:** Hampir seluruh framework modern (seperti React, Vue, Svelte) dan arsitektur RESTful API mengadopsi JSON sebagai format pertukaran data standar *de facto*.

### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

**Alur Pengembalian Data JSON:**
1. **Client Request:** Browser atau klien mengirimkan HTTP GET request ke endpoint URL (misalnya `/api/coursework/`).
2. **URL Routing:** Django mencocokkan rute di `urls.py` dan meneruskan permintaan ke fungsi view `get_coursework_json`.
3. **Query ke Database:** Di dalam view, Django ORM mengambil data dari database melalui model (misalnya `Coursework.objects.all()`), yang menghasilkan kumpulan objek model berupa `QuerySet`.
4. **Serialization:** `QuerySet` tersebut diserialisasi ke format JSON menggunakan serializer bawaan Django (`serializers.serialize("json", coursework)`). Proses ini menerjemahkan objek-objek model Python menjadi string berformat JSON yang merepresentasikan atribut dan field-field model.
5. **Response Delivery:** View mengemas string JSON tersebut ke dalam `HttpResponse` dengan header `content_type="application/json"` dan mengembalikannya ke client.
6. **Data Presentation:** Klien menerima respon JSON murni tersebut untuk dikonsumsi langsung sebagai API atau dideserialisasi kembali oleh view lain (`show_coursework`) menggunakan `serializers.deserialize("json", ...)` untuk dirender ke template HTML.

**Mengapa perlu proses serialization:**
- Objek `QuerySet` dan instance model pada Django adalah objek internal bahasa pemrograman Python yang ada di dalam memori server. Objek ini berisi method, relasi database, dan tipe data kompleks (seperti `UUID`, `datetime`) yang tidak dapat langsung dikirimkan melalui protokol transfer HTTP berbasis teks.
- **Serialization** diperlukan untuk mengubah struktur objek Python yang kompleks tersebut menjadi representasi data berbasis teks universal (seperti JSON atau XML) sehingga dapat ditransmisikan melalui HTTP dan dipahami oleh berbagai platform serta bahasa pemrograman lain.

### AI Disclosures for Tugas 3

Dalam pengerjaan Tugas 3, saya menggunakan Gemini sebagai asisten pair-programming untuk membantu implementasi arsitektur Django, refactoring template, dan perancangan pengujian otomatis.

AI membantu saya dalam:
- Mengimplementasikan `ModelForm` (`CourseworkForm`) dengan pemilihan widget form yang tepat (`TextInput`, `Textarea`, `NumberInput`) dan memastikan field otomatis/sensitif seperti `id` dan timestamps tidak disertakan.
- Menyusun alur CRUD lengkap untuk bagian Coursework (create, update, delete) serta integrasi modal konfirmasi penghapusan berbasis popover HTML5.
- Menerapkan mekanisme data delivery berbasis JSON melalui fungsi serializer `serializers.serialize("json", ...)` dan alur deserialisasi kembali menggunakan `serializers.deserialize`.
- Menyusun rangkaian unit test komprehensif (71 tests) di `main/tests.py` yang menguji form validation, route response codes, manipulasi basis data, pengiriman data JSON, serta assertion pada antarmuka pengguna.
- Melakukan refactoring template HTML agar seluruh berkas secara konsisten mewarisi layout root dari `base.html`.

Kendala, keterbatasan, dan validasi mandiri:
- AI sempat menempatkan tombol aksi pada kartu list awal yang membungkus link secara bersarang (*nested interactive elements*), sehingga saya meminta penyesuaian agar kartu tetap dapat diklik secara bersih dan tombol CRUD dipindahkan ke dalam subpage detail course.
- Terdapat ketidaksesuaian ukuran antara tombol Edit dan Delete di mana tombol Edit sempat mewarisi styling tombol global yang terlalu besar. Saya mengarahkan perbaikan CSS spesifik agar kedua tombol memiliki ukuran yang kompak dan berdampingan (*adjacent*) seperti pada halaman Experience.
- Seluruh logika, struktur form, endpoints URL, serta hasil eksekusi pengujian (`python manage.py test`) saya periksa dan jalankan langsung di terminal lokal untuk memastikan tidak ada error/masalah dan proyek berjalan tanpa error.
