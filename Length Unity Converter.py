cns = input("[km]=kilometre\n[hm]=hektometre\n[dam]=dekametre\n[m]=metre\n[dm]=desimetre\n[cm]=santimetre\n[mm]=milimetre\nHangi cinsten değer gireeksiniz?")
if cns == "cm" :
    deger = int(input("bir değer giriniz"))
    print("mm : ",(deger*10)," \n"
          "dm : ",(deger/10)," \n"
          "m : ",(deger/100)," \n"
          "dam : ",(deger/1000)," \n"
          "hm : ",(deger/10000)," \n"
          "km : ",(deger/100000))
    
if cns == "km" :
    deger = int(input("bir değer giriniz"))
    print("mm : ",(deger*1000000)," \n"
          "cm : ",(deger*100000)," \n"
          "dm : ",(deger*10000)," \n"
          "m : ", (deger*1000)," \n"
          "dam : ",(deger*100)," \n"
          "hm : ",(deger*10))
    
if cns == "hm" :
    deger = int(input("bir değer giriniz"))
    print("mm : ",(deger*100000)," \n"
          "cm : ",(deger*10000)," \n"
          "dm : ",(deger*1000)," \n"
          "m : ",(deger*100)," \n"
          "dam : ",(deger*10)," \n"
          "km : ",(deger/10))
    
if cns == "dam" :
    deger = int(input("bir değer giriniz"))
    print("mm : ",(deger*10000)," \n"
          "cm : ",(deger*1000)," \n"
          "dm : ",(deger*100)," \n"
          "m : ",(deger*10)," \n"
          "hm : ",(deger/10)," \n"
          "km : ",(deger/100))   

if cns == "m" :
    deger = int(input("bir değer giriniz"))
    print("mm : ",(deger*1000)," \n"
          "cm : ",(deger*100)," \n"
          "dm : ",(deger*10)," \n"
          "dam : ",(deger/10)," \n"
          "hm : ",(deger/100)," \n"
          "km : ",(deger/1000))

if cns == "dm" :
    deger = int(input("bir değer giriniz"))
    print("mm : ", (deger*100)," \n"
          "cm : ",(deger*10)," \n"
          "m : ", (deger/10)," \n"
          "dam : ", (deger/100)," \n"
          "hm : ",(deger/1000)," \n"
          "km : ",(deger/10000))

if cns == "mm" :
    deger = int(input("bir değer giriniz"))
    print("cm : ",(deger/10)," \n"
          "dm : ",(deger/100)," \n"
          "m : ",(deger/1000)," \n"
          "dam : ",(deger/10000)," \n"
          "hm : ",(deger/100000)," \n"
          "km : ",(deger/1000000))
