import pickle
import numpy as np
import matplotlib.pyplot as plt

ffile = "tp73"

with open(ffile + ".txt", "rb") as fp:
	horizons = pickle.load(fp)
horizons = np.array(horizons).reshape([15, -1])

plt.figure(dpi=150, figsize=(3, 7))
for j in range(15):
	plt.plot(-horizons[j, :], color="k")
plt.show()

# from IPython import embed; embed()