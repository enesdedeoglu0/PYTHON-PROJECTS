print("\nÜçgen   > 1  Dörtgen > 2 \n")
tip = int(input("Lütfen Üçgen'nin Mi Dörtgenin Mi tipini bulmak istiyorsunuz ?"))

liste = list()

if tip == 1:
    i =0
    while (i<3):
        kenar = int(input("Kenar uzunluğunu giriniz : "))
        liste.append(kenar)
        i+=1
    
    if ((abs(liste[0] + liste[1]) > liste[2]) and (abs(liste[2] + liste[1]) > liste[0]) and (abs(liste[2] + liste[0]) > liste[1])):
        if (liste[0] == liste[1] and liste[0] == liste[2]):
            print("Bu bir EŞKENAR Üçgen ")
        elif ((liste[0] == liste[1] and liste[0] != liste[2])   or   (liste[0] == liste[2] and liste[0] != liste[1]) or (liste[1] == liste[2] and liste[1] != liste[0])):
            print("Bu bir İKİZKENAR Üçgen")
        else:
            print("Bu bir ÇEŞİTKENAR Üçgen ")
    else:
        print("Girdiğiniz kenarlar üçgen belirtmiyor ")

elif tip == 2:
    i =0
    while (i<4):
        kenar = int(input("Kenar uzunluğunu giriniz : "))
        liste.append(kenar)
        i+=1
    
    if (liste[0] == liste[1] and liste[0] == liste[2] and liste[0] == liste[3]):
        print("Bu bir KARE ")
    elif (liste[0] == liste[1] and liste[2] == liste[3]):
        print("Bu bir DİKDÖRTGEN ")
    else:
        print("Bu bir DÖRTGEN ")

else:
 print("Geçersiz şekil")
