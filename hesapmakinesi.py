sayi1 = int(input("Sayı1: "))
sayi2 = int(input("Sayı2: "))

print("Toplama için 1")
print("Çıkarma için 2")
print("Çarpma için 3")
print("Bölme için 4")
islem = int(input("İşleminizi seçiniz. "))

if (islem==1):
    sonuc=sayi1+sayi2
elif (islem==2):
    sonuc=sayi1-sayi2
elif (islem==3):
    sonuc=sayi1*sayi2
elif (islem==4):
    sonuc=sayi1/sayi2

print("İşleminizin sonucu: {}".format(sonuc))

