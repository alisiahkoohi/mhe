import matplotlib.pyplot as plt
import numpy as np
import os

def my_read(fileName, n1, n2):
    data = np.fromfile(fileName,
                dtype='>f4', sep="")

    return data

if __name__ == '__main__':

    _dataDir = "../../data/2d/"
    seismicDir = "tpd"
    name = "tp73.dat"
    fileName = os.path.join(_dataDir, seismicDir, name)

    n1,n2 = 240, 357
    data = my_read(fileName, n1, n2)
    plt.imshow(np.reshape(data, (357, -1)).T);plt.show()


