# Kullanıcıdan bir sayı girişi alın
sayi = int(input("Bir sayı girin: "))

# Sayının tek veya çift olduğunu kontrol edin
if sayi % 2 == 0:
    print(sayi, "çift bir sayıdır.")
else:
    print(sayi, "tek bir sayıdır.")

#-----------------------------------------------------------------------------#

# Bir örnek dizi oluşturun
dizi = [6, 31, 53, 26, 98, 64, 52]

# Çift sayıların toplamını saklayacak bir değişkeni başlatın
cift_sayilar_toplami = 0

# Dizi üzerinde dönerek çift sayıları bulun ve toplamı hesaplayın
for sayi in dizi:
    if sayi % 2 == 0:
        cift_sayilar_toplami += sayi

# Sonucu ekrana yazdırın
print("Dizideki çift sayıların toplamı:", cift_sayilar_toplami)
