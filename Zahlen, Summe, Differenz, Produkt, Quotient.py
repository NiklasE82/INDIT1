# Schreiben Sie kurzes Phyton-Programm, das Sie nach der Eingabe von 2 Zahlen fragt
# und danach die Summe, die Differenz, das Produkt und den Quotient der beiden Zahlen
# ausgibt.
#
# Schreiben Sie jeweils eine Funktion zur Berechnung von Summe, Different, Produkt und
# Quotient.
#
# Verhindern Sie das mathematisch unmögliche Berechnungen gestartet werden.

eingabe1 = float(input("Eingabe 1 Zahl: ")) #Eingabe Wert 1
eingabe2 = float(input("Eingabe 2 Zahl: ")) #Eingabe Wert 2

def summe(eingabe1, eingabe2):      
    zwischensumme = eingabe1 + eingabe2
    return (zwischensumme)

def differenz(eingabe1, eingabe2):      
    zwischendifferenz = eingabe1 - eingabe2
    return (zwischendifferenz)

def produkt(eingabe1, eingabe2):      
    zwischenprodukt = eingabe1 * eingabe2
    return (zwischenprodukt)

def quotient(eingabe1, eingabe2):
    if eingabe2 == 0:
        print("Division durch 0")
        return
    zwischenquotient = eingabe1 / eingabe2
    return (zwischenquotient)

Wert1 = summe(eingabe1, eingabe2)
Wert2 = differenz(eingabe1, eingabe2)
Wert3 = produkt(eingabe1, eingabe2)
Wert4 = quotient(eingabe1, eingabe2)

print("Summe: ", Wert1)
print("Differenz: ", Wert2)
print("Produkt: ", Wert3)
print("Quotient: ", Wert4)