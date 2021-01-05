sayi=int(input("Please enter the number"))
sayac=0

for i in range(2,sayi):
     if sayi%i==0:
          sayac=sayac+1

if sayac > 0:
     print("It is not a prime number.")
else:
     print("Is the prime number.")
