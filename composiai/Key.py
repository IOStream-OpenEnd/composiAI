
import pyaudio
import numpy as np
import wave


class Key:

    def play(self, f):
        p = pyaudio.PyAudio()

        volume = 0.5  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer
        duration = 3.0  # in seconds, may be float
        #f = 439.435  # sine frequency, Hz, may be



        # generate samples, note conversion to float32 array

        samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

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

    def  play2(self, note):

        CHUNK = 1024

        wf = wave.open('.\\wav\\' + note + '.wav', 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()


