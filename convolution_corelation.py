# find the convolution between two vectors in python without using inbuilt convolution librabry
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [-1,-2,-3,-4,-5]

h = [-5,-4,-3,-2,-1]

len_x = len(x)
len_y = len(y)

len_z = (len_x + len_y - 1)
z = [0]*len_z
Cxy = [0]*len_z

for n in range(len_z):
    total = 0
    for k in range(len_x):
        j = n-k
        if 0 <= j < len_y:
            total += x[k]*y[j]
    z[n] = total

for n in range(len_z):
    total = 0
    for k in range(len_x):
        j = n-k
        if 0 <= j < len_y:
            total += x[k]*h[j]
    Cxy[n] = total

print("Convolution is: ", z)
print("Co-relation is: ", Cxy)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.stem(range(len_z), z)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("Amplitude")
plt.title("Convolution")


plt.subplot(1,2,2)
plt.stem(range(len_z), Cxy)
plt.grid(True)
plt.xlabel("index")
plt.ylabel("Amplitude")
plt.title("Co-relation")

plt.tight_layout()
plt.show()

        