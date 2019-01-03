import composiai.Note as n
import math
class Frequency:

    def nth_octave_frequency_dict(self):
        pass

    def note_to_frequency(self, note):
        if note == " ":
         return 37
        standard_notes = n.NOTES
        octave = None
        key_number = standard_notes.index(note[0])
        if len(note) == 3:
            octave = note[2]
        else:
            octave = note[1]

        if key_number < 3:
            key_number = int(key_number) + 12 + ((int(octave) - 1) * 12) + 1
        else:
            key_number = int(key_number) + ((int(octave) - 1) * 12) + 1

        return 440 * math.pow(2, (key_number - 49) / 12)

    def get_note_frequency_dict(self, note_octave_list, octave_obj):
        note_frequency_dict = {}
        for note in note_octave_list:
            note_frequency_dict[note] = self.note_to_frequency(note)

        return note_frequency_dict
