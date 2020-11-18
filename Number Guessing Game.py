import random as r  #projemize random kütüphanesini ekliyoruz

rastgele=r.randint(1,100)  #"rastgele" değişkenine 1 ile 100 arasında herhangi bir sayıyı atıyoruz

tahmins=0   #"tahmins" değişkenine ilk olarak 0'ı atıyoruz



sayi=int(input("1 ile 100 arasında bir sayı tuttum, bil bakalım kaç?"))  #kullanıcıdan sayıyı tahmin etmesini istiyoruz
while True:
    
    if sayi > rastgele:
        tahmins = tahmins + 1
        print("Daha küçük bir sayı giriniz")  #kullanıcının girdiği sayı, rastgele tutulan sayıdan büyükse tekrar denemesini söylüyoruz
        sayi=int(input("----------------------------------\nBir daha tahmin et"))
    

    elif sayi < rastgele:
        tahmins = tahmins + 1
        print("Daha büyük bir sayı giriniz")  #kullanıcının girdiği sayı, rastgele tutulan sayıdan küçükse tekrar denemesini söylüyoruz
        sayi=int(input("----------------------------------\nBir daha tahmin et"))

    else:
        tahmins = tahmins + 1
        print("Tebrikler, ",tahmins," seferde bildiniz...")  #eğer cevap doğruysa kullanıcıyı tebrik edip programdan çıkış yapıyoruz
        break

