metin=input("Şifrelemek istediğiniz metni giriniz")
artmik=int(input("Artma miktarı  ne olsun"))
sifre=""

for k in metin:
    print(ord(k))
    print(k, "=>", chr(ord(k) + artmik))
    sifre = sifre + chr(ord(k) + artmik)

print(metin, " =>", sifre)

