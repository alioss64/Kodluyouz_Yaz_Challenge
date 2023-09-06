# Kullanıcıdan bir sayı girişi alınır
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

# Faktöriyel hesaplama işlemi
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i

# Sonucu ekrana yazdırma
print(f"{sayi} faktöriyeli = {faktoriyel}")

#----------------------------------------------------------------------------------------------------#

