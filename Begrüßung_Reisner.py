# Begrüßung Reisner 

# Schreiben Sie ein Programm, das in zwei Versionen, die in der Liste aufgeführten Personen begrüßt z.B.: "Hallo, Peter!"
# Version 1: for-Schleife im Hauptprogramm, Ausgabe der Begrüßung in einem Unterprogramm
# Version 2: for-Schleife und Ausgabe der Begrüßung in einem Unterprogramm

Namen = ["Peter", "Dora", "Kevin", "Fritz", "Sarah"] # Namensliste.

def Begrueßung(name):
    print("Hallo ", name) # Ausgabe
    print("Schön dich zu sehen!") # Ausgabe
    print("Viel Spaß mit dem Programm!") # Ausgabe
    return # Rückgabe 

def Begrueßung2(namensliste): 
    for ein_name in namensliste: # Schleife
        print("Hallo ", name, "!") # Ausgabe
        print("Schön dich zu sehen!") # Ausgabe
        print("Viel Spaß mit dem Programm!") # Ausgabe
    return

print("Version 1:") # Ausgabe
for name in Namen:  # Schleife
    Begrueßung(name)
    
print("") # Ausgabe (dient nur als Absatz)
    
print("Version 2:") # Ausgabe
Begrueßung2(Namen)