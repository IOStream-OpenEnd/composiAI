
from pydub import AudioSegment
from pydub.playback import play as p


path_to_wav = '.\\wav\\'

class Track:
    sound = AudioSegment.silent(0)

    def __init__(self,note_octave_list):

        self.sound = AudioSegment.silent(duration=self.get_track_duration_ms(note_octave_list))
        pos = 0
        total_length = 0
        for i in range(len(note_octave_list)):
            note = note_octave_list[i]
            print(note_octave_list[i])
            print(i)
            nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
            self.sound = self.sound.overlay(nth_sound, pos)
            pos = total_length + 450
            print("pos=> ", pos)
            total_length = total_length + (nth_sound.duration_seconds) * 1000
            print("total_length=> ", total_length)

    def export_to_wav(self, output_file_name ,path ,):
        self.sound.export(path + output_file_name + '.wav', format="wav")

    def get_track_duration_ms(self, note_octave_list):
        total_duration = 0
        for i in range(len(note_octave_list)):
            note = note_octave_list[i]
            nth_sound = AudioSegment.from_file(path_to_wav + note + '.wav')
            total_duration = total_duration + (nth_sound.duration_seconds * 1000)
        return total_duration

    def play(self):
        p(self.sound)

    def channel_count(self):
        print('channel count => ', self.sound.channels)

