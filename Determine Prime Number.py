number=int(input("Please enter the number")) #I take a number from user
counter=0

for i in range(2,number):
     if number%i==0:
          counter=counter+1 

if counter > 0:
     print("It is not a prime number.")  #I print outout to screen
else:
     print("Is the prime number.")  #I print outout to screen

