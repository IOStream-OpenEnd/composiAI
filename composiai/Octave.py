class Octave:

    def note_to_octave_list(self, formatted_notes, main_octave):
        note_octave_list = []

        for note in formatted_notes:
            if len(note) == 2 and not str(note).__contains__('#'):
                if str(note[0]) == '-':
                    note = note[1] + str(main_octave - 1)
                   # print(note)
                if str(note[0]) == '+':
                    note = note[1] + str(main_octave + 1)
                   # print(note)
            elif len(note) == 2 and str(note).__contains__('#'):
                note = note + str(main_octave)
               # print(note)
            elif len(note) == 3 and str(note).__contains__('#'):
                if str(note[0]) == '-':
                    note = note[1] + '#' + str(main_octave - 1)
                   # print(note)
                if str(note[0]) == '+':
                    note = note[1] + '#' + str(main_octave + 1)
                   # print(note)
            elif len(note) == 1:
                if note != " ":
                    note = note + str(main_octave)
                   # print(note)
                else:
                    pass
            else:
                print(note, "not => found", len(note))
            note_octave_list.append(note)
           # print(note_octave_list)
        return note_octave_list

    def get_nth_octave_list(self, octave_number):
        nth_octave_list = []

        return nth_octave_list
