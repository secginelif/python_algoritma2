import random
import time

a = 1
while True:
    zar1 = random.randint(1,6)
    zar2 = random.randint(1,6)

    if zar1==6 and zar2==6:
        print("Deneme {} : ({}) ({})".format(a,zar1,zar2))
        time.sleep(1)
        break
    print("Deneme {} : ({}) ({})".format(a,zar1,zar2))
    a +=1
    time.sleep(1)

print(" {}. denemede (6,6) gelmiştir.".format(a))


