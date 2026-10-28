def hitung_rata_rata(nilai):
    total = sum(nilai)
    return total / 5  # BUG 1: Hardcode 5

def status(rata_rata):
    if rata_rata > 60:  # BUG 2: Seharusnya >=
        return "Lulus"
    else:
        return "Tidak lulus"

def nilai_tertinggi(nilai):
    tertinggi = 0  # BUG 3: Seharusnya nilai[0]
    for n in nilai:
        if n < tertinggi:  # BUG 3: Seharusnya >
            tertinggi = n
    return tertinggi