#!/usr/bin/env python3

import math
import numpy as np
import scipy
import scipy.io.wavfile
import sys

RATE=44100
_, freq, length, outp = sys.argv
freq=float(freq)
length=float(length)

sample_freq = freq / RATE

t = np.asarray(list(range(int(RATE*length))))
samples = np.sin(t*sample_freq * np.pi)

samples = np.asarray(samples)
samples = np.int16(samples * 32000)

scipy.io.wavfile.write(outp, RATE, samples)
