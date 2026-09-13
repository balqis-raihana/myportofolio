Nama  : Balqis Raihana

NPM   : 2506625981

Kelas : PBP A

========================================================================================================
### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda? 

Awalnya, saya hanya tahu <div> dan <section>, sedangkan <article> belum saya pahami. Setelah belajar tentang elemen semantik, saya jadi tahu bahwa <article> bisa digunakan untuk bagian konten yang bisa berdiri sendiri, seperti course card di website saya. Penggunaan <article> juga membuat struktur konten website lebih jelas bagi screen reader dan membantu search engine memahami bahwa bagian tersebut merupakan satu unit konten yang berdiri sendiri.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?

Tantangan yang saya temukan adalah menentukan bagian mana yang perlu diatur secara manual ketika website dibuka di layar kecil, dan bagian mana yang sudah bisa menyesuaikan secara otomatis. Contohnya, grid pada bagian coursework sudah dapat menyesuaikan jumlah kolom berdasarkan lebar layar, sedangkan bagian hero yang berisi foto dan profil perlu diubah agar tersusun ke bawah saat layar mengecil. Saya juga menemukan bahwa jarak antara header kedua <section> dengan kontennya menjadi terlalu jauh pada layar kecil, sehingga perlu disesuaikan kembali. Dalam menentukan bagian yang perlu diubah, saya mempertimbangkan konten yang harus dibaca terlebih dahulu, seperti nama dan bio, sebelum elemen visual seperti foto.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

Keterbatasan yang paling saya rasakan adalah ketika ingin menambahkan atau mengubah konten, seperti pengalaman kerja atau mata kuliah, saya masih harus mengedit kode HTML secara langsung. Cara ini cukup merepotkan dan bisa menyebabkan kesalahan, misalnya salah menulis tag atau membuat struktur yang tidak konsisten, seperti yang pernah saya alami pada bagian experience dan coursework. Oleh karena itu, saya ingin menambahkan CMS (Content Management System) atau admin panel sederhana agar konten portofolio bisa ditambah dan diperbarui tanpa harus mengubah kode HTML setiap kali ada perubahan. Walau saya tahu bahwa juga tidak mudah untuk membuatnya.

## AI Disclosures for Tugas 1
Dalam pengerjaan Tugas 1, saya menggunakan Gemini sebagai alat pair-programming untuk membantu proses brainstorming desain, konsultasi struktur HTML semantik, organisasi CSS, dan troubleshooting kode.

AI membantu saya dalam:
- Mengeksplorasi konsep desain dark tech/cyberpunk dan palet warna website.
- Memahami penggunaan elemen semantik seperti <div>, <section>, <article>, dan <time> untuk mendukung struktur, aksesibilitas, dan SEO.
- Mengorganisasi style.css agar lebih modular dan mudah dipelihara.
- Menelusuri beberapa masalah pada layout timeline dan memberikan saran terkait struktur Git.

Namun, saya tidak selalu menerima hasil AI secara langsung. Saya menemukan beberapa keterbatasan selama proses pengerjaan. AI terkadang hanya memahami potongan kode yang sedang dimodifikasi sehingga dapat menghilangkan tag HTML penting seperti </main> atau </section>. Selain itu, beberapa referensi CSS lama seperti var(--accent-dark) dan var(--paper) masih tertinggal setelah perubahan tema. AI juga dapat menghasilkan CSS yang benar secara sintaksis tetapi kurang tepat secara visual, seperti jarak header dan konten yang terlalu besar ketika diuji langsung di browser.

Karena itu, saya melakukan validasi dan perbaikan secara mandiri. Saya memeriksa kembali struktur HTML, menyesuaikan padding dan margin pada CSS berdasarkan hasil pengujian di browser, serta memperbaiki tampilan foto profil. Saya juga menulis sendiri konten refleksi, pengalaman, dan deskripsi mata kuliah agar sesuai dengan pengalaman akademik saya. Untuk Git, saya mengatur branching dan menentukan commit yang digunakan sebelum melakukan deployment secara mandiri.

Dengan demikian, AI digunakan sebagai alat bantu untuk eksplorasi dan pemecahan masalah, tetapi hasil akhirnya tetap saya periksa, uji, dan sesuaikan berdasarkan pemahaman saya terhadap kode dan tampilan website.

========================================================================================================
## Tugas 2
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

