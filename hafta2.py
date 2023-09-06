def asal_mi(sayi):
    if sayi <= 1:
        return False
    elif sayi <= 3:
        return True
    elif sayi % 2 == 0 or sayi % 3 == 0:
        return False
    i = 5
    while i * i <= sayi:
        if sayi % i == 0 or sayi % (i + 2) == 0:
            return False
        i += 6
    return True

# Kullanıcıdan bir sayı alın
sayi = int(input("Bir sayı girin: "))

# Sayının asal olup olmadığını kontrol edin ve sonucu ekrana yazdırın
if asal_mi(sayi):
    print(f"{sayi} asal bir sayıdır.")
else:
    print(f"{sayi} asal bir sayı değildir.")



#------------------------------------------------------------------------------------------------#

kelime = input("Bir kelime girin: ")

# Kelimenin harflerini büyük harfe dönüştür
buyuk_harfler = kelime.upper()

# Sonucu ekrana yazdır
print("Kelimenin büyük harf hali:", buyuk_harfler)


#---------------------------------------------------------------------------------------------#




