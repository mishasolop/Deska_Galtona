# Program na zaliczenie ćwiczeń z fizyki pod nazwą Deska Galtona
# by Mykhailo Solop
# Program wykorzystuje bibliotekę Matplotlib do zailustrowania działania Deski Galtona
# i bibliotekę NumPY do wszelkich obliczeń.
#v 0.1 25.12.20

import matplotlib.pyplot as plt

import random

import math

import numpy as np

import pylab

fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False, figsize=(20, 8))

pylab.rc('font', family='sans', size=20)

pylab.rc('axes', linewidth=1.5)

plt.rcParams['xtick.major.width'] = 3

plt.rcParams['xtick.minor.width'] = 3

plt.rcParams['ytick.major.width'] = 3

plt.rcParams['ytick.minor.width'] = 3

plt.rcParams['figure.facecolor'] = 'white'

ax1 = axes[0]

ax2 = axes[1]


# funkcja do policzenia prawdopodobieństwa

def probs(N, x):  # x must be x = -N, -N + 2, -N + 4, ... , N - 4, N - 2, N

    top = math.factorial(abs(N)) * 2 ** (-N)

    bottom = math.factorial(abs(N - x) / 2) * math.factorial(abs(x + N) / 2)

    P = top / bottom

    return P


N = 12  # liczba "schodków"

n = 100000  # liczba kulek

p = 0.5  # prawdopodobieństwo, że kulka poleci w lewo

q = abs(1 - p)  # prawdopodobieństwo, że kulka poleci w prawo

if p + q > 1.0:
    print("ERROR: p + q ma być 1.0.")

x = np.zeros(n)

# główna pętla

for i in range(n):

    start1 = 0

    for j in range(N):

        rand = random.uniform(0.0, 1.0)

        if 0 < rand < p:

            start1 = start1 - 1  # przesuń się w lewo

        elif p < rand < 1.0:

            start1 = start1 + 1  # przesuń się w prawo

    x[i] = start1

w = 1

n_bins = math.ceil((2.0 * N + 1) / w)

histContents = ax1.hist(x, bins=n_bins)

totalContents = 0

for k in range(n_bins):
    totalContents = totalContents + histContents[0][k]

probys = histContents[0] / totalContents

print("simulated probabilities: ", probys)

probyslist = []

probysExact = []

i = 0

while i < len(probys):

    if probys[i] != 0.0: probyslist.append(probys[i])

    i = i + 1

i = -N

while i <= N:
    probysExact.append(probs(N, i))

    i = i + 2

probys = np.array(probyslist)

print("Zasymulowane prawdopodobieństwa: ", probys)

probysExact = np.array(probysExact)

print("Dokładne prawdopodobieństwa: ", probysExact)

residual = abs(probys - probysExact)

print("Counts: ", histContents[0])

print("prawdopodobieństwo znalezienia kulki w {} z {} próbami:".format(-N, N), probs(N, 0))

Xrange = np.linspace(1, len(probys), num=len(probys))

ax2.plot(Xrange, probys, 'ro', label="Zasymulowane prawdopodobieństwa")

ax2.plot(Xrange, probysExact, 'bo', label="Dokładne prawdopodobieństwa")

ax2.plot(Xrange, residual, 'go', label="Różnica")

ax2.set_ylabel("Prawdopodobieństwo znalezienia kulki w koszu")

ax2.legend()

ax1.set_xlabel("pozycja")

ax1.set_ylabel("liczby")

ax1.set_title("Deska Galtona")

plt.show()
