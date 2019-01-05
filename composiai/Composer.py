import composiai.Note as n
import composiai.Octave as o
import composiai.Frequency as f


import composiai.Track as t


class Composer:

    def __init__(self, raw_notes , main_octave):
        self.note_obj = n.Note()  # creating note object
        self.octave_obj = o.Octave()  # creating octave object
        self.frequency_obj = f.Frequency()  # creating frequency object
        self.main_octave = main_octave
        self.note_frequency_dict = {}
        self.note_octave_list = []
        # inputs raw notes as string type
        self.raw_notes = raw_notes
        # converts raw notes to formatted notes
        formatted_notes = self.note_obj.format_note(self.raw_notes)
        if main_octave in range(1,7):
            # converts notes to the corresponding main octave given by the user
            self.note_octave_list = self.octave_obj.note_to_octave_list(formatted_notes, self.main_octave)
            # gets the dictionary {"note" : frequency } of notes with frequency
            self.note_frequency_dict = self.frequency_obj.get_note_frequency_dict(self.note_octave_list,self.octave_obj)
            self.track_obj = t.Track(self.note_octave_list)
        else:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print(" main octave must be in between 1 to 7")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    def set_octave(self, main_octave):
        # sets main octave to the composer
        self.main_octave = main_octave

    def play(self):
        self.track_obj.play()

    def export_as_wav(self, output_file_name, path):
        self.track_obj.export_to_wav(output_file_name, path)

    def export_as_mp3(self, output_file_name, path, path_to_ffmpeg):
        self.track_obj.export_to_mp3(output_file_name, path, path_to_ffmpeg)

