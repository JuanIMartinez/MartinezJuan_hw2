import numpy as np
import matplotlib.pylab as plt

tiempo=np.genfromtxt("data_posiciones.dat",usecols=(0))
U1=np.genfromtxt("data_posiciones.dat",usecols=(1))
U2=np.genfromtxt("data_posiciones.dat",usecols=(2))
U3=np.genfromtxt("data_posiciones.dat",usecols=(3))


plt.figure()
plt.plot(tiempo,U1, c="royalblue", label="primer piso", linewidth=0.7)
plt.plot(tiempo,U2, c="lawngreen", label="segundo piso", linewidth=0.7)
plt.plot(tiempo,U3, c="tomato", label="tercer piso", linewidth=0.7)
plt.xlabel("tiempo")
plt.ylabel("desplazamiento horizontal")
plt.title("Desplazamiento hotizontal vs. Tiempo")
plt.legend()
plt.grid()
plt.savefig("Desplazamiento.pdf")
plt.close()

omegas=np.genfromtxt("maximo_movimiento.dat",usecols=(0))
U1_max=np.genfromtxt("maximo_movimiento.dat",usecols=(1))
U2_max=np.genfromtxt("maximo_movimiento.dat",usecols=(2))
U3_max=np.genfromtxt("maximo_movimiento.dat",usecols=(3))


plt.figure()
plt.plot(omegas,U1_max, c="cyan", label="primer piso", marker="^")
plt.plot(omegas,U2_max, c="magenta", label="segundo piso", marker="d")
plt.plot(omegas,U3_max, c="c", label="tercer piso", marker=".")
plt.xlabel("Omegas")
plt.ylabel("desplazamiento horizontal")
plt.title("Max. Desplazamiento hotizontal vs. omegas")
plt.legend()
plt.grid()
plt.savefig("Desplazamiento_omegas.pdf")
plt.close()
