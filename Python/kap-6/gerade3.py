# gerade3.py prüft mit if und else, ob eine eingegebene Zahl gerade oder ungerade ist
eingabe = input("Bitte geben Sie eine ganze Zahl ein: ")
zahl = int(eingabe)
rest = zahl % 2

if rest == 0:
    print("Die Zahl", zahl, "ist gerade")
else:
    print("Die Zahl", zahl, "ist ungerade")