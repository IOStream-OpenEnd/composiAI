
from pydub import AudioSegment
from pydub.playback import play as p
import pydub


path_to_wav = '.\\note\\'

class Track:
    sound = AudioSegment.silent(0)

    def __init__(self,note_octave_list):



        self.sound = AudioSegment.silent(duration=self.get_track_duration_ms(note_octave_list))
        #total_length = 0
        pos = 0

        for i in range(len(note_octave_list)):
            note = note_octave_list[i]

            print(note_octave_list[i])
            print(i)
            if note == ' ':
                nth_sound = AudioSegment.silent(duration=2000)
                self.sound = self.sound.overlay(nth_sound, pos)
            else:
                nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
                self.sound = self.sound.overlay(nth_sound, pos)

            # total_length = total_length + (nth_sound.duration_seconds) * 1000
            pos = pos + ((18 / 100) * (nth_sound.duration_seconds) * 1000)
            print("pos=> ", pos)
            # print("total_length=> ", total_length)
            print("length of note", nth_sound.duration_seconds * 1000)
            print("====================================================")
            if i == len(note_octave_list)-1:
                print(pos + nth_sound.duration_seconds * 1000)
                self.sound = self.sound[:pos + nth_sound.duration_seconds * 1000]

    def export_to_wav(self, output_file_name, path):
        self.sound.export(path + output_file_name + '.wav', format="wav")

    def export_to_mp3(self, output_file_name, path, path_to_ffmpeg):
        pydub.AudioSegment.converter = path_to_ffmpeg
        self.sound.export(path + output_file_name + '.mp3', format="mp3")

    def get_track_duration_ms(self, note_octave_list):
        total_duration = 0
        for i in range(len(note_octave_list)):
            note = note_octave_list[i]
            if note == ' ':
                continue
            nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
            total_duration = total_duration + (nth_sound.duration_seconds * 1000)
        return total_duration

    def play(self):
        p(self.sound)

    def channel_count(self):
        print('channel count => ', self.sound.channels)

