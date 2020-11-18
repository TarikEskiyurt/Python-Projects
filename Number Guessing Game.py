import random as r

rastgele=r.randint(1,100)

tahmins=0



sayi=int(input("1 ile 100 arasında bir sayı tuttum, bil bakalım kaç?"))
while True:
    
    if sayi > rastgele:
        tahmins = tahmins + 1
        print("Daha küçük bir sayı giriniz")
        sayi=int(input("----------------------------------\nBir daha tahmin et"))
    

    elif sayi < rastgele:
        tahmins = tahmins + 1
        print("Daha büyük bir sayı giriniz")
        sayi=int(input("----------------------------------\nBir daha tahmin et"))

    else:
        tahmins = tahmins + 1
        print("Tebrikler, ",tahmins," seferde bildiniz...")
        break


