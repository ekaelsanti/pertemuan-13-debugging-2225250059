def hitung_rata_rata(data):
    # BUG LOGIKA: Pembagi di-hardcode angka 5, padahal isi data bisa variabel
    total = sum(data)
    return total / 5

# Pengujian
data_nilai = [80, 90, 70]
print("Rata-rata:", hitung_rata_rata(data_nilai))  # Hasilnya salah karena pembaginya 5