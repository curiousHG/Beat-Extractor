import aubio
import numpy as np

s = aubio.source('Aero Chord - Surface.wav')
print(type(s))
print(s.uri, s.samplerate, s.channels, s.hop_size)
# print(aubio.tempo.get_bpm())
with s as source:
    n_frames = 0
    for samples in source:
        n_frames += len(samples)
    print(f'read {n_frames} samples in {samples.shape[0]} channels from file {source.uri}')
s=aubio.tempo('Aero Chord - Surface.wav')