print("Vítejte v aplikaci pro výpočet vzorečků pro obdelník/kvádru")

print("Pro výpočet objemu zadejte 1.")
print("Pro výpočet obvodu zadejte 2.")
print("Pro výpočet obsahu zadejte 3.")
print("Pro ukončení zadejte 4.")

volba = input("Zadejte vaši volbu: ")

if volba == "1":
    print("Zadejte v dm")
    a = int(input("Zadejte stranu a: "))
    a = int(input("Zadejte stranu b: "))
    a = int(input("Zadejte stranu c: "))

    if a>0 and b>0 and c>0:
        vysledek = a*b*c
        print("Objem kvádru je: ", vysledek, " litrů")
    else:
        print("Co to děláš kámo?")

elif volba == "2":
    print("Pro výpočet obvodu zadávejte délku strany v cm")
    a = int(input("Zadejte stranu a: "))
    a = int(input("Zadejte stranu b: "))

elif volba =="3":
print("Pro výpočet obsahu zadávejte délku strany")

