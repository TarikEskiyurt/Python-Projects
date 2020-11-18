height = int(input("noel ağacının yüksekliği: ")) #kullanıcıdan noel ağacının yüksekliğini girmesini istiyoruz

for i in range(int(height * 0.7)):
    print( (" " * (height - (i // 2))) + ("*" * i)) #noel ağacının yapraklarını ekrana yazdırıyoruz

for i in range(int(height * 0.7), height):
    print((" " * (height - 1)) + "||")   #noel ağacının gövdesini ekrana yazdırıyoruz
