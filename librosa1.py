import librosa
y, sr = librosa.load('Aero Chord - Surface.wav')

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
l=[]
for i in range(len(beat_frames)):
    l.append([beat_frames[i],beat_times[i]])
print(l)

