


print("Vítejte v aplikaci pro výpočet obsahu obdélníku")

a = input("Zadejte délku a : ")
b = input ("Zadejte délku strany b :")

a = int(a)
b = int(b)

if a>0 and b>0:
    print("výsledek je: ")
    print(2*a+2*b)

else:
    print("copak to děláš? však si zadal záporné číslo")