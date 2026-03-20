# Taş , Kağıt , Makas Oyunu

import random
isim = input("Lütfen kullanıcı adı giriniz : ")
os = 0
bp = 0
kp = 0
while True:
    bs = 0
    bss = random.randint(1, 3)
    if bss == 1:
        bs = "taş"
    elif bss == 2:
        bs = "kağıt"
    else:
        bs = "makas"

    ks = input("Taş , Kağıt , Makas :").lower()

    if ks != "taş" and ks != "kağıt" and ks != "makas":
        print("Yanlış tuşlama yaptınız.!")
        continue
    os += 1
    print("Bilgisayar Seçimi : " + bs)
    if ks == bs:
        os -= 1
        print("Berabere")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))
    elif ks == "taş" and bs == "makas":
        kp += 1
        print("Kullanıcı Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    elif ks == "taş" and bs == "kağıt":
        bp += 1
        print("Bilgisayar Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    elif ks == "kağıt" and bs == "taş":
        kp += 1
        print("Kullanıcı Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    elif ks == "kağıt" and bs == "makas":
        bp += 1
        print("Bilgisayar Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    elif ks == "makas" and bs == "taş":
        bp += 1
        print("Bilgisayar Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    elif ks == "makas" and bs == "kağıt":
        kp += 1
        print("Kullanıcı Kazandı!!")
        print("{} puanı : {}".format(isim, kp))
        print("Bilgisayar puanı : {}".format(bp))

    if os == 5:
        print("OYUN BİTTİ!!!! ")
        print("PUAN DURUMU!!!")
        print("{} Puanı : {}".format(isim, kp))
        print("Bilgisayar Puanı : {}".format(bp))
        if bp > kp:
            print("Oyunu Bilgisayar Kazandı!!!!")
        elif bp == kp:
            print("Oyun berabere bitti!!!!")
        else:
            print("Oyunu {} Kazandı!!!!".format(isim))
        soru = input("Yeniden oynamak ister misiniz ? ").lower()
        if soru == "evet":
            kp = 0
            os = 0
            bp = 0
            continue
        else:
            break


