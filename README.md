# Pertemuan 13 - Debugging dan Testing

Nama: Eka Elsanti
NIM: 2225250059
Kelas: 3A

## Kasus
Program `praktik_4_debugging.py` digunakan untuk menghitung nilai rata-rata dari sekumpulan data, menentukan status kelulusan berdasarkan ambang batas nilai 60, serta mengidentifikasi nilai tertinggi dari sekumpulan data angka.

## Test Case
| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC-01 | [80, 90] | 85.0 | 34.0 | FAIL |
| TC-02 | 60 | Lulus | Tidak lulus | FAIL |
| TC-03 | [-10, -5] | -5 | 0 | FAIL |

## Bug Report
1. **Fungsi `hitung_rata_rata`**
   * Gejala: Hasil perhitungan rata-rata tidak tepat (terlalu kecil).
   * Lokasi: `return total / 5`
   * Akar Penyebab: Pembagi jumlah total di-hardcode dengan angka 5.
   * Perbaikan: Mengganti angka 5 dengan fungsi `len(nilai)`.

2. **Fungsi `status`**
   * Gejala: Input nilai 60 menghasilkan status "Tidak lulus".
   * Lokasi: `if rata_rata > 60:`
   * Akar Penyebab: Penggunaan operator relasional `>` yang mengabaikan nilai pas 60.
   * Perbaikan: Mengubah operator menjadi `>=`.

3. **Fungsi `nilai_tertinggi`**
   * Gejala: Input angka negatif menghasilkan angka 0.
   * Lokasi: `tertinggi = 0` dan `if n < tertinggi:`
   * Akar Penyebab: Inisialisasi awal nilai 0 dan perbandingan operator terbalik.
   * Perbaikan: Inisialisasi awal menggunakan `nilai[0]` dan perbandingan menggunakan `>`.

## Retest
| ID | Input | Expected | Actual Perbaikan | Status |
|---|---|---|---|---|
| TC-01 | [80, 90] | 85.0 | 85.0 | PASS |
| TC-02 | 60 | Lulus | Lulus | PASS |
| TC-03 | [-10, -5] | -5 | -5 | PASS |

## Cara Menjalankan
python3 grafik/praktik_4_debugging.py

## Refleksi
Teknik debugging yang paling membantu adalah penggunaan **breakpoint** bersama fitur **tracing/step over** pada IDE. Teknik ini memungkinkan penelusuran perubahan nilai variabel secara langsung pada tiap baris eksekusi tanpa perlu menambahkan perintah `print()` manual, sehingga mempercepat penemuan bug logika.