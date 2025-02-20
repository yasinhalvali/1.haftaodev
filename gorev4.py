# Kullanıcıdan metin al
metin = input("Bir metin girin: ")
ters_metin = ""

# Metni ters çevirmek için döngü kullan
for i in range(len(metin) - 1, -1, -1):
    ters_metin += metin[i]

print(f"Girdiğiniz metnin tersi: {ters_metin}")
