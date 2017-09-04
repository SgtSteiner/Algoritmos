"""
Problem #88 Pitch and Notes

http://www.codeabbey.com/index/task_view/pitch-and-notes
http://elclubdelautodidacta.es/wp/2012/08/calculo-de-la-frecuencia-de-nuestras-notas-musicales/

The music could be represented as a stream of different sounds. We can distinguish these sounds as they have different
tones. For example if we listen to "Moonlight Sonata" of Beethoven, its 1st movement (find it on youtube if you forget
what it is) - our ear easily catch in the beginning the same pattern of 3 tones played several times.

These tones are called notes in music. From physical point of view they are just stable oscillations (of a string or
some other part of instrument) in the air.

Such oscillations are characterized firstly by the frequency - i.e. simply the amount of "forth-and-back" movements
performed during a second. If the string make 440 such oscillations per second, we say it has a pitch (or frequency)
of 440 Hz (the measurement unit is called Hertz after famous German scientist who discovered electromagnetic waves
while trying to prove they could not exist).

What is important, notes have not some randomly assigned pitch, but rather one defined by simple mathematical law.
This task is dedicated to calculation of note frequencies.

NOTE NAMES

In music the whole range of possible pitches is divided in octaves. Each octave have frequency range twice larger
compared to preceding one, i.e. if one octave covers the range 110 ... 220 Hz, the next will cover
the range 220 ... 440 Hz, while third - 440 ... 880 Hz.

Each octave has 12 notes in it, of them 7 have proper names, C D E F G A B in English musical notation.
Other 5 notes are added between some of these and have derived names, so the whole octave looks like:

C  C#  D  D#  E  F  F#  G  G#  A  A#  B

Notes with # sign are read as C-sharp for example. You see, there are no "sharps" for E and B - strictly speaking E#
has the same pitch as F and B# has the same pitch as C of the next octave.

So the full title of the note consists of its own name and the number of octave, e.g.:

A2 G#5 G#2 A1 F3 D4 D2 E5 C#3 D#1 E3 C2 F4 B2 A#3 D3 D1 B5 A#4

FREQUENCY LAW

You see, the frequency range of octave is not constant. Rathe the ratio between ranges of octaves is a constant
factor of 2. The same with notes - the ratio of frequencies of two neighbor notes is a constant - and has such a value
that if we multiply it by itself for 12 times (i.e. raising note for 12 steps) whe get the value of 2,
i.e. the whole octave.

You may guess that since the ratios of octave steps is represented by a sequence of powers of 2, i.e.:

2 ^ 1 = 2   2 ^ 2 = 4   2 ^ 3 = 8 ...

then the ratios of single note steps are created similarly:

2 ^ (1/12)   2 ^ (2/12)   2 ^ (3/12)   ...   2 ^ (12/12) = 2 ^ 1

Calculator will help us to see that the ratio for a single pitch step is 1.059463094, though it is not important.

Now we can find the frequency for any note, though we need some basis point. Internationaly it is chosen as
the pitch for A4 note which is exactly 440 Hz, so that A3 is 220 Hz and C4 is about 261.63 Hz etc.

PROBLEM STATEMENT

You are given a sequence of notes - calculate frequencies for them using the explanations above.

Input data will have the number of notes in the first line.
Next line contains note names separated by spaces.
Answer should contain frequencies for these notes, rounded to nearest integer.

Test Data:
19
D3 G2 E1 C5 F#3 G#3 G#2 E2 A#5 D#5 F#5 F5 C4 A#3 A1 D2 C#4 G3 C#3
"""

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
R = 1.059463094     # ratio for a single pitch step
A4_PITCH = 440      # A4' pitch
A4_POS = 9          # A4' index
A4_OCT = 4          # A4' octave


def get_frequency(note, octave):
    diff_semitone = (NOTES.index(note) - A4_POS) + (12 * (octave - A4_OCT))
    return round(A4_PITCH * R**diff_semitone)

num_data = int(input())
notes = input().split()
frequencies = [get_frequency(note[:-1], int(note[-1])) for note in notes]

print(" ".join(map(str, frequencies)))
