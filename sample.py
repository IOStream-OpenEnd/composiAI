import composiai.Composer as cp

# WARNING => this file is for demo purpose only. this is not currently working. Please don't try to run it.


harryPotterNotes = "-B,E,G,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"

myComposer = cp.Composer()
myComposer.input_notes_sequence(harryPotterNotes)
myComposer.set_octave(4)
myComposer.compose()
myComposer.play()




