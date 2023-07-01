# masa=input("Podaj wage:")
# jednostka=input("Czy użyto (K)g czy (L)bs? ")
# if (jednostka=="K" or jednostka=="k" ):
#     lbs=round(float(masa)*2.20462,2)
#     print("Waga w lbs " , lbs)
# elif (jednostka=="L" or jednostka=="l"):
#     kg=(round(float(masa)*0.453592,2))
#     print("Waga w kg " , kg)
# else:
#     print("Błąd")
# 22
ilosc_kart=range(54)
talia_kart=[]
for karta in ilosc_kart:
        for kolor in range(4):
            talia_kart.append(karta+1)           
print(talia_kart)        

