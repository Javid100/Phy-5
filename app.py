#Tapsiriq 1
money=int(input("PPulu yaz: "))
convert=int(input("Pulu Avroya(1) Rubla(2) Dollara(3) cevir:"))
def moneyconverter(a,b):
    if a==1:
        print(f"Your money in Euro equals to {b*0.56}")
    elif a==2:
        print(f"Your money in Dollar equals to {b*0.59}")
    elif a==3:
        print(f"Your money in Rubl equals to {b*57.47}")
    else:
        print("ERROR")



#Tapsiriq2
qram=int(input("Qrami dxil et: "))
if qram>0 and qram<100:
    print(f"Endirim qiymet {qram}")
elif qram>100 and qram<200:
    print(f"Endirim iymet {qram-((qram/100)*3)}")
elif qram>200 and qram<300:
    print(f"Endirim qiymet {qram-((qram/100)*5)}")
else:
    print(f"Endirim qiymet {qram-((qram/100)*7)}")

#Tapsiiq3


#Tapsiriq4
hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
if hour <= 24 and minute<= 60:
    print("Saat duzdur")
else:
    print("Saat sefdir")