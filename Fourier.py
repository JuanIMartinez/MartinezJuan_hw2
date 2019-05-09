# Ejercicio 2: Transformada de fourier 

import numpy as np
import matplotlib.pylab as plt

### se almacenan los datos de signal.dat y signalSuma.dat.

##signal.dat
tiempo=np.genfromtxt("signal.dat",usecols=(0))
dt=(tiempo[-1]-tiempo[0])/len(tiempo)



signal=np.genfromtxt("signal.dat",usecols=(1))



##signalSuma.dat

tiempo_suma=np.genfromtxt("signalSuma.dat",usecols=(0))
dt_suma=(tiempo_suma[-1]-tiempo_suma[0])/len(tiempo_suma)

signal_suma=np.genfromtxt("signalSuma.dat",usecols=(1))



## se grafican las señales de signal.dat y signalSuma.dat.


plt.figure()
plt.subplot(2,1,1)
plt.title('SignalSuma y Signal')
plt.plot(tiempo_suma,signal_suma,c="lightsalmon",label = "SignalSuma", linewidth=0.7)
plt.ylabel("SignalSuma")
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(tiempo,signal,c="c",label = "Signal", linewidth=0.7)
plt.ylabel("Signal")
plt.xlabel("Tiempo")
plt.grid()
plt.legend()
plt.savefig("signals.pdf")
plt.close()


##implementacion de la transformada discreta de Fourier.

def transformada_fourier(data):
    fourier=np.empty(0)
    for i in range(len(data)):
        factor=0
        for j in range(len(data)):
            factor=factor+data[j]*np.exp(-2*np.pi/len(data)*j*i*1j)
            incluir=abs(factor)/len(data)
        fourier=np.append(fourier,incluir)
    return fourier

       
## Transformada de Fourier de signal y signalSuma con implementacion Propia

fourier_signal=transformada_fourier(signal)
fourier_signalSuma=transformada_fourier(signal_suma)

##Transformada de Fourier de signal y signalSuma 


len_signal=len(signal)
fftfreq_signal_plot=dt/len(signal)*np.linspace(0,len(signal),len(signal)) ##IMPLEMENTACION QUE REEMPLAZA FFTFREQ



len_signalSuma=len(signal_suma)
fftfreq_signalSuma_plot=dt/len(signal_suma)*np.linspace(0,len(signal_suma),len(signal_suma)) ##IMPLEMENTACION QUE REEMPLAZA FFTFREQ



plt.figure()
plt.subplot(2,1,1)
plt.title('Transformada Fourier de SignalSuma y Signal')
plt.plot(fftfreq_signalSuma_plot,fourier_signalSuma,c="skyblue",label = "T. SignalSuma", linewidth=0.7)
plt.ylabel("T. SignalSuma")
plt.grid()
plt.legend()
plt.subplot(2,1,2)
plt.plot(fftfreq_signal_plot,fourier_signal,c="tomato",label = "T. Signal", linewidth=0.7)
plt.ylabel("T. Signal")
plt.xlabel("Frecuencia")
plt.grid()
plt.legend()
plt.savefig("TransformadasFourier.pdf")
plt.close()


##espectogramas

plt.figure()
plt.subplot(2,1,1)
plt.title('Transformada Fourier de SignalSuma y Signal')
plt.specgram(signal_suma, NFFT=256*2, Fs=dt_suma)
plt.colorbar()
plt.grid()
plt.subplot(2,1,2)
plt.specgram(signal, NFFT=256*2, Fs=dt)
plt.colorbar()
plt.grid()
plt.savefig("Espectograma.pdf")
plt.close()

print("SE UTILIZO UNA IMPLEMENTACION PROPIA PARA REEMPLAZAR FFTFREQ")


#####se almacena temblor.txt y se grafica

temblor=np.genfromtxt("temblor.txt")[4:]
dt_temblor=1/100
tiempo_temblor=np.linspace(0,len(temblor)/dt,len(temblor))


plt.figure()
plt.plot(tiempo_temblor,temblor, c="springgreen", label="signal Temblor", linewidth=0.7)
plt.xlabel("tiempo [s]")
plt.ylabel("signal")
plt.title("Signal Temblor")
plt.legend()
plt.grid()
plt.savefig("SignalTemblor.pdf")
plt.close()

## transformada 

fourier_temblor = abs( np.fft.fft(temblor))
cantidad_datos_temblor=len(temblor)
fftfreq=np.fft.fftfreq(cantidad_datos_temblor,dt_temblor)
fftfreq_plot_temblor=abs(fftfreq)

plt.figure()
plt.plot(fftfreq_plot_temblor,fourier_temblor, c="orange", label="T. signal Temblor", linewidth=0.7)
plt.xlabel("frecuencia (1/s)")
plt.ylabel("T. Signal Temblor")
plt.title("Transformada de Fourier Signal Temblor")
plt.grid()
plt.legend()
plt.savefig("Fourier_temblor.pdf")
plt.close()

##espectrograma de Temblor.txt

plt.figure()
plt.title('Transformada Fourier de SignalSuma y Signal')
plt.specgram(temblor, NFFT=256, Fs=dt_temblor)
plt.colorbar()
plt.grid()
plt.savefig("Espectograma_temblor.pdf")
plt.close()
