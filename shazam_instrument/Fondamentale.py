# Projet de POO : Shazam_Instrument
# LE ROY Hugo
# 09/03/2020

# Calcul la foondamentale d'un fichier son à partir de "TraceTDF2"

import numpy as np
import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt


fichierBasson=open(r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\basson.txt") # Pour utiliser le fichier contenant les valeurs des harmoniques
fichiermarimba=open(r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\marimba.txt")
fichierpiano=open(r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\piano.txt")
fichiersaxo=open(r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\saxo.txt")


##########################################################################################Pour le Basson#######################################################################################
harmonique=fichierBasson.read() # On extrait les valeurs et on les met dans f
n = harmonique.split('\t')
nbre_valeur = int(n[0])
f=[]
for idx in range(0,nbre_valeur):
    f.append(float(n[1+idx]))
#print(f)

somme =0

for k in range (0, len(f)-1):  # On calcul la différence entre chaque harmonique (donc les fondamentales) et on fait une moyenne
    diff = abs(f[k]-f[k+1])
    somme = somme + diff
fbas=somme/len(f);
print("la fondamentale du basson est:" ,fbas)


##########################################################################################Pour le marimba#######################################################################################
harmonique=fichiermarimba.read() # On extrait les valeurs et on les met dans f
n = harmonique.split('\t')
nbre_valeur = int(n[0])
f=[]
for idx in range(0,nbre_valeur):
    f.append(float(n[1+idx]))
#print(f)

somme =0

for k in range (0, len(f)-1):  # On calcul la différence entre chaque harmonique (donc les fondamentales) et on fait une moyenne
    diff = abs(f[k]-f[k+1])
    somme = somme + diff
fmari=somme/len(f);
print("la fondamentale du marimba est:" ,fmari)


##########################################################################################Pour le piano#######################################################################################
harmonique=fichierpiano.read() # On extrait les valeurs et on les met dans f
n = harmonique.split('\t')
nbre_valeur = int(n[0])
f=[]
for idx in range(0,nbre_valeur):
    f.append(float(n[1+idx]))
#print(f)

somme =0

for k in range (0, len(f)-1):  # On calcul la différence entre chaque harmonique (donc les fondamentales) et on fait une moyenne
    diff = abs(f[k]-f[k+1])
    somme = somme + diff
fpia=somme/len(f);
print("la fondamentale du piano est:" ,fpia)


##########################################################################################Pour le saxo#######################################################################################
harmonique=fichiersaxo.read() # On extrait les valeurs et on les met dans f
n = harmonique.split('\t')
nbre_valeur = int(n[0])
f=[]
for idx in range(0,nbre_valeur):
    f.append(float(n[1+idx]))
#print(f)

somme =0

for k in range (0, len(f)-1):  # On calcul la différence entre chaque harmonique (donc les fondamentales) et on fait une moyenne
    diff = abs(f[k]-f[k+1])
    somme = somme + diff
fsax=somme/len(f);
print("la fondamentale du saxo est:" ,fsax)


