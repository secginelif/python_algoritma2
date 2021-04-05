def metin(cumle,sayi=0):
    harfler = "aeiıöoüuAEIİOÖUÜ"

    for harf in cumle:
        if harf in harfler:
            sayi += 1
    return sayi

cumle = input("Cümle giriniz. ")
print("Cümledeki ünlü harf sayısı {} ".format(metin(cumle)))