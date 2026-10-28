def baca_file_nilai(nama_file):
    # Dapat memicu FileNotFoundError jika file tidak ditemukan
    with open(nama_file, 'r', encoding='utf-8') as f:
        isi = f.readlines()
    return isi

try:
    data = baca_file_nilai("data_nilai_dummy.txt")
    print(data)
except FileNotFoundError:
    print("Error: File data tidak ditemukan!")