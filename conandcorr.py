import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,2,2]);
h=np.array([3,2,5]);
N= len(x) + len(h) - 1;


y=np.zeros(N);

for n in range(N):
    for k in range(len(x)):
        if n-k>=0 and n-k< len(h):
            y[n]+=x[k]*h[n-k]
            

con=np.convolve(x,h);

print(con);
n=np.arange(N);
plt.subplot(1,2,1);
plt.stem(n,con);

plt.subplot(1,2,2);
plt.stem(n,y);

# correlation


a = np.array([1, 2, 2])
b = np.array([3, 2, 5])

con=np.convolve(a,h);
corre=np.correlate(a,b,mode='full');

print(con);
print(corre);

n=np.arange(len(corre))

plt.subplot(1,2,1);
plt.stem(n,corre);

plt.subplot(1,2,2);
plt.stem(n,con);

# manual conv
import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3])
h = np.array([0, 1, 0.5])


N = len(x) + len(h) - 1

y = np.zeros(N)

# Manual convolution
for n in range(N):
    for k in range(len(x)):
        if n - k >= 0 and n - k < len(h):
            y[n] += x[k] * h[n - k]


print("x[n]:", x)
print("h[n]:", h)
print("Convolution y[n]:", y)


plt.subplot(3,1,3)
n_out = np.arange(N)
plt.stem(n_out, y)
plt.title("Manual Convolution")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.subplot(3,1,1)
plt.stem(h)
plt.title("original signal h(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.subplot(3,1,2)
plt.stem(x)
plt.title("original signal x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()


# manual corre

x = np.array([1, 2, 3])
y_vec = np.array([0, 1, 0.5])


N_corr = len(x) + len(y_vec) - 1

r = np.zeros(N_corr)


for n in range(-len(y_vec)+1, len(x)):
    sum_val = 0
    for k in range(len(x)):
        if 0 <= k + n < len(y_vec):
            sum_val += x[k] * y_vec[k + n]
    r[n + len(y_vec) - 1] = sum_val  


print("Cross-Correlation r_xy[n]:", r)


plt.subplot(3,1,1)
n_corr = np.arange(-len(y_vec)+1, len(x))
plt.stem(n_corr, r)
plt.title("Manual Cross-Correlation")
plt.xlabel("n (lag)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.subplot(3,1,2)
plt.stem(h)
plt.title("original signal h(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.subplot(3,1,3)
plt.stem(x)
plt.title("original signal x(n)")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
