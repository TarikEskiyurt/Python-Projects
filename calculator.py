import math

a=int(input("ALTI İŞLEM MAKİNESİNE HOŞ GELDİNİZ, YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))  #kullanıcıya hangi işlemi yapmak istediğini soruyoruz

while True:
    if a == 1:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))   #kullanıcıdan toplamak istediği iki sayıyı girmesini istiyoruz ve toplamı ekrana yazdırıyoruz
        toplam=sayi1 + sayi2
        print("Toplam => ",toplam,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 2:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))      #kullanıcıdan çıkarmak istediği iki sayıyı girmesini istiyoruz ve farkı ekrana yazdırıyoruz
        fark=sayi1 - sayi2
        print("Fark=> ",fark,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 3:
        sayi1=int(input("Böleceğiniz sayıyı giriniz"))
        sayi2=int(input("Girdiğiniz sayıyı kaça böleceksiniz"))    #kullanıcıdan bölmek istediği sayıyı ve kaça bölmek istediğini soruyoruz. Ardından bölümü ekrana yazdırıyoruz
        bölüm=sayi1 / sayi2
        print("Bölüm => ",bölüm,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 4:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))       #kullanıcıdan çarpmak istediği iki sayıyı girmesini istiyoruz. Ardından çarpımı ekrana yazdırıyoruz
        çarpım=sayi1 * sayi2
        print("Çarpım => ",çarpım,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 5:
        sayi1=int(input("Sayıyı giriniz"))
        sayi2=int(input("Sayının üssünü giriniz"))     #kullanıcıdan üssün almak istediği sayıyı ve üssünü girmesini istiyoruz. Ardından sonucu ekrana yazdırıyoruz
        kare=sayi1 ** sayi2
        print("Sayının karesi => ",kare,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))
    
    if a == 6:
        sayi=int(input("Karekökünü almak istediğiniz sayıyı giriniz."))          #kullanıcıdan karekökünü almak istediği sayıyı girmesini istiyoruz. Ardından sonucu ekrana yazdırıyoruz
        math.sqrt(sayi)
        print("Karekök => ",math.sqrt(sayi),"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

