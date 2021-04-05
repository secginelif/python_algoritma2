import time
import datetime

print("3")
time.sleep(0.3)
print("2")
time.sleep(0.3)
print("1")
time.sleep(0.3)

zaman = datetime.datetime.now()

metin = input("Cümle yazınız: ")    
zaman2 = datetime.datetime.now()
yazim_hizi = zaman2-zaman
saniye = round(yazim_hizi.total_seconds(),2)
zaman3 = round(len(metin)/saniye,1)

print("Toplam süre: {}".format(saniye))
print("{} kelime başına saniye".format(zaman3))

print("----------")

