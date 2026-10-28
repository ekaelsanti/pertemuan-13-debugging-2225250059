# Latihan 4: Debugging dengan Breakpoint
def rata_rata(data):
    if len(data) == 0:
        return 0
    total = sum(data)
    return total / len(data)

print("Rata-rata:", rata_rata([80, 90, 70]))