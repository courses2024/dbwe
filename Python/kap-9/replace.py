list1 = [5, 10, 15, 20, 25, 30, 5, 10, 15, 20, 25, 30]
print("Liste: ", list1)
zu_ersetzen = int(input("Geben Sie eine Zahl ein, die ersetzt werden soll: "))
ersetzen_mit = int(input(str(zu_ersetzen) +  " ersetzen durch: "))

# finde das erste Vorkommen von zu_ersetzen in der Liste list1
# und speichere den Index in der Variablen index
if zu_ersetzen in list1:
    index = list1.index(zu_ersetzen)
    # Ändere den Wert an der Stelle index in ersetzen_mit
    # und gebe die Liste aus
    list1[index] = ersetzen_mit
    # gebe die Liste aus
    print(list1)
else:
    # Falls zu_ersetzen nicht in der Liste ist, gebe eine Fehlermeldung aus
    print("Die Zahl", zu_ersetzen, "ist nicht in der Liste enthalten.")

