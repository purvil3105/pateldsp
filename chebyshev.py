import numpy as np 
import matplotlib.pyplot as plt 
from scipy import signal 

Fs = 2000
fp =200
fs = 100
rp = 1
rs = 40

wp = fp/(Fs/2)
ws = fs/(Fs/2)

N, wn = signal.cheb1ord(ws,wp,rp,rs , analog=False)
print("Order of the filter N =", N)

b,a = signal.cheby1(N , rp ,wn , btype='high' , analog =False)

w,h = signal.freqz(b,a , worN =1024)
plt.figure(figsize=(10, 5))
plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Chebyshev Type-1 High Pass Filter Response")
plt.xlabel("Normalized Frequency (×π rad/sample)")
plt.ylabel("Magnitude (dB)")
plt.grid(True)
plt.show()


# Order and cutoff
N, Wn = signal.cheb1ord(Wp, Ws, Rp, Rs, analog=False)

# Design Low Pass Chebyshev-I filter
b, a = signal.cheby1(N, Rp, Wn, btype='low', analog=False)

w, h = signal.freqz(b, a, worN=1024)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Chebyshev Type-1 Low Pass Filter")
plt.grid(True)
plt.show()


N, Wn = signal.buttord(Wp, Ws, Rp, Rs)

b, a = signal.butter(N, Wn, btype='high')

w, h = signal.freqz(b, a, worN=1024)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Butterworth High Pass Filter")
plt.grid(True)
plt.show()


N, Wn = signal.cheb2ord(Wp, Ws, Rp, Rs)

b, a = signal.cheby2(N, Rs, Wn, btype='high')

w, h = signal.freqz(b, a, worN=1024)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Chebyshev Type-2 High Pass Filter")
plt.grid(True)
plt.show()


N, Wn = signal.ellipord(Wp, Ws, Rp, Rs)

b, a = signal.ellip(N, Rp, Rs, Wn, btype='high')

w, h = signal.freqz(b, a, worN=1024)

plt.plot(w/np.pi, 20*np.log10(abs(h)))
plt.title("Elliptic High Pass Filter")
plt.grid(True)
plt.show()

