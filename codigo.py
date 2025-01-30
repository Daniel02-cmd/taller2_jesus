import numpy as np

mu = 3
sigma = 0.5 
n=1000
vals = np.random.normal(loc=mu, scale=sigma, size=n)
print(vals)
vals.shape

vals1 = np.random.chisquare(df=3)
vals1.shape