eingabe = input("Bitte geben Sie eine ganze Zahl ein: ")
zahl = int(eingabe)
rest = zahl % 2

if rest == 0:
    print("Die Zahl", zahl, "ist gerade")
if rest == 1:
    print("Die Zahl", zahl, "ist ungerade")