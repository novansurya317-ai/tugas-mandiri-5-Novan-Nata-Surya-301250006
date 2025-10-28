# Outer loop untuk mengontrol jumlah baris
for i in range(5, 0, -1):
    # Inner loop untuk mengontrol angka dalam setiap baris
    for j in range(1, i + 1):
        print(j, end='')
    print()  # Pindah ke baris baru setelah setiap baris selesai