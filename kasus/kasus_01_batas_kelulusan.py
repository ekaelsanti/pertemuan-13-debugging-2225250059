def status_lulus(nilai):
    # BUG LOGIKA: Nilai 60 dianggap tidak lulus karena menggunakan '>' bukan '>='
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"

# Pengujian
print("Nilai 75:", status_lulus(75))
print("Nilai 60:", status_lulus(60))  # Harusnya Lulus
print("Nilai 59:", status_lulus(59))