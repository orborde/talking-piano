#! /usr/bin/env python3

import argparse
import matplotlib.pyplot as plt
import math
from pathlib import Path
import numpy as np
import scipy
import scipy.signal
import scipy.io.wavfile

parser = argparse.ArgumentParser()
parser.add_argument("inp", type=Path)
parser.add_argument("outp", type=Path)
parser.add_argument("--block-size", type=int, default=128)
args = parser.parse_args()

rate, rawdata = scipy.io.wavfile.read(args.inp, mmap=True)
print(rate, rawdata.shape)

#data = np.asarray([left for left,right in rawdata])
data=rawdata
print(data.shape)

freqs, wtimes, spectro = scipy.signal.spectrogram(data, nperseg=args.block_size)

#print(freqs, len(freqs))
print(len(freqs))
print(wtimes)
#print(spectro)
print(len(spectro), len(spectro[0]))

for i,f in enumerate(freqs):
    print(i,f)

def synthesize_block(blockid, width, frequencies, amplitudes):
    samples=[]
    for idx in range(width):
        t = blockid*width+idx
        sample = np.sum(amplitudes * np.sin(t*frequencies*2*np.pi))
        samples.append(sample)
    return samples

blocks = []
for blockid, amplitudes in enumerate(np.transpose(spectro)):
    blocks.append(synthesize_block(blockid, args.block_size, freqs, amplitudes))
    print('synthesized block', blockid)
samples = sum(blocks, [])
samples = np.asarray(samples)
samples = samples / np.max(np.abs(samples))
samples = np.int16(samples * 32000)

scipy.io.wavfile.write(args.outp, rate, samples)
