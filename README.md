# LAB-AP-18-2026
## 📚 Repositori Tugas Praktikum Algoritma & Pemrograman 2026

Selamat datang di repositori resmi **Praktikum Algoritma & Pemrograman 2026**.
Repositori ini digunakan oleh mahasiswa untuk mengumpulkan seluruh **Tugas Praktikum (TP)** selama semester berlangsung.

---

# 🚀 Tutorial Pengumpulan Tugas (Fork hingga Pull Request)

Ikuti langkah-langkah di bawah ini untuk mengerjakan dan mengumpulkan tugas praktikum kamu.

## Langkah 1: Fork Repository (Di Browser)
1. Buka halaman GitHub repository utama ini.
2. Di pojok kanan atas halaman, klik tombol **Fork**.
3. Pastikan memilih akun GitHub pribadimu sebagai tujuan *fork*.
4. Klik **Create fork**. Sekarang kamu memiliki salinan repository ini di akun GitHub kamu sendiri.

## Langkah 2: Clone Repository (Di Komputer/Laptop)
Agar bisa mengerjakan tugas di komputer sendiri, kamu harus men-download (clone) repository hasil fork milikmu.

1. Buka hasil fork di GitHub kamu.
2. Klik tombol hijau bertuliskan **<> Code**, lalu *copy* link URL yang muncul.
3. Buka **Terminal** atau **Command Prompt / Git Bash** di komputermu, arahkan ke folder tempat kamu ingin menyimpan tugas.
4. Jalankan perintah berikut (ganti dengan link yang kamu *copy*):
   ```bash
   git clone <link-repository-kamu>
   ```
5. Masuk ke dalam folder yang baru saja di-*clone*:
   ```bash
   cd LAB-AP-18-2026
   ```

## Langkah 3: Mengerjakan Tugas
1. Buka folder tersebut di aplikasi *Code Editor* favoritmu (misal: **VS Code**).
2. Cari folder dengan nama **NIM** kamu (misal: `H071261059`).
3. Tambahkan atau buat file tugas kamu di dalam folder NIM kamu tersebut.
   > **Catatan:** Jangan mengubah file di luar folder NIM milikmu agar tidak terjadi *conflict*!

## Langkah 4: Upload Perubahan (Push ke GitHub)
Setelah tugas selesai dibuat di dalam folder NIM kamu, buka terminal di VS Code (atau terminal biasa), pastikan posisimu berada di dalam folder proyek, lalu jalankan urutan perintah berikut:

```bash
git add .
git status
git commit -m "TP-N"
git push
```
> **Penting:** Ganti `N` pada `TP-N` dengan angka tugas praktikumnya. Misalnya untuk Tugas Praktikum 1, gunakan `git commit -m "TP-1"`.

## Langkah 5: Membuat Pull Request (Mengirimkan Tugas ke Asisten)
1. Buka halaman repository hasil fork di akun GitHub kamu.
2. Akan ada notifikasi *"This branch is 1 commit ahead of..."*, klik tombol **Contribute** lalu pilih **Open pull request**.
3. Di halaman perbandingan, pastikan:
   - **Base repository:** repository utama milik lab/asisten.
   - **Head repository:** repository hasil fork milikmu.
4. Klik tombol **Create pull request**.
5. Isi judul sesuai dengan aturan asisten (contoh: `[TP1] H071261059`).
6. Klik **Create pull request** sekali lagi.

Selesai! Tugas kamu sudah berhasil dikirimkan ke repository utama.

---

## ⚠️ Aturan Penting
1. **Jangan mengubah folder mahasiswa lain.** Setiap mahasiswa hanya mengerjakan folder miliknya sendiri.
2. **Jangan menghapus file mahasiswa lain.**
3. Pastikan program berjalan tanpa error sebelum melakukan `commit` dan dikumpulkan.
4. **Kesalahan target Pull Request atau mengedit file orang lain bisa menyebabkan tugas tidak dinilai.**

**Happy Coding! 🚀**
