import composiai.Note
import composiai.Octave
import composiai.Frequency
import winsound

class Composer:

    note_obj = composiai.Note()  # creating note object
    octave_obj = composiai.Octave()  # creating octave object
    frequency_obj = composiai.Frequency()  # creating frequency object
    main_octave = 4  # default value 4
    raw_notes = ""
    note_frequency_dict = {}
    note_octave_list = []

    def input_notes_sequence(self, raw_notes):
        # inputs raw notes as string type
        self.raw_notes = raw_notes

    def set_octave(self, main_octave):
        # sets main octave to the composer
        self.main_octave = main_octave

    def compose(self):
        # composes raw notes to the given main octave

        formatted_notes = self.note_obj.format_note(self.raw_notes)  # converts raw notes to formatted notes

        self.note_octave_list = self.octave_obj.note_to_octave_list(formatted_notes, self.main_octave)
        # converts notes to the corresponding main octave given by the user

        self.note_frequency_dict = self.frequency_obj.get_note_frequency_dict(self.note_octave_list, self.octave_obj)
        # gets the dictionary {"note" : frequency } of notes with frequency

    def play(self):

        # for windows
        for note in self.note_octave_list:
            winsound.Beep(self.note_frequency_dict[note], 1000)  # produces beep sound of evey note for 1 second
