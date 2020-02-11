import matplotlib.pyplot as plt
import numpy as np
import os

def read_binary(fileName):
    data = np.fromfile(fileName, dtype='>f4', sep="")

    return data

if __name__ == '__main__':

    _dataDir = "../../data/2d/"
    seismicDir = "tpd"
    name = "tp73.dat"
    fileName = os.path.join(_dataDir, seismicDir, name)
    data = read_binary(fileName)

    n = 357
    plt.imshow(np.reshape(data, (n, -1)).T); plt.show()


