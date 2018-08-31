#Write by BURAK UĞUR
print("""*******************************ZAR OYUNUNA HOŞGELDİNİZ*********************""")
import time
import random


donus=0
tahmin=int(input("Kaç deneme sonra tüm zarların üst yüzü 6 olur ?   "))
while True:

    zar1=(1,2,3,4,5,6)
    zar2=(1,2,3,4,5,6)
    x=random.choice(zar1)
    y=random.choice(zar2)


    if(x==y==6):

        time.sleep(2)
        print("İlk zar:",x)
        print("İkinci zar:",y)
        print("    TEBRİKLERRR      \n  Zarların üst yüzü 6 sayısını göstermektedir \n  Oyunu Kazandınız")
        donus+=1
        break


    else:

        print("Zarlar 6 sayısını göstermiyor...")
        time.sleep(1)
        print("İlk zar:",x)
        print("İkinci zar:",y)
        print("Bir daha deneniyor..\n\n")
        time.sleep(2)
        donus += 1

    if(donus == tahmin):
        print("Hakkınız doldu \n Oyunu kazanamadınız...")
        break