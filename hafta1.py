from datetime import datetime

# Kullanıcıdan doğum tarihi bilgisini alıdık.
doğum_tarihi = input("Doğum tarihinizi (YYYY-MM-DD formatında) girin: ")

# Şu anki tarih bilgisini aldık.
şu_an = datetime.now()

# Doğum tarihini 'YYYY-MM-DD' formatına çevirin
doğum_tarihi = datetime.strptime(doğum_tarihi, "%Y-%m-%d")

# Yaş hesabını yaptık
yaş = şu_an.year - doğum_tarihi.year - ((şu_an.month, şu_an.day) < (doğum_tarihi.month, doğum_tarihi.day))

print(f"Siz {yaş} yaşindasiniz.")

#----------------------------------------------------------------------------------------------------#
from collections import Counter

# Kullanıcıdan metni alın
metin = input("Bir metin girin: ")

# Metindeki harf sayılarını hesaplayın
harf_sayilari = Counter(metin)

# En çok tekrar eden harfi ve kaç kere tekrar ettiğini bulun
en_cok_tekrar_eden_harf, tekrar_sayisi = harf_sayilari.most_common(1)[0]

# Sonucu ekrana yazdırın
print(f"'{en_cok_tekrar_eden_harf}' harfi metinde en çok tekrar eden harftir ve {tekrar_sayisi} kere tekrar etmektedir.")
#---------------------------------------------------------------------------------------------------#
def hedef_sayiyi_ulaştır(dizi, hedef):
    def toplam_kombinasyonlar(dizi, hedef, indeks, kombinasyon):
        if hedef == 0:
            sonuç.append(kombinasyon)
            return
        if hedef < 0 or indeks == len(dizi):
            return

        # Mevcut elemanı dahil etmeyi dene
        toplam_kombinasyonlar(dizi, hedef - dizi[indeks], indeks, kombinasyon + [dizi[indeks]])
        # Mevcut elemanı dahil etmeme seçeneğini dene
        toplam_kombinasyonlar(dizi, hedef, indeks + 1, kombinasyon)

    sonuç = []
    toplam_kombinasyonlar(dizi, hedef, 0, [])
    return sonuç

# Kullanıcıdan tam sayı dizisini ve hedef sayıyı alın
dizi = list(map(int, input("Bir tam sayı dizisi girin (boşlukla ayırın): ").split()))
hedef = int(input("Hedef sayıyı girin: "))

# Hedefe ulaşan kombinasyonları hesaplayın
sonuçlar = hedef_sayiyi_ulaştır(dizi, hedef)

# Sonuçları ekrana yazdırın
if sonuçlar:
    print(f"Hedef sayıya ({hedef}) ulaşan kombinasyonlar:")
    for kombinasyon in sonuçlar:
        print(kombinasyon)
else:
    print("Hedef sayıya ulaşan bir kombinasyon bulunamadı.")




