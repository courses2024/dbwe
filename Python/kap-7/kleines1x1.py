# kleinex1x1.py gibt das kleine 1x1 einer Zahl aus
zahl = int(input("Geben Sie die Zahl ein: "))
faktor = 1
print("Kleines 1 x", zahl)
while faktor <= 10:
    print(faktor, "x", zahl, "=", zahl * faktor)
    faktor = faktor + 1