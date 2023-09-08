# Kullanıcıdan iki sayı girişi alın
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# İki sayının toplamını hesaplayın
toplam = sayi1 + sayi2

# Sonucu ekrana yazdırın
print("Toplam:", toplam)

#----------------------------------------------------------------------------#

import math

# Kullanıcıdan bir sayı girişi alın
sayi = float(input("Bir sayı girin: "))

# Sayının karekökünü hesaplayın
karekok = math.sqrt(sayi)

# Karekökün tam olarak çıkıp çıkmadığını kontrol edin
if karekok.is_integer():
    print(f"{sayi} sayısının karekökü tam olarak {int(karekok)} çıkar.")
else:
    print(f"{sayi} sayısının karekökü tam olarak çıkmaz.")
