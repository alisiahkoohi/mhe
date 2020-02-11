import pickle
import numpy as np
import matplotlib.pyplot as plt

ffile = "myfile_0"

with open(ffile + ".txt", "rb") as fp:
	horizons = pickle.load(fp)
horizons = np.array(horizons).reshape([6, -1])

plt.figure(dpi=150, figsize=(3, 7))
for j in range(6):
	plt.plot(-horizons[j, :], color="k")
plt.show()

# from IPython import embed; embed()