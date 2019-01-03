import composiai.Composer as cp

# WARNING => this file is for demo purpose only. this is not currently working. Please don't try to run it.


harryPotterNotes = "-B E G F# E B A F#   E G F# Eb E -B -B E G F# E B +D +Db +C Ab +C B Bb Eb G E G B G B G +C B Bb F# G B Bb Eb E B G B G B G +D +Db +C Ab +C B Bb Eb G E"


myComposer = cp.Composer()
myComposer.input_notes_sequence(harryPotterNotes)
myComposer.set_octave(4)
myComposer.compose()
myComposer.play()




