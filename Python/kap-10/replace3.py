"""
replace3.py
Variante zu replace2.py mit list comprehension
Dieses Programm erzeugt eine neuen Liste und ersetzt dabei alle Vorkommen einer gesuchten Zahl .
"""
list1 = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]
print("Liste: ", list1)
zu_ersetzen = int(input("Geben Sie eine Zahl ein, die ersetzt werden soll: "))
ersetzen_mit = int(input(str(zu_ersetzen) +  " ersetzen durch: "))

# finde alle Vorkommen von zu_ersetzen in der Liste list1
# und ersetze sie mit ersetzen_mit. Variante 3 mit list comprehension

if zu_ersetzen in list1:
    list2 = [ersetzen_mit if x == zu_ersetzen else x for x in list1]
    # gebe die Liste aus
    print(list2)
else:
    # Falls zu_ersetzen nicht in der Liste ist, gebe eine Fehlermeldung aus
    print("Die Zahl", zu_ersetzen, "ist nicht in der Liste enthalten.")
