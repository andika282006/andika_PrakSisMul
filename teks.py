teks = "Anjayy"

for karakter in teks:
    kode = ord(karakter)
    biner = format(kode, '08b')
    print(karakter, "=", kode, "(", biner, ")")
