yrcp=int(input("Dairenizin yarıçapını giriniz")) #kullanıcıya çevresini bulmak istediği çemberin yarıçapını soruyoruz
cevre=2*3.14*yrcp #çevreyi hesaplıyoruz ve "cevre" değişkenine atıyoruz

if cevre <= 0:
    print("Pozitif değer giriniz")    #yarıçap negatif bir değer ise pozitif değer girmesini istiyoruz

if cevre == str:
    print("Lütfen bir sayı giriniz")  #kullanıcı yarıçapa bir karakter girmişse, sadece sayı girmesini istiyoruz

print("dairenin çevresi :",cevre) #dairenin çevresini ekrana yazdırıyoruz
