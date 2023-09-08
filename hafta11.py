import math

# Kırmızı, yeşil ve mavi topların sayısı
kirmizi_top_sayisi = 5
yesil_top_sayisi = 4
mavi_top_sayisi = 3

# Toplardan seçilecek olan topların sayısı
secilecek_top_sayisi = 2

# Aynı renkteki topların kombinasyonlarını hesaplayın
kirmizi_kombinasyon = math.comb(kirmizi_top_sayisi, secilecek_top_sayisi)
yesil_kombinasyon = math.comb(yesil_top_sayisi, secilecek_top_sayisi)
mavi_kombinasyon = math.comb(mavi_top_sayisi, secilecek_top_sayisi)

# Topların aynı renkte olma olasılığını hesaplayın
ayni_renkte_olasilik = (kirmizi_kombinasyon + yesil_kombinasyon + mavi_kombinasyon) / math.comb(kirmizi_top_sayisi + yesil_top_sayisi + mavi_top_sayisi, secilecek_top_sayisi)

# Sonucu ekrana yazdırın
print("Topların aynı renkte olma olasılığı:", ayni_renkte_olasilik)

#------------------------------------------------------------------------------------#
yillik_hedef = 36

# Toplam ay sayısı
ay_sayisi = 12

# Her ay kaç kitap okuması gerektiğini hesaplayın
aylik_hedef = yillik_hedef / ay_sayisi

# Sonucu ekrana yazdırın
print("Her ay", aylik_hedef, "kitap okuması gerekmektedir.")
#--------------------------------------------------------------------------------------#