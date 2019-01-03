import composiai.Note as n
import composiai.Octave as o
import composiai.Frequency as f
import winsound
note_obj = n.Note()
octave_obj = o.Octave()
frequency_obj = f.Frequency()

harryPotterNotes = "-B,E,G,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
got = "G,C,D#,F,G,C,D#,D"
happy = "D#,C,D,C,F,E,C,C,D,C,G,F,C,C,C,A,F,F,E,D,Bb,Bb,A,F,G,F"


formatted_notes = note_obj.format_note(happy)
note_octave_list = octave_obj.note_to_octave_list(formatted_notes, 4)
note_frequency_dict = frequency_obj.get_note_frequency_dict(note_octave_list, octave_obj)

print(note_frequency_dict)

# for windows
for note in note_octave_list:
    winsound.Beep(int(note_frequency_dict[note]), 800)  # produces beep sound of evey note for 1 second

