from datetime import *  #doğum günü kütüphanesini projemize ekliyoruz

birth = datetime.strptime(input("senin doğum günün(d.m.Y): "), "%d.%m.%Y") #kullanıcıdan doğum tarihini girmesini istiyoruz

age = datetime.now() - birth #bügünkü tarihten kullanıcının doğum tarihini çıkarıyoruz

print("EN=You lived {} seconds .".format(age.total_seconds()),"\nTR= {} saniye yaşadınız.".format(age.total_seconds())) #gün sayısını saniyeye çevirip ekrana yazdırıyoruz

