
import pyaudio
import numpy as np


class Key:

    def play(self, note_octave_list,note_frequency_dict):
        p = pyaudio.PyAudio()

        volume = 0.5  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer
        duration = 3.0  # in seconds, may be float
        #f = 439.435  # sine frequency, Hz, may be

        for note in note_octave_list:

          # generate samples, note conversion to float32 array

          samples = (np.sin(2 * np.pi * np.arange(fs * duration) * note_frequency_dict[note] / fs)).astype(np.float32)

          # for paFloat32 sample values must be in range [-1.0, 1.0]
          stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

          # play. May repeat with different volume values (if done interactively)
          stream.write(volume * samples)

        stream.stop_stream()
        stream.close()

        p.terminate()
