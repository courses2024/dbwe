"""
beersong.py demonstriert die Vewendung einer while-Schleife
In jedem Durchlauf wird eine Flasche Bier ausgetrunken, ein Text ausgegeben und 
die Anzahl der Flaschen im Kühlschrank wird um 1 reduziert.  
Die Text-Ausgabe erfolgt abhängig davon, ob es sich um eine oder mehrere Flaschen handelt.
"""

# Variablen deklarieren
text1 = "Flaschen Bier"
text2 = "Im Kühlschrank"
anzahl_flaschen=0

print("Der Kühlschrank ist leer.")
# Eingabe des Startwerts
anzahl_flaschen= int(input('Wieviele Flaschen Bier kaufen? '))

# Trink-Schleife
while anzahl_flaschen > 0:
    if anzahl_flaschen == 1:
        text1 = "Flasche Bier"
    print(anzahl_flaschen, text1, text2)
    print(anzahl_flaschen, text1)
    print("Nimm eine raus")
    print("Trink sie aus")
    print()
    anzahl_flaschen -= 1

print("Der Kühlschrank ist leer ...\n")