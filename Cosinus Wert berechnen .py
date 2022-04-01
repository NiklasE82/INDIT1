# Lab 2/1:
# Programm, das in 10 Grad-Schritten zwischen 0 Grad und 180 Grad den jew. Cosinus-Wert berechnet und ausgibt

inta=10
intb=181

while inta < intb:
    
    from math import *
    Erg = cos(radians(inta))
    floatErg = float(Erg)
    inta += 10

    print("Cosinus Wert:", floatErg)



    