import pydub
from pydub import AudioSegment

import composiai.Note as n
import composiai.Octave as o
import composiai.Frequency as f
import composiai.Key as k
import composiai.Track as t

import threading
import time

# this file is only for developer for testing purpose

import winsound

note_obj = n.Note()
octave_obj = o.Octave()
key_obj = k.Key()
frequency_obj = f.Frequency()

harryPotterNotes = "-B,E,G,F#,E,B,A, ,F#, ,E,G,F#,Eb,E,-B"
got = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"
got2 = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D"

happy = "D#,C,D,C,F,E,C,C,D,C,G,F,C,C,C,A,F,F,E,D,Bb,Bb,A,F,G,F"
halfgirl = "Bb,+C,+Db,+Eb,+C,Bb,Ab,Ab,Bb,+C,+C"

formatted_notes = note_obj.format_note(got)
note_octave_list = octave_obj.note_to_octave_list(formatted_notes, 5)
note_frequency_dict = frequency_obj.get_note_frequency_dict(note_octave_list, octave_obj)

print(note_frequency_dict)
print(note_octave_list)

#
# def playNote(notte):
#     key_obj.play2(notte)
#     # winsound.Beep(int(note_frequency_dict[notte]), 3000)  # produces beep sound of evey note for 1 second

# # for windows

#
# for note in note_octave_list:
#
#
#     t = threading.Thread(target=playNote, args=(note,))
#     t.start()
#     time.sleep(0.45)

# for note in note_octave_list:
#     key_obj.play2(note)


# from pydub import AudioSegment
# sound1 = AudioSegment.from_file('C:\\Users\\Shubham\\PycharmProjects\\composiAI\\wav\\A1.wav')
# sound2 = AudioSegment.from_file('C:\\Users\\Shubham\\PycharmProjects\\composiAI\\wav\\B1.wav')
# from pydub.playback import play
# #sound1 = sound1 + AudioSegment.silent(duration=1000)
# combined_with_5_sec_crossfade = sound1.append(sound2, crossfade=1)
# play(combined_with_5_sec_crossfade)


#key_obj.play4(note_octave_list)
# #
track1 = t.Track(note_octave_list)
# # track1.play()
# out_wav = track1.export_to_wav('got','output/')
track1.export_to_mp3('got','output/',"C:\\Users\\Shubham\\Downloads\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe")
# track1.channel_count()

# from scipy.io.wavfile import read
# import matplotlib.pyplot as plt
# (fs,x)=read('output/got.wav')
# print('fs => ', fs)
#
# print('x = > ',x[0])
# print("x.size = > ",x.size)
# print("x.shape = > ",x.shape)
#
# plt.figure(1)
# plt.title('Signal Wave...')
# plt.xlabel("time")
# plt.plot(x)
# plt.show()
