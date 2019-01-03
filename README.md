# composiAI
composes music based on AI

### BASIC KNOWLEDGE

#### 1. What is piano?
   
   Piano is a music instrument that produces music by sequence of notes.
   
   A standard piano have 9 octaves and 88 keys
   
#### 2. What is note?

   a note is the pitch and duration of a sound, and also its representation in musical notation.
   
   example => {C,C#,D,D#,E ,F,F#,G,G#,A,A#,B}

#### 3. What is octave?

   A octave is set of notes of particular frequencies.
   
   Octaves are numbered from 0 to 8
   
   Each octave have 12 keys/notes
   
   Example => 4th octave => {C4,C#4,D4,D#4,E4 ,F4,F#4,G4,G#4,A4,A#4,B4}
   
   Exceptiions => 0th octave has two keys and 8th octave has one key in standard piano
   
#### 4. what is the format of sequence of notes? I
   
   sequence of notes is given by example(Harry Potter Theme Music) => 
   ```
   "-B E G F# E B A F#   E G F# Eb E -B
-B E G F# E B +D +Db +C Ab +C B Bb Eb G E
G B G B G +C B Bb F# G B Bb Eb E B
G B G B G +D +Db +C Ab +C B Bb Eb G E" 
```
#### 5. what is +D or Ab or -B

so there are three tpyes of octave in a sequence.
1. main octave => let say 4th
2. prev octave => main-1 => 3th
3. next octave => main+1 => 5th

so here +D = D5 and Ab = G# and -B = B3

please refer above diagram clearly to understand better...

#### 6. How we produce sound of every note?

every note has a particular frequency.

1. For Python

we use Beep(frequency,duration) in python for windows to produce sound of a particular frequency.

```python
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

```

> find function for linux is the task to be done 

2. For Javascript

check out this blog [Generate Sounds using Javascript!](http://marcgg.com/blog/2016/11/01/javascript-audio/)

![Image of Yaktocat](https://musicmotivated.com/wp-content/uploads/2014/06/piano-guitar-bass-frequency-chart-88-keys-pitches.jpg)



### FEATURES
#### Basic
1. play music based on notes
2. developer usuable library

#### Advanced
1. music generation base don AI

### Teams

1. For Python 3
2. for Javascript

### Implementation PLan

TASK 1 : creating relevant class of various objects needed in our project

TASK 2 : creating various functions needed in out classes

TASK 3 : testing on both linux and windows

### Classes with Functions

1. - composer
     - input_notes_sequence()
     - set_octave()
     - play()
2. - note
     - format_note()
3. - octave
     - note_to_octave_list()
     - nth_octave_list()
4. - frequency
     - nth_octave_frequency_dict()
     - note_to_frequency()

### Process

1. we take raw input as list and main octave number

example => ["C#","-D","F"," ","C#4","D3","F4"]

2. then formats the input notes according to main octave

3. then fetch the frequencies according to notes

4. at last play them
