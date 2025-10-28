# Piramida biasa
tinggi = 5

print("Piramida Biasa:")
for i in range(tinggi):
    # Spasi sebelum bintang
    for j in range(tinggi - i - 1):
        print(" ", end="")
    
    # Bintang
    for k in range(2 * i + 1):
        print("*", end="")
    
    print()