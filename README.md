# composiAI
composes music(.wav or .mp3) based on piano notes.
> NOTE : Currently there is nothing related to AI

### USAGE

```python

#importing the composer
import composiai.Composer as cp

# storing the input notes into a variable as a string of note seperated by A COMMA(",")
# use single space between COMMA to add a gaps in between two notes

game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

# creating composer object with two arguments
# first argument = game_of_thrones = is the the notes string 
# second argument = 5 =  is the octave number
# octave number ranges from 1 to 7

myComposer = cp.Composer(game_of_thrones, 5)

# using the play function on the myComposer object to play music track generated by our string game_of_thrones
myComposer.play()

```

#### API Documentation

This document is a work in progress.
#### Composer()
```python

import composiai.Composer as cp

game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

myComposer = cp.Composer(game_of_thrones, 5)

myComposer.play()

```
#### Composer().set_octave(main_octave)
```python

import composiai.Composer as cp
game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

myComposer = cp.Composer(game_of_thrones, 5)
myComposer.set_octave(4)
myComposer.play()

```
#### Composer().play()
```python

import composiai.Composer as cp
game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

myComposer = cp.Composer(game_of_thrones, 5)
myComposer.set_octave(4)
myComposer.play()

```
#### Composer().export_as_wav(output_file_name, path)
```python

import composiai.Composer as cp
import os

game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

myComposer = cp.Composer(game_of_thrones, 5)

output_file_path = os.path.dirname(os.path.realpath(__file__))

output_file_name = "got"

##### To generate mp3 file

myComposer.export_as_wav(output_file_name,output_file_path)

```
```python

import composiai.Composer as cp
import os

game_of_thrones = "G,C,D#,F,G,C,D#,F,G,C,D#,F,D,-G,-A#,C,D,-G,-A#,C,D,-G, , ,G, ,C, ,D#,F,G, ,C, ,D#,F,D,-A#,D#,F,D,-A#, ,F, ,-A#, ,D#,D,F, ,-A#, ,D#,D,C,-G#,-G#,-A#,C,-F,-G#,-A#,C,-F,-G#,-A#,C"

myComposer = cp.Composer(game_of_thrones, 5)

output_file_path = os.path.dirname(os.path.realpath(__file__))

output_file_name = "got"

##### To generate mp3 file

#please change this path to your path of ffmpeg
path_to_ffmpeg = "path_to_ffmpeg\\ffmpeg\\bin\\ffmpeg.exe"

myComposer.export_as_mp3(output_file_name,output_file_path,path_to_ffmpeg)

```

