""" 
Im Programm eintritt3.py in Kapitel 6 wurden zwei Bedingungen überprüft und mit or ver-knüpft.
if antwort == 'J' or antwort == 'j':
ist_student = True
Wie könnte das mithilfe einer Liste gelöst werden, die verschiedene denkbare Antworten (z.B. ‘J’, ‘j’, ‘Ja’, ‘ja’, ‘JA’, ‘Yep’, ‘Aber sicher’, ‘Jawohl’ oder ‘Klar, Mann’) enthält?

"""

# Die Liste antworten enthält alle denkbaren Antworten, die als Ja gewertet werden.
antworten = ['J', 'j', 'Ja', 'ja', 'JA', 'Yep', 'Aber sicher', 'Jawohl', 'Klar, Mann']
antwort = input("Sind Sie Student? (J/N): ")
if antwort in antworten:
    # Wenn die Eingabe des Benutzers in dieser Liste enthalten ist, wird ist_student auf True gesetzt.
    ist_student = True
else:
    # Andernfalls wird ist_student auf False gesetzt.
    ist_student = False
print("Ist Student:", ist_student)
# Dies ist eine einfache und effektive Möglichkeit, mehrere Bedingungen zu überprüfen, ohne viele or-Bedingungen verwenden zu müssen.   