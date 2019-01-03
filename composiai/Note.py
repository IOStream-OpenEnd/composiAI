

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


class Note:

    def format_note(self, raw_notes , type = 1 ):

        # suppose if input notes have Ab instead of G# it converts Ab to G# and similarly others
        # suppose if input note is in lowercase it converts it in standard uppercase
        # converting the raw_notes (string type) to formatted_notes (list type)
        # exp => raw_notes = "-B,E,g,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
        # to formatted_notes = ['-B','E','G','F#','E','B',A','F#',' ',' ','E','G','F#','D#','E','-B']
        # NOTE : here g is converted to 'G' and Eb is converted to 'D#' similarly others.

        formatted_notes = []

        print(raw_notes.split(','))

        return formatted_notes
