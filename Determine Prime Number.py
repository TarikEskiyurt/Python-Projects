number=int(input("Please enter the number"))
counter=0

for i in range(2,number):
     if number%i==0:
          counter=counter+1

if counter > 0:
     print("It is not a prime number.")
else:
     print("Is the prime number.")
