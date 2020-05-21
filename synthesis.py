#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.signal
import scipy.io.wavfile
import sys

_, inp = sys.argv

rate, rawdata = scipy.io.wavfile.read(inp, mmap=True)
print(rate, rawdata.shape)

#data = np.asarray([left for left,right in rawdata])
data=rawdata
print(data.shape)

freqs, wtimes, spectro = scipy.signal.spectrogram(data)

#print(freqs, len(freqs))
print(len(freqs))
#print(wtimes)
#print(spectro)
print(len(spectro), len(spectro[0]))

for i,f in enumerate(freqs):
    print(i,f)

plt.imshow(spectro, cmap='hot', interpolation='nearest')
plt.show()
