# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))
toplam = 0

# 1'den sayıya kadar olan toplamı hesapla
for i in range(1, sayi + 1):
    toplam += i

print(f"1'den {sayi}'a kadar olan sayıların toplamı: {toplam}")
