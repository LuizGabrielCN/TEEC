import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import rfft, rfftfreq 
from scipy.signal import butter, lfilter, freqz, filtfilt

plt.close('all')

#Parâmetros
timesignal = 1 #Tempo dos sinais.
freqnc = 10000 #Frequência de amostragem.

#Função para gerar sinais senoidais.
def gerar_sinal_senoidal (freq, taxa_amostragem, duracao):
    t = np.linspace(0.0001, duracao, taxa_amostragem*duracao, endpoint=False)
    f = t*freq
    y = np.sin((2*np.pi)*f) #Obtendo o sinal.
    return t, y

#Geração dos Sinais.
t1, a = gerar_sinal_senoidal(60, freqnc, timesignal)
t2, b = gerar_sinal_senoidal(180, freqnc, timesignal)
t3, c = gerar_sinal_senoidal (300, freqnc, timesignal)
t4, d = gerar_sinal_senoidal (420, freqnc, timesignal)

#Soma dos sinais gerados.
y = 1*a + 0.5*b + 0.25*c + 0.10*d

plt.xlabel("Tempo em segundos")
plt.ylabel("Amplitude da Onda")
plt.plot(t1, a)
plt.show()
plt.savefig('a.png')
plt.plot(t2, b)
plt.show()
plt.savefig('b.png')
plt.plot(t3, c)
plt.show()
plt.savefig('c.png')
plt.plot(t4, d)
plt.show()
plt.savefig('d.png')

fy = scipy.fft.fft(y)
