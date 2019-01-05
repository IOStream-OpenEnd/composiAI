import composiai.Composer as cp



harryPotterNotes = "-B,E,G,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
got = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"


myComposer = cp.Composer(harryPotterNotes, 5)
#myComposer.play()


#myComposer.export_as_mp3("got","output/","C:\\Users\\Shubham\\Downloads\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe")




