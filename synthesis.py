#! /usr/bin/env python3

import matplotlib.pyplot as plt
import math
import numpy as np
import scipy
import scipy.signal
import scipy.io.wavfile
import sys

_, inp,outp = sys.argv

rate, rawdata = scipy.io.wavfile.read(inp, mmap=True)
print(rate, rawdata.shape)

#data = np.asarray([left for left,right in rawdata])
data=rawdata
print(data.shape)

freqs, wtimes, spectro = scipy.signal.spectrogram(data)

#print(freqs, len(freqs))
print(len(freqs))
print(wtimes)
#print(spectro)
print(len(spectro), len(spectro[0]))

for i,f in enumerate(freqs):
    print(i,f)

def synthesize_block(width, frequencies, amplitudes):
    samples=[]
    for t in range(width):
        sample = 0
        for f,amp in zip(frequencies, amplitudes):
            component = math.sin(t*f)*amp
            sample += component
        samples.append(sample)
    return samples

blocks = []
for blockid, amplitudes in enumerate(np.transpose(spectro)):
    blocks.append(synthesize_block(128, freqs, amplitudes))
    print('synthesized block', blockid)
samples = sum(blocks, [])
samples = np.asarray(samples)

scipy.io.wavfile.write(outp, rate, samples)
