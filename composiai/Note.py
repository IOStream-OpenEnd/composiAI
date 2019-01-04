

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


class Note:

    def format_note(self, raw_notes , type = 1 ):

        # suppose if input notes have Ab instead of G# it converts Ab to G# and similarly others
        # suppose if input note is in lowercase it converts it in standard uppercase
        # converting the raw_notes (string type) to formatted_notes (list type)
        # exp => raw_notes = "-B,E,g,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
        # to formatted_notes = ['-B','E','G','F#','E','B',A','F#',' ',' ','E','G','F#','D#','E','-B']
        # NOTE : here g is converted to 'G' and Eb is converted to 'D#' similarly others.

        formatted_notes_list = []

        for note in raw_notes.split(','):
            if len(note) == 2:
                if note == 'Db':
                    note = 'C#'
                elif note == 'Eb':
                    note = 'D#'
                elif note == 'Gb':
                    note = 'F#'
                elif note == 'Ab':
                    note = 'G#'
                elif note == 'Bb':
                    note = 'A#'
                else:
                    pass
            elif len(note) == 3:
                print(note)
                print(note[1:3])
                if note[1:3] == 'Db':
                    note = str(note[0]) + 'C#'
                elif note[1:3] == 'Eb':
                    note = str(note[0]) + 'D#'
                elif note[1:3] == 'Gb':
                    note = str(note[0]) + 'F#'
                elif note[1:3] == 'Ab':
                    note = str(note[0]) + 'G#'
                elif note[1:3] == 'Bb':
                    note = str(note[0]) + 'A#'
            else:
                pass
            formatted_notes_list.append(note)
        print(formatted_notes_list)

        return formatted_notes_list
