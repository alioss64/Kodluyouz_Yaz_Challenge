# Kullanıcıdan bir kelime girişi alın
kelime = input("Bir kelime girin: ")

# Kelimenin uzunluğunu hesaplayın
uzunluk = len(kelime)

# Sonucu ekrana yazdırın
print("Kelimenin uzunluğu:", uzunluk)

#--------------------------------------------------------------------------------------#
# Kullanıcıdan bir sayı girişi alın
sayi = int(input("Bir sayı girin: "))

# Sayının basamaklarının toplamını hesaplayın
toplam = 0
gecici_sayi = sayi

while gecici_sayi > 0:
    basamak = gecici_sayi % 10
    toplam += basamak
    gecici_sayi //= 10

# Sonucu ekrana yazdırın
print("Sayının basamaklarının toplamı:", toplam)
