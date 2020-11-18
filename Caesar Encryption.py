metin=input("Şifrelemek istediğiniz metni giriniz")  #kullanıcının şifrelemek istediği metni soruyoruz
artmik=int(input("Artma miktarı  ne olsun")) #kullanıcıdan her bir rakamı kaç arttırarak metni şifrelemek istediğini soruyoruz
sifre=""

for k in metin:    #bütün rakamlara "artmik" teki değeri ekliyoruz ve şifrelenmiş metni "sifre" değişkenine atıyoruz
    print(ord(k))
    print(k, "=>", chr(ord(k) + artmik))
    sifre = sifre + chr(ord(k) + artmik)

print(metin, " =>", sifre) #şifrelenmiş metni ekrana yazdırıyoruz