Ketika pengguna membuka halaman portofolio, browser mengirim HTTP request ke Django. Request pertama kali diproses oleh urls.py proyek (portofolio/urls.py), kemudian diteruskan ke urls.py aplikasi (main/urls.py) untuk menentukan view yang sesuai.
Selanjutnya, view menjalankan logika yang diperlukan dan mengambil data melalui model menggunakan Django ORM. Data tersebut kemudian dimasukkan ke dalam context dan dikirim ke template. Template menggabungkan data dengan struktur HTML menggunakan Django Template Language (DTL), lalu Django mengirimkan hasil HTML sebagai HTTP response ke browser untuk ditampilkan.
Alurnya:
Browser → urls.py proyek → urls.py aplikasi → View → Model/Database → View → Template → Browser

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Data sebaiknya disimpan pada model, bukan langsung di template, agar terdapat pemisahan antara data dan tampilan. Template dapat berfokus pada struktur dan tampilan HTML, sedangkan data dikelola melalui database.
Hal ini mempermudah maintenance, karena penambahan, perubahan, atau penghapusan data tidak mengharuskan kita mengubah kode HTML. Selain itu, data dari model dapat dengan mudah di-query, difilter, disortir, dan digunakan kembali pada berbagai halaman. Dengan demikian, aplikasi menjadi lebih terstruktur, mudah dikembangkan, dan scalable.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

- makemigrations: membaca perubahan pada models.py dan membuat file migration yang berisi instruksi perubahan struktur database. Perintah ini belum mengubah database.
- migrate: menjalankan file migration tersebut sehingga perubahan benar-benar diterapkan pada database.
Contohnya, jika menambahkan field journal pada model Coursework:
journal = models.TextField(blank=True, null=True)
maka jalankan:
python manage.py makemigrations
python manage.py migrate
Perintah pertama membuat file migration, sedangkan perintah kedua menerapkan penambahan kolom journal ke database.

## AI Disclosures for Tugas 2
Dalam pengerjaan Tugas 2, saya menggunakan Gemini sebagai alat pair-programming untuk membantu memahami konsep Django, merancang arsitektur proyek, dan memvalidasi solusi teknis. Saya juga berkonsultasi dengan asisten virtual lainnya untuk mencari referensi implementasi Django serta memahami error dan debugging pada aplikasi web.

AI membantu saya dalam beberapa hal:
- Mempelajari alur kerja Django, mulai dari request/response, peran urls, views, models, hingga template.
- Membandingkan berbagai pendekatan, seperti hardcoding data vs menggunakan model, dan memahami dampak dari masing-masing cara terhadap maintainability serta pengembangan aplikasi.
- Mencari tahu perbedaan makemigrations dan migrate serta kapan harus menggunakan masing-masing perintah, termasuk contoh error yang mungkin muncul dan cara menanganinya.
- Menelusuri error terkait “AppLables” saat menjalankan manage.py runserver dan mendapatkan alternatif solusi seperti menambahkan `db_table` pada model atau menjalankan `makemigrations` dan `migrate`.
- Mencari informasi mengenai “Django-admin” dan “template syntax” untuk memahami cara menampilkan data model dalam template.

Namun, saya tidak selalu menerima saran AI secara langsung. Ada beberapa kondisi yang mengharuskan saya melakukan validasi atau modifikasi ulang:

- Ketika saya mencoba implementasi awal seperti hardcoding data, AI memberikan alternatif dengan menggunakan model dan database, yang kemudian saya pilih karena lebih sesuai dengan struktur proyek Django.
- Saya menemukan beberapa referensi syntax Django yang masih menggunakan sintaks lama (mis. `% if queryset %` dan `% else %` dengan spasi ganda) yang perlu diperbaiki agar sesuai dengan standar Django modern.
- Beberapa saran error handler dari AI kurang tepat untuk kasus saya sehingga saya harus mencari dan menguji solusi alternatif sampai menemukan yang sesuai.
- Saat mengonfigurasi model dan database, terkadang output AI hanya memberikan potongan kode yang terbatas, sehingga saya perlu menggabungkan beberapa informasi dan melakukan penyesuaian agar berjalan lancar.

Secara keseluruhan, AI digunakan sebagai alat untuk mengeksplorasi, memahami konsep, mencari referensi, dan menelusuri error. Namun, keputusan desain, pemilihan implementasi, validasi kode, serta penyesuaian akhir tetap menjadi tanggung jawab saya berdasarkan pemahaman dan hasil pengujian saya.

========================================================================================================
