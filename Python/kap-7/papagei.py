# papagei.py - Ein Papagei, der alles nachplappert, 
# bis der Benutzer "Ende" oder "Schluss" eingibt
while True:
    antwort = input("Erzähl mir was :")
    if antwort == "Ende" or antwort == "Schluss":
        print("War schön mit Dir zu reden")
        break
    print(antwort)