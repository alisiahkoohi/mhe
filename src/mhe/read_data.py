import matplotlib.pyplot as plt
import numpy as np
import os

def my_read(fileName):
    data = np.fromfile(fileName, dtype='>f4', sep="")

    return data

if __name__ == '__main__':

    _dataDir = "../../data/2d/"
    seismicDir = "tpd"
    name = "tp73.dat"
    fileName = os.path.join(_dataDir, seismicDir, name)

    data = my_read(fileName)

    n1,n2 = 240, 357
    plt.imshow(np.reshape(data, (n2, -1)).T);plt.show()


