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
