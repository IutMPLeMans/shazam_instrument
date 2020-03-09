# Projet de POO : Shazam_Instrument
# LE ROY Hugo
# 09/03/2020

# Calcul la foondamentale d'un fichier son à partir de "TraceTDF2"

import numpy as np
import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt
fichier=open("piano.txt","r") # Pour utiliser le fichier contenant les valeurs des harmoniques

harmonique=fichier.read() # On extrait les valeurset on les met dans f
n = harmonique.split('\t')
nbre_valeur = int(n[0])
f=[]
for idx in range(0,nbre_valeur):
    f.append(float(n[1+idx]))
print(f)

somme =0

for k in range (0, len(f)):  # On calcul la différence entre chaque harmonique (donc les fondamentales) et on fait une moyenne
    diff = abs(f[k]-f[k+1])
    somme = somme + diff
print(somme/len(f))