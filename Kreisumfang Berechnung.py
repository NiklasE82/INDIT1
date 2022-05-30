
#Schreiben Sie ein Programm, das nach Eingabe der Radius in einer Funktion den Kreisumfang berechnet.
#Verwenden Sie dazu die Konstante pi aus dem math-Paket
#
#Die Eingabe soll in einer eigenen Funktion erfolgen, in der sichergestellt wird das es sich dabei
#  a) jedenfalls um eine Zahl handelt
# und
#  b) eine positive Zahl handelt

import math

def eingabe():
    correct = False
    while correct == False:
        radius = input("Eingabe Radius: ")
        try: 
            rad = float(radius)     
            if rad > 0:
                correct = True                
            else:
                print("Zahl ungültig!! (bitte eine positive Zahl eingeben) ")
        except ValueError:
            print("Eingabe ungültig!! (bitte eine positive Zahl eingeben)")
    return rad

def kreisumfang(radius):
    umfang = 2*radius*math.pi
    return umfang

kreisradius = eingabe()
print("Eingegebener Radius: ", kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang beträgt: ", umfang)