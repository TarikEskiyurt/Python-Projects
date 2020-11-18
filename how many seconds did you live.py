from datetime import *

birth = datetime.strptime(input("senin doğum günün(d.m.Y): "), "%d.%m.%Y")

age = datetime.now() - birth

print("EN=You lived {} seconds .".format(age.total_seconds()),"\nTR= {} saniye yaşadınız.".format(age.total_seconds()))
