height = int(input("noel ağacının yüksekliği: "))

for i in range(int(height * 0.7)):
    print( (" " * (height - (i // 2))) + ("*" * i))

for i in range(int(height * 0.7), height):
    print((" " * (height - 1)) + "||")
