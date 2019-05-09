# Ejercicio 2: Transformada de fourier 

import numpy as np
import matplotlib.pylab as plt

### se almacenan los datos de signal.dat y signalSuma.dat.

##signal.dat
tiempo=np.genfromtxt("signal.dat",usecols=(0))
dt=(tiempo[-1]-tiempo[0])/len(tiempo)



signal=np.genfromtxt("signal.dat",usecols=(1))
len_sigma=len(signal)


##signalSuma.dat

tiempo_suma=np.genfromtxt("signalSuma.dat",usecols=(0))
dt_suma=(tiempo_suma[-1]-tiempo_suma[0])/len(tiempo_suma)

signal_suma=np.genfromtxt("signalSuma.dat",usecols=(1))
len_sigmaSuma=len(signal_suma)


## se grafican las señales de signal.dat y signalSuma.dat.


plt.figure()
plt.subplot(2,1,1)
plt.title('SignalSuma y Signal')
plt.plot(tiempo_suma,signal_suma,c="lightsalmon",label = "SignalSuma")
plt.ylabel("SignalSuma")
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(tiempo,signal,c="c",label = "Signal")
plt.ylabel("Signal")
plt.xlabel("Tiempo")
plt.grid()
plt.legend()
plt.savefig("signals.pdf")
plt.close()


##implementacion de la transformada discreta de Fourier.

def transformada_fourier(data):
    fourier=[]
    for i in range(len(data)):
        factor=0
        for j in range(len(data)):
               factor=factor+(np.cos(-2*np.pi*j/len(data))+1j*np.sin(-2*np.pi*j/len(data)))*data[i]
        fourier.append(factor)
        
## Transformada de Fourier de signal y signalSuma con implementacion Propia

fourier_signal_propia=transformada_fourier(signal)
fourier_signalSuma_propia=transformada_fourier(signal_suma)

##Transformada de Fourier de signal y signalSuma 

fourier_signal = np.fft.fft(signal)
len_signal=len(signal)
fftfreq_signal=np.fft.fftfreq(len_signal,dt)
fftfreq_signal_plot=np.abs(fftfreq_signal)


fourier_signalSuma = np.fft.fft(signal_suma)
len_signalSuma=len(signal_suma)
fftfreq_signalSuma=np.fft.fftfreq(len_signalSuma,dt_suma)
fftfreq_signalSuma_plot=np.abs(fftfreq_signalSuma)



plt.figure()
plt.subplot(2,1,1)
plt.title('Transformada Fourier de SignalSuma y Signal')
plt.plot(fftfreq_signalSuma_plot,fourier_signalSuma,c="skyblue",label = "T. SignalSuma")
plt.ylabel("T. SignalSuma")
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(fftfreq_signal_plot,fourier_signal,c="tomato",label = "T. Signal")
plt.ylabel("T. Signal")
plt.xlabel("Frecuencia")
plt.grid()
plt.legend()
plt.savefig("TransformadasFourier.pdf")
plt.close()


##espectogramas

plt.figure()
plt.subplot(1,2,1)
plt.title('Transformada Fourier de SignalSuma y Signal')
plt.specgram(signal_suma, NFFT=256*2, Fs=0.3)
plt.grid()
plt.subplot(1,2,2)
plt.specgram(signal, NFFT=256*2, Fs=0.3)
plt.grid()
plt.savefig("Espectograma.pdf")
plt.close()
