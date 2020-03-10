# Projet de POO : Shazam_Instrument
# Teboul pavel, Mariolan Cathie
# 03/03/2020

#1. Tracé TF du signal 
#2. Calcul et affichage du nombre d'échantillon, de la fréquence d'échantillonnage et des harmoniques


import numpy as np
import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt

nom=[r"C:\Users\s177090\source\repos\IutMPLeMans\shazam_instrument\Base_de_donnees\Marimba\Marimba.yarn.ff.Db2.stereo.aif",
     r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\Base_de_donnees\piano\Piano.pp.E1.aiff",
     r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\Base_de_donnees\saxo\SopSax.vib.ff.Ab3.stereo.aif",
     r"C:\Users\s177090\Source\Repos\IutMPLeMans\shazam_instrument\Base_de_donnees\Basson\Bassoon.pp.Bb1B1.aiff"]

inst=["marimba",
      "piano",
      "saxo",
      "basson"]
for n,inst in zip(nom,inst):
    

    fichier=open(inst,"w")

    #calcul et affichage du nombre d'échantillon et de la fréquence d'échantillonnage

    son , Fe = sf.read(n)
    N = son.shape[0]
    print(inst)
    print("Nombre d'échantillons : ", N)
    print("Fréquence d'échantillonnage : ", Fe)
    if son.ndim==1:
        S = np.fft.fft(son)
    else:
        S = np.fft.fft(son[:, 0])
    # Tracer du signal temporel
    #te = np.arange(0,N)/Fe
    #plt.figure(1)
    #plt.plot(te,son,label='Voie 0')
    #plt.title('Signal la.wav')
    #plt.legend()
    #plt.grid(True)
    #plt.xlabel('Temps (s)')
    #plt.ylabel('Amplitude (u.a.)')
    #plt.pause(0.1)
    # Tracer du module du spectre de la TFD du signal temporel
    plt.figure(2)
    p=[];
    r=[];
    freq = np.fft.fftfreq(N)*Fe
    plt.plot(np.fft.fftshift(freq),np.fft.fftshift(np.abs(S).real))#,label="Voie 0")
    mod_S = np.abs(S).real
    h_max = np.max(mod_S[2:N//2])
    for idx,o in enumerate(mod_S[0:N//2]):
	    if  np.abs(o)> h_max/10  and np.abs(o)>mod_S[idx-1] and np.abs(o).real>mod_S[idx+1]: #on sélectionne les harmonique qui ont une amplitude supérieur à 10% de lamplitude max pour pas prendre les petits trucs
		    p.append(idx)
    ind_max = p[0]

    #Calcul et affichages de max correspondant aux valeurs des harmoniques
    for k in range (1,len(p)):
        if (p[k]-ind_max)*Fe/N<3:
            if k+1<len(p) and mod_S[ind_max]<mod_S[p[k+1]]:
               ind_max = p[k+1]
        else:
            if ind_max*Fe/N >32.7: #selection des valeur des harmoniques supérieurs à 32.7Hz (première note de l'octave 0 (cf wikipédia))
                r.append(ind_max)
            ind_max = p[k]
    r.append(ind_max)
    fichier.write(str(len(r))) #écriture dans un le fichier, première valeur : taille de r nombre de valeur d'harmonique calculées 
    fichier.write("\t")
    for x in r:
        fichier.write(str(mod_S[x]/h_max))   #normalise et ecrit dans le fichier l'amplitude avec en valeur max 1
        fichier.write("\t")
        fichier.write(str(x/(r[0])))     #normalise et ecrit dans le fichier l'absciesse en prenant la premiere harmonique en fondamentale !!!!!!!!!!!!!!!! Erreur qu'il faudra corriger plus tard peut etre
        fichier.write("\t")
        print(x/(r[0])); 
    fichier.close()


    #plt.title('Module de la T.F.D. (harmoniques)')
    #plt.legend()
    #plt.grid(True)
    #plt.xlabel('Fréquence (Hz)')
    #plt.ylabel('Amplitude (u.a.)')
    # Tracer de la phase du spectre du signal temporel
    #plt.figure(3)
    #plt.plot(np.fft.fftshift(freq),np.fft.fftshift(np.angle(S).real), label="Voie 0")
    #plt.title('Module de la T.F.D.')
    #plt.legend()
    #plt.grid(True)
    #plt.xlabel('Fréquence (Hz)')
    #plt.ylabel('Phase (rd)')
    #plt.show()  


    #Commentaire du 09/03/2020
    #Amélioration du code pour avoir un seuil : 10%de la hauteur du plus grand pic (pour pas avoir les trop petites harmoniques)
    #seuil aussi pour pas avoir les fréquence inférieur à 32.7Hz (première note de l'octave 0) lien wikipédia : https://fr.wikipedia.org/wiki/Note_de_musique
    #Récupération des valeurs des harmoniques dans un fichier  /!\ ligne 13 du fichier en haut !
    #