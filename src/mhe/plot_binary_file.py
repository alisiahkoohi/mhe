import matplotlib.pyplot as plt
import numpy as np
import os
import glob

def read_binary(fileName):
    data = np.fromfile(fileName, dtype='>f4', sep="")

    return data

if __name__ == '__main__':

    for file in glob.glob("samples/*dm.dat"):
        data = read_binary(file)
        n = 401
        plt.plot(np.reshape(data, (n, -1)).T[:, 50])
        plt.figure()
        plt.plot(np.diff(np.reshape(data, (n, -1)).T[:, 50]))
        plt.figure()
        plt.imshow(np.reshape(data, (n, -1)).T); plt.show()
        break


