
import pyaudio
import numpy as np
import wave
from pydub import AudioSegment
from pydub.playback import play as p

path_to_wav = '.\\note\\'

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

        if note == ' ':
            return

        CHUNK = 1024

        wf = wave.open(path_to_wav + note + '.wav', 'rb')

        # instantiate PyAudio (1)
        p = pyaudio.PyAudio()

        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)



        # read data
        data = wf.readframes(CHUNK)
        print(data)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)


        # stop stream (4)
        stream.stop_stream()
        stream.close()

        # close PyAudio (5)
        p.terminate()

    def play3(self, note_octave_list):
        print('note octave list inside play3 => ',note_octave_list)
        sound = AudioSegment.empty()

        for i in range(len(note_octave_list)):

            note = note_octave_list[i]
            print(note_octave_list[i])
            print(i)

            nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
            #print(nth_sound.duration_seconds)
            if i == 0:
                sound = sound.append(nth_sound,0)
            else:
                sound = sound.append(nth_sound, crossfade=100)

        p(sound)

    # def get_track_duration_ms(self,note_octave_list):
    #     total_ducration = 0
    #     for i in range(len(note_octave_list)):
    #         note = note_octave_list[i]
    #         nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
    #         total_ducration = total_ducration + (nth_sound.duration_seconds * 1000)
    #     return total_ducration
    #
    #
    # def play4(self ,note_octave_list):
    #     sound = AudioSegment.silent(duration= self.get_track_duration_ms(note_octave_list))
    #     pos = 0
    #     total_length = 0
    #     for i in range(len(note_octave_list)):
    #
    #         note = note_octave_list[i]
    #         print(note_octave_list[i])
    #         print(i)
    #         nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
    #         sound = sound.overlay(nth_sound, pos)
    #         pos = total_length + 450
    #         print("pos=> ",pos)
    #         total_length = total_length + (nth_sound.duration_seconds) * 1000
    #         print("total_length=> ", total_length)
    #
    #         FH = sound.export("output.wav", format="wav")
    #
    #     p(sound)
    #
    #
    #
    #
