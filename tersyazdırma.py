def cevirme(metin,sayi=[]):
    for i in range(len(metin)-1,-1,-1):
        sayi.append(metin[i])
    return "".join(sayi)

cumle = input("Cümle giriniz. ")
print("Tersi: {} ".format(cevirme(cumle)))