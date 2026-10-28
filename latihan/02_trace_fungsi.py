# Latihan 2: Tracing Fungsi
def hitung_diskon(total, persen):
    diskon = total * persen / 100
    return total - diskon

print("Total bayar:", hitung_diskon(200000, 10))