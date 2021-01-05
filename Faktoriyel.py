a=int(input("Enter the number which number do you want to take factorial."))
counter=a

if a == 0:
     print("1")

else:
     
     while counter > 1:
          counter = counter-1
          a=a*(counter)
     print(a)



