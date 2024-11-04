# Deklarasi  matriks pertama 
matriks1 = []
matriks2 = []

# Meminta input untuk matriks pertama
print("Masukkan elemen untuk matriks pertama (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks1.append(baris)

# Meminta input untuk matriks kedua
print("\nMasukan elemen untuk matriks kedua (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukkan elemen baris {i+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks2.append(baris)

# Minta input berdasarkan operasi
operasi = input("\nPilih oprasi (Perjumlahan/Perngurangan/Perkalian): ").lower()

# Melakukan operasi berdasarkan pilihan
hasil = []
if operasi == 'Penjumlahan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)
elif operasi == 'Pengurangan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] - matriks2[i][j])
    hasil.append(baris)
elif operasi == 'Perkalian':
    for i in range(3):
        baris = []
        for j in range(3):
            nilai = 0
            for k in range(3):
                nilai += matriks1[i][k] * matriks2[i][k]
            baris.append(nilai)
        hasil.append(baris)
else:
    print("operasi tidak valid")

# Menampilkan hasil operasi
if hasil:
    print(f"\nHasil {operasi} matriks:")
    for baris in hasil:
        print(baris)