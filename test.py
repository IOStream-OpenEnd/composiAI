import composiai.Note as n
import composiai.Octave as o
import composiai.Frequency as f
import composiai.Key as k

import threading
import time

import winsound

note_obj = n.Note()
octave_obj = o.Octave()
key_obj = k.Key()
frequency_obj = f.Frequency()

harryPotterNotes = "-B,E,G,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
got = "G,C,D#,F,G,C,D#,D"
happy = "D#,C,D,C,F,E,C,C,D,C,G,F,C,C,C,A,F,F,E,D,Bb,Bb,A,F,G,F"
halfgirl = "Bb,+C,+Db,+Eb,+C,Bb,Ab,Ab,Bb,+C,+C"

formatted_notes = note_obj.format_note(happy)
note_octave_list = octave_obj.note_to_octave_list(formatted_notes, 1)
note_frequency_dict = frequency_obj.get_note_frequency_dict(note_octave_list, octave_obj)

print(note_frequency_dict)
print(note_octave_list)


def playNote(notte):
    key_obj.play2(note)
    # winsound.Beep(int(note_frequency_dict[notte]), 3000)  # produces beep sound of evey note for 1 second

# # for windows
for note in note_octave_list:


    t = threading.Thread(target=playNote, args=(note,))
    t.start()
    time.sleep(.45)

#key_obj.play(note_octave_list,note_frequency_dict)

