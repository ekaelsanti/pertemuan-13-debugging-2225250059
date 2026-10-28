# Latihan 3: Test Case
def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

# Test Case Manual
print("Test 59:", status_lulus(59))  # Expected: Tidak lulus
print("Test 60:", status_lulus(60))  # Expected: Lulus
print("Test 61:", status_lulus(61))  # Expected: Lulus