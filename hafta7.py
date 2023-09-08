# Kullanıcıdan bir sayı girişi alın
sayi = float(input("Bir sayı girin: "))

# Sayının karesini hesaplayın
kare = sayi ** 2

# Sonucu ekrana yazdırın
print(sayi, "sayısının karesi:", kare)

#----------------------------------------------------------------------------------------------------#


dizi = [11,5, 25, 30, 75, 27, 89]

# Diziyi sıralayın
dizi.sort()

# Dizinin uzunluğunu alın
uzunluk = len(dizi)

# Medyanı hesaplayın
if uzunluk % 2 == 1:
    # Dizi tek uzunlukta ise
    medyan = dizi[uzunluk // 2]
else:
    # Dizi çift uzunlukta ise
    orta_1 = dizi[uzunluk // 2 - 1]
    orta_2 = dizi[uzunluk // 2]
    medyan = (orta_1 + orta_2) / 2

# Sonucu ekrana yazdırın
print("Dizin medyanı:", medyan)

#-------------------------------------------------------------------------------------------#

# Kullanıcıdan bir sayı girişi alın
sayi = int(input("Bir sayı girin: "))

# Sayının basamak sayısını hesaplayın
basamak_sayisi = len(str(sayi))

# Sayının Armstrong sayısı olup olmadığını kontrol edin
toplam = 0
gecici_sayi = sayi

while gecici_sayi > 0:
    basamak = gecici_sayi % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10

if sayi == toplam:
    print(sayi, "bir Armstrong sayısıdır.")
else:
    print(sayi, "bir Armstrong sayısı değildir.")
