hiz = 60  
mesafe = 240  
zaman = mesafe / hiz

print("Araba", zaman, "saatte", mesafe, "km yol alır.")

#----------------------------------------------------------------------------------------------------#
toplam_hayvan_sayisi = 36
toplam_bacak_sayisi = 100

# Tavukların bacak sayısı
tavuk_bacak_sayisi = 2

# Koyunların bacak sayısı
koyun_bacak_sayisi = 4

# Tavuk sayısını hesapla
tavuk_sayisi = (toplam_bacak_sayisi - (koyun_bacak_sayisi * toplam_hayvan_sayisi)) / (tavuk_bacak_sayisi - koyun_bacak_sayisi)

# Koyun sayısını hesapla
koyun_sayisi = toplam_hayvan_sayisi - tavuk_sayisi

print("Çiftlikte", int(tavuk_sayisi), "tavuk ve", int(koyun_sayisi), "koyun bulunmaktadır.")

#-------------------------------------------------------------------------------------------------#

