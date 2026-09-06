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

## AI Disclosures
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