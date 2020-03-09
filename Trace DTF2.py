# Projet de POO : Shazam_Instrument
# Teboul pavel, Mariolan Cathie
# 03/03/2020

#1. Tracé TF du signal 
#2. Calcul et affichage du nombre d'échantillon, de la fréquence d'échantillonnage et des harmoniques


import numpy as np
import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt
fichier=open("piano.txt","w")

#calcul et affichage du nombre d'échantillon et de la fréquence d'échantillonnage

son , Fe = sf.read(r"H:\Poo lien utiles\Base_de_donnees\piano\Piano.pp.E1.aiff")
N = son.shape[0]
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
for idx,o in enumerate(mod_S[0:N//2]):
	if  np.abs(o)> 10  and np.abs(o).real>mod_S[idx-1] and np.abs(o).real>mod_S[idx+1]:
		p.append(idx)
ind_max = p[0]

#Calcul et affichages de max correspondant aux valeurs des harmoniques
for k in range (1,len(p)-1):
    if (p[k]-ind_max)*Fe/N<3:
        if mod_S[ind_max]<mod_S[p[k+1]]:
           ind_max = p[k+1]
    else:
        if ind_max*Fe/N >32.7: #selection des 
            r.append(ind_max)
        ind_max = p[k]
r.append(ind_max)
fichier.write(str(len(r)))
fichier.write("\t")
for x in r:
    fichier.write(str(x*Fe/N))
    fichier.write("\t")
    print(x*Fe/N); 
fichier.close()




plt.title('Module de la T.F.D. (harmoniques)')
#plt.legend()
plt.grid(True)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude (u.a.)')
# Tracer de la phase du spectre du signal temporel
#plt.figure(3)
#plt.plot(np.fft.fftshift(freq),np.fft.fftshift(np.angle(S).real), label="Voie 0")
#plt.title('Module de la T.F.D.')
#plt.legend()
#plt.grid(True)
#plt.xlabel('Fréquence (Hz)')
#plt.ylabel('Phase (rd)')
plt.show()  