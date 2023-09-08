# 3 puanlık atışlarda isabet sayısı
isabet_3_puan = 5

# 2 puanlık atışlarda isabet sayısı
isabet_2_puan = 10

# Toplam puanı hesaplayın
toplam_puan = (3 * isabet_3_puan) + (2 * isabet_2_puan)

# Sonucu ekrana yazdırın
print("Toplam puan:", toplam_puan)

#----------------------------------------------------------------------------#

# Ürün fiyatlarını tanımlayın
kitap_fiyati = 80  # Bir kitabın fiyatı (TL)
defter_fiyati = 20  # Bir defterin fiyatı (TL)
kalem_fiyati = 5  # Bir kalemim fiyatı (TL)

# Müşterinin alışveriş miktarlarını tanımlayın
kitap_adedi = 2
defter_adedi = 3
kalem_adedi = 4

# Toplam maliyeti hesaplayın
toplam_maliyet = (kitap_fiyati * kitap_adedi) + (defter_fiyati * defter_adedi) + (kalem_fiyati * kalem_adedi)

# Sonucu ekrana yazdırın
print("Müşteri ödemesi gereken toplam miktar:", toplam_maliyet, "TL")

#--------------------------------------------------------------------------------------------------#
import math

# Toplam öğrenci sayısı
toplam_ogrenci = 30

# Seçilecek öğrenci sayısı
secilecek_ogrenci_sayisi = 4

# Kombinasyon hesaplaması yapın (30 öğrenci arasından 4 kişiyi seçme)
farkli_sekiller = math.comb(toplam_ogrenci, secilecek_ogrenci_sayisi)

# Sonucu ekrana yazdırın
print(f"{toplam_ogrenci} öğrenci arasından {secilecek_ogrenci_sayisi} kişi seçmenin farklı şekilleri: {farkli_sekiller}")
