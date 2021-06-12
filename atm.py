import os
import time

bky=0

a=int(input("TARIK BANKASI'na hoş geldiniz, yapmak istediğiniz işlemin numarasını aşağıdan seçiniz.\n[1]BAKİYE SORMA\n[2]PARA ÇEKME\n[3]PARA YATIRMA\n[4]ÇIKIŞ\n=> "))


while True:
    if a == 1:
        print("Bakiyeniz {} TL'dir.".format(bky))
        time.sleep(2)
        os.system('cls')
        a=int(input("Yapmak istediğiniz işlemin numarasını aşağıdan seçiniz.\n[1]BAKİYE SORMA\n[2]PARA ÇEKME\n[3]PARA YATIRMA\n[4]ÇIKIŞ\n=> "))

    if a == 2:
        b=int(input("Kaç TL çekmek istersiniz"))
        if b > bky:
            print("Yetersiz bakiye")
            time.sleep(2)
            os.system('cls')
            a=int(input("Yapmak istediğiniz işlemin numarasını aşağıdan seçiniz.\n[1]BAKİYE SORMA\n[2]PARA ÇEKME\n[3]PARA YATIRMA\n[4]ÇIKIŞ\n=> "))
        else:
            bky=bky - b
            print("Bakiyeniz {} TL'dir.".format(bky))
            time.sleep(2)
            os.system('cls')
            a=int(input("Yapmak istediğiniz işlemin numarasını aşağıdan seçiniz.\n[1]BAKİYE SORMA\n[2]PARA ÇEKME\n[3]PARA YATIRMA\n[4]ÇIKIŞ\n=> "))

    if a == 3:
        c=int(input("Kaç TL yatırmak istersiniz?"))
        bky= bky + c
        print("Bakiyeniz {} TL'dir.".format(bky))
        time.sleep(2)
        os.system('cls')
        a=int(input("Yapmak istediğiniz işlemin numarasını aşağıdan seçiniz.\n[1]BAKİYE SORMA\n[2]PARA ÇEKME\n[3]PARA YATIRMA\n[4]ÇIKIŞ\n=> "))

    if a == 4:
        print("Çıkış yapılıyor...")
        print("TARIK BANKASI'nı tercih ettiğiniz için teşekkür ederiz...")
        print("YİNE BEKLERİZ...")
        time.sleep(3)
        break

    
