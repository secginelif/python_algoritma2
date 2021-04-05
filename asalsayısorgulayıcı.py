def asalsayı_sorgulama(sayi):
    if (sayi>1):
        for i in range(2,sayi):
            if sayi%i ==0:
                return False
        return True
    else:
        return False     

while True:
    if(asalsayı_sorgulama(int(input("Sorgulamak istediğiniz sayı: ")))):
        print("Asaldır")
    else:
        print("Asal Degildir")
    if(input("Devam etmek için herhangi bir tuşa basın")):
        continue