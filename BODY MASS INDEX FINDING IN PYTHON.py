boy = float(input("Lutfen boyunuzu  giriniz  :"))
kilo = int(input("Lutfen  kilonuzu giriniz  :"))

float = bki = kilo / (boy ** 2)
print("Vucut kitle endeksiniz : {}\n".format(bki))

if bki < 18:
    print("Zayıf")
elif 18 < bki < 25:
    print("Gayet Normal")
elif 25 < bki < 30:
    print("Hafif Şişman")
elif 30 < bki < 35:
    print("Obez")
else:
    print("Sağlık açısından tehlikeli")