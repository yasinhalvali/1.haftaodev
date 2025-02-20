# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İşlemleri gerçekleştir
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
if sayi2 != 0:
    bolum = sayi1 / sayi2
    mod = sayi1 % sayi2
else:
    bolum = "Tanımsız (Sıfıra bölme hatası!)"
    mod = "Tanımsız (Sıfıra bölme hatası!)"

us = sayi1 ** sayi2

# Sonuçları ekrana yazdır
print(f"\nToplama: {toplam}")
print(f"Çıkarma: {fark}")
print(f"Çarpma: {carpim}")
print(f"Bölme: {bolum}")
print(f"Mod Alma: {mod}")
print(f"Üs Alma: {us}")