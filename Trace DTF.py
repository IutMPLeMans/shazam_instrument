#fichier obsolète de calcul de TF

import numpy as np
import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt

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
freq = np.fft.fftfreq(N)*Fe
plt.plot(np.fft.fftshift(freq),np.fft.fftshift(np.abs(S).real))#,label="Voie 0")
for idx,o in enumerate(S[1:N//2]):
	if np.abs(o).real>np.abs(S[idx-1]).real and np.abs(o).real>np.abs(S[idx+1]).real:
		print(idx*Fe/N)
	
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
