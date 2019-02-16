import composiai.Composer as cp
import os


harryPotterNotes = "-B,E,G,F#,E,B,A,F#, , ,E,G,F#,Eb,E,-B"
got = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"


myComposer = cp.Composer(got, 5)
#myComposer.play()

output_file_path = os.path.dirname(os.path.realpath(__file__))

output_file_name = "got"

##### To generate mp3 file

myComposer.export_as_wav(output_file_name,output_file_path)

##### To generate mp3 file

#path_to_ffmpeg = "C:\\Users\\Shubham\\Downloads\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"

#myComposer.export_as_mp3(output_file_name,output_file_path,path_to_ffmpeg)




