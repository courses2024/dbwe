preise = [199.33, 2030.50, 320789, 0.99]
steuersatz = 8.1
pos = 0
print("Position {0:>15s} {1:>15s}".format('Netto', 'Brutto'))
for preis in preise :
    pos += 1
    bruttopreis = preis + preis / 100 * steuersatz
    print("{0:<8d} {1:15.2f} {2:>15.2f}".format(pos, preis, bruttopreis))

