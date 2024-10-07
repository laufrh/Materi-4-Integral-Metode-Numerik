# -*- coding: utf-8 -*-
"""Materi-1-Integral-Metode-Numerik-Syafrudin Fahrul Anas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zyd8ZtW67bOW2pHa4wSMwbHwKbPASbBK
"""



# Mengimport Library
import numpy as np
import matplotlib.pyplot as plt

# Fungsi yang akan diintegralkan
def func(x):
    return (x**(-3)) + np.cos(x)

# Batas Integrasi
a = 1.0  # Batas bawah
b = 5.0 # Batas atas
n = 10   # Jumlah grid

# --------- Metode Trapezoid ---------
dx = (b-a)/(n-1)
x = np.linspace(a,b,n)

sigma = 0
for i in range(1, n-1):
    sigma += func(x[i])

hasil = 0.5*dx*(func(x[0])+2*sigma+func(x[-1]))

print(hasil)

xp = np.linspace(a, b, 1000)
plt.plot(xp, func(xp), label="Fungsi (x**(-3) + np.cos(x))")
plt.show()

xp =np.linspace(a, b, 1000)
plt.plot(xp,func(xp))

for i in range (n):
    plt.bar(x[i], func(x[i]), align='edge', width=0.000001, edgecolor='red')

plt.show()

xp =np.linspace(a, b, 1000)
plt.plot(xp,func(xp))

for i in range (n):
    plt.bar(x[i], func(x[i]), align='edge', width=0.000001, edgecolor='red')

plt.fill_between(x, func(x), color='yellow', alpha=0.5)
plt.show()

# --------- Metode Simpson ---------
# Jika n genap, tambah 1 agar menjadi ganjil
if n % 2 == 0:
    n += 1 #Jika n genap, tambah 1 agar menjadi ganjil

x = np.linspace(a, b, n)
dx = (x[-1] - x[0]) / (n - 1)

# Menghitung integral menggunakanmetode simpson
hasil = func(x[0]) + func(x[-1]) # Tambah f(a) dan f(b)

for i in range(1, n-1, 2):
    hasil += 4 * func(x[i]) # Untuk Indeks ganjil

for i in range(2, n-2, 2):
    hasil += 2 * func(x[i]) # Untuk Indeks genap

hasil *= dx / 3 # Fahtor dx/3

# Visualisasi grafik dan bar
xp = np.linspace(a, b, 1000)
plt.plot(xp, func(xp))

for i in range(n):
    plt.bar(x[i], func(x[i]), align='edge', width=dx,color='red', edgecolor='black')

plt.show()
print(hasil)

