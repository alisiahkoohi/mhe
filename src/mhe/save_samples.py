import matplotlib.pyplot as plt
import numpy as np
import torch
from load_vel import judi_model
import os

def load(checkpoint_dir='./'):

    log_to_load = os.path.join(checkpoint_dir, 'training-logs.pt')
    assert os.path.isfile(log_to_load)
    training_logs = torch.load(log_to_load, map_location='cpu')

    samples = training_logs['samples']
    return samples

def my_save(arr, filename):
    arr = arr
    arr = arr.astype('>f4')
    arr.tofile(filename, sep="")

def model_topMute(image, mute_end=20, length=1):

    mute_start = mute_end - length
    damp = np.zeros([image.shape[0]])
    damp[0:mute_start-1] = 0.
    damp[mute_end:] = 1.
    taper_length = mute_end - mute_start + 1
    taper = (1. + np.sin((np.pi/2.0*np.array(range(0,taper_length-1)))/(taper_length - 1)))/2.
    damp[mute_start:mute_end] = taper
    for j in range(0, image.shape[1]):
        image[:,j] = image[:,j]*damp
    return image

if __name__ == '__main__':

    burn_in_index = 52
    m0, m, dm, spacing, shape, origin = judi_model()

    samples = load()

    samples = np.array(samples)[burn_in_index:, :, :]
    samples = np.transpose(samples.reshape((-1, dm.shape[2], dm.shape[3])), 
        (0, 2, 1))
    for j in range(samples.shape[0]):
        samples[j, :, :] = model_topMute(samples[j, :, :])
    samples = np.transpose(samples, (0, 2, 1))
    samples_mean = np.mean(samples[burn_in_index:, :, :], axis=0)

    if not os.path.exists('samples'):
        os.makedirs('samples')

    for j in range(samples.shape[0]):
        my_save(samples[j, ...].reshape(-1), os.path.join('samples', 'myfile_' + str(j) + '.dat'))

    my_save(dm.numpy().reshape(-1), os.path.join('samples', 'dm.dat'))
    my_save(samples_mean.reshape(-1), os.path.join('samples', 'samples_mean.dat'))