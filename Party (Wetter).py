#  Party Beispiel

wetter = input("WE-Wetter - 'sonnig' oder 'regnerisch' : ")

#  doppeltes = Zeichen stellt einen Vergleichoperator dar

if wetter.upper() == "SONNIG":
    print("Gartenparty")
    print("Jippieeehhh")
elif wetter.lower() == "regnerisch":
    print("Kellerparty")
    print("Mist")
else:
    print("Bitte entweder 'regnerisch' oder 'sonnig' eingeben.")