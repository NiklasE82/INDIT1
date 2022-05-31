
# Erweiterung der Woerterbuches
# 1. Verwendung von Assoziativ-Arrays (Dictionary)
# 2. Funktion zum Auslesen
# 3. Funktion um neue Wörter hinzuzufügen



mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon","pfirsich":"peach"}


print("Wählen Sie eine Funktion: ")
print("[A] = Wortabfrage")
print("[H] = Wort hinzufügen")

correct = False
    
while correct == False: # While Schleife
    eingabe = input("Auswahl Funktion: ") # Eingabe     
    if eingabe == "A":
                                        
        wort=input("Wort in DE: ")
        wort = wort.lower() # wandelt alles in Klienbuchstaben um 
        if wort in mein_woerterbuch:
            print("Wort in EN: ",mein_woerterbuch[wort]) # Übersetzung
        else:
            print('Nicht vorhanden')
    elif eingabe == "H":
        print("Eingabe nur in Kleinbuschstaben!",)   
        mein_woerterbuch[input('Wort in DE:')] = input('Wort in EN:') # Wort hinzufügen
          
    else:
        print("Nicht bekannt")