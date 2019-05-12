Resultados_hw2.pdf : Resultados_hw2.tex signals.pdf TransformadasFourier.pdf Espectrograma.pdf SignalTemblor.pdf Fourier_temblor.pdf Espectrograma_temblor.pdf Desplazamiento.pdf Desplazamiento1.pdf Desplazamiento2.pdf Desplazamiento_omegas.pdf resonancia.pdf 
	pdflatex Resultados_hw2.tex
signals.pdf: Fourier.py
	python Fourier.py
TransformadasFourier.pdf: Fourier.py
	python Fourier.py
Espectrograma.pdf: Fourier.py
	python Fourier.py
SignalTemblor.pdf: Fourier.py
	python Fourier.py
Fourier_temblor.pdf: Fourier.py
	python Fourier.py
Espectrograma_temblor.pdf: Fourier.py
	python Fourier.py
Desplazamiento.pdf: Graficas_edificio.py data_posiciones.dat
	python Graficas_edificio.py
data_posiciones.dat: a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
Desplazamiento1.pdf: Graficas_edificio.py data_posiciones1.dat
	python Graficas_edificio.py
data_posiciones1.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
Desplazamiento2.pdf: Graficas_edificio.py data_posiciones2.dat
	python Graficas_edificio.py
data_posiciones2.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
Desplazamiento_omegas.pdf: Graficas_edificio.py maximo_movimiento.dat
	python Graficas_edificio.py
maximo_movimiento.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
resonancia.pdf: Graficas_edificio.py data_posiciones_07.dat data_posiciones_35.dat data_posiciones.dat
	python Graficas_edificio.py
data_posiciones_35.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
data_posiciones_07.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
data_posiciones.dat : a.out
	./a.out
a.out : Edificio.cpp
	g++ Edificio.cpp
    
