"""
Problem #89 Instrument Tuner

http://www.codeabbey.com/index/task_view/instrument-tuner

This task is the reverse of Pitch and Notes (so perhaps you may want to read or solve it first) - suppose you are
building the electronic tuner for guitar, violin or piano - and you already connected microphone to microcontroller
and succeeded in registering the sound wave, smoothering it and measuring its frequency.

Now the only thing remained is to write a part of program responsible for determining the note played by its frequency.
I.e. if the device have detected sound of 440 Hz it should be able to tell that note A4 is played.

Since in reality instruments could be slightly out of tune, you need not expect that pitch will be mathematically exact.
Nevertheless you'll be able to determine the nearest note. I.e. frequencies of 433 Hz or 449 Hz should anyway be
classified as A4.

Input data contains number of notes to identify.
The next line will provide the frequencies, separated by spaces.
Answer should contain identified note names.

Test Data:
22
61.8 124.5 388.9 54.8 292.5 40.5 740.0 69.6 184.6 129.5 110.0 99.8 65.9 584.4 307.4 372.6 39.3 176.0 117.0 787.9 224.2 843.1
"""

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
R = 1.059463094     # ratio for a single pitch step
A4_PITCH = 440      # A4' pitch
A4_POS = 9          # A4' index
A4_OCT = 4          # A4' octave


def gen_frec():
    """ Return: dictionary frequencies 5 octaves """
    f = {}
    for octave in range (1, 6):
        for i in range(len(NOTES)):
            diff_semitone = (i - A4_POS) + (12 * (octave - A4_OCT))
            frec = round(A4_PITCH * R ** diff_semitone)
            f[frec] = NOTES[i] + str(octave)
    return f


def get_note(frecuency, p):
    """ Parameter: frecuency dictionary, pitch
        Return: note
    """
    if p in frecuency:
        return frecuency[p]
    frec_min = 0
    frec_max = 9999
    for frec in sorted(frecuency):
        if frec > p:
            frec_max = frec
            break
        frec_min = frec
    if frec_max - p < p - frec_min:
        return frecuency[frec_max]
    else:
        return frecuency[frec_min]


num_data = int(input())
pitch = list(map(float, input().split()))
frecuency = gen_frec()
notes = [get_note(frecuency, round(p)) for p in pitch]
print(" ".join(notes))
