import random

def isim_olustrma():
    isim = ["Ali","Esra","Salih","Elif"]
    soyad = ["Seçgin","Ozkan","Kara"]

    return "{} {} ".format(random.choice(isim),random.choice(soyad))

for i in range(10):
    print(isim_olustrma())
