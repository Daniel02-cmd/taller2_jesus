import numpy as np

mu = 3
sigma = 0.5 
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)
vals.shape

vals1 = np.random.chisquare(df=3)
vals1.shape

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=vals1, bins=30)
plt.title('Histograma de valores generados')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
plt.show()

print(bins)
print(count)