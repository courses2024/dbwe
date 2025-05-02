"""
replace2.py, Variante von replace.py aus Kap 9
Dieses Programm ersetzt alle Vorkommen einer gesuchten Zahl in der gleichen Liste.
"""
list1 = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]
print("Liste: ", list1)
zu_ersetzen = int(input("Geben Sie eine Zahl ein, die ersetzt werden soll: "))
ersetzen_mit = int(input(str(zu_ersetzen) +  " ersetzen durch: "))

if zu_ersetzen in list1:
    # finde alle Vorkommen von zu_ersetzen in der Liste list1
    # und ersetze sie mit ersetzen_mit. Variante 2 mit Schleife
    for i in range(len(list1)):
        if list1[i] == zu_ersetzen:
            list1[i] = ersetzen_mit
    # Liste ausgeben    
    print(list1)
else:
    # Falls zu_ersetzen nicht in der Liste ist, gebe eine Fehlermeldung aus
    print("Die Zahl", zu_ersetzen, "ist nicht in der Liste enthalten.")