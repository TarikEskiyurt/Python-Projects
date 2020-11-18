import math

a=int(input("ALTI İŞLEM MAKİNESİNE HOŞ GELDİNİZ, YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

while True:
    if a == 1:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))
        toplam=sayi1 + sayi2
        print("Toplam => ",toplam,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 2:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))
        fark=sayi1 - sayi2
        print("Fark=> ",fark,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 3:
        sayi1=int(input("Böleceğiniz sayıyı giriniz"))
        sayi2=int(input("Girdiğiniz sayıyı kaça böleceksiniz"))
        bölüm=sayi1 / sayi2
        print("Bölüm => ",bölüm,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 4:
        sayi1=int(input("1. sayıyı giriniz"))
        sayi2=int(input("2. sayıyı giriniz"))
        çarpım=sayi1 * sayi2
        print("Çarpım => ",çarpım,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

    if a == 5:
        sayi1=int(input("Sayıyı giriniz"))
        sayi2=int(input("Sayının üssünü giriniz"))
        kare=sayi1 ** sayi2
        print("Sayının karesi => ",kare,"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))
    
    if a == 6:
        sayi=int(input("Karekökünü almak istediğiniz sayıyı giriniz."))
        math.sqrt(sayi)
        print("Karekök => ",math.sqrt(sayi),"\n------------------------------------\n")
        a=int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİN NUMARASINI AŞAĞIYA YAZINIZ...\n[1]TOPLAMA\n[2]ÇIKARMA\n[3]BÖLME\n[4]ÇARPMA\n[5]SAYININ KARESİNİ ALMA\n[6]SAYININ KAREKÖKÜNÜ ALMA\n"))

