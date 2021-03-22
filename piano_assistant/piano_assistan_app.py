import sys
import time
import re
from scipy.io.wavfile import write
import numpy as np

samplerate = 44100

def get_piano_notes():
    '''
    Returns a dict object for all the piano 
    note's frequencies
    '''
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B'] 
    base_freq = 261.63 #Frequency of Note C4
    
    note_freqs = {octave[i]: base_freq * pow(2,(i/12)) for i in range(len(octave))}        
    note_freqs[''] = 0.0
    
    return note_freqs


def get_wave(freq, duration=0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song.astype(np.int16)


def main():
    music = input("Would you like to hear those notes y/n? ")
    if music == 'y':
        music_notes = 'C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C'
        data = get_song_data(music_notes)
        data = data * (16300/np.max(data))
        write('selected-notes.wav', samplerate, data.astype(np.int16))
    else:
        quit


notes_ocatve = [
    ("C4", 1),
    ("Cs4", 2),
    ("Df4", 2),
    ("D4", 3),
    ("Ds4", 4),
    ("Ef4", 4),
    ("E4", 5),
    ("F4", 6),
    ("Fs4", 7),
    ("Gf4", 7),
    ('G4', 8),
    ("Gs4", 9),
    ("Af4", 9),
    ("A4", 10),
    ("As4", 11),
    ("Bf4", 11),
    ("B4", 12),
    ("C5", 13),
    ("Cs5", 14),
    ("Df5", 14),
    ("D5", 15),
    ("Ds5", 16),
    ("Ef5", 16),
    ("E5", 17),
    ("F5", 18),
    ("Fs5", 19),
    ("Gf5", 19),
    ("G5", 20),
    ("Gs5", 21),
    ("Af5", 21),
    ("A5", 22),
    ("As5", 23),
    ("Bf5", 23),
    ("B5", 24),
    ("C6", 25),
    ("Cs6", 26)
]

interval_name = (
    ("1st", 1, "n/a"),
    ("2nd", 2, "n/a"),
    ("-3rd", 3, "n/a"),
    ("3rd", 4, "5:4"),
    ("4th", 5, "4:3"),
    ("b5th", 6, "n/a"),
    ("5th", 7, "3/2"),
    ("+5th", 8, "n/a"),
    ("6th", 9, "5/3"),
    ("b7th", 10, "n/a"),
    ("7th", 11, "n/a"),
    ("8th/octave,", 12, "2:1, 4:2, 6:3"),
    ("b9th", 13, "n/a"),
    ("9th", 14, "n/a"),
    ("b10th", 15, "n/a"),
    ("10th", 16, "5/2"),
    ("11th", 17, "n/a"),
    ("b12th", 18, "n/a"),
    ("12th", 19, "n/a"),
    ("b13th", 20, "n/a"),
    ("13th", 21, "n/a"),
    ("b14th", 22, "n/a"),
    ("14th", 23, "n/a"),
    ("15th/double octave", 24, "n/a"),
    ("b16th", 25, "n/a"),
    ("16th", 26, "n/a"),
    ("b17th", 27, "n/a"),
    ("17th", 28, "5:1")
)


selected_notes = []

def add_notes(arg):
    note = arg
    selected_notes.append(note)
  

def get_piano_notes():
    print("""



    >>>>>>> Welcome to the Piano Tuning Assistant! <<<<<<<
    >>>>>>>>>>>>>>> Designed by J. Flood <<<<<<<<<<<<<<<<<
    >>>>>>> Enter 'DISPLAY' to show selected notes <<<<<<<




    """)

def display_notes():
    answer = input("Would you like to see the notes you chose? y/n")
    if answer == 'y':
        for note in selected_notes:
            print(note)
    elif answer == 'n':
        quit
        

def find_interval(arg, arg2):
    for note in notes_ocatve:
        if str(arg) == note[0]:
            number1 = note[1]
        if str(arg2) == note[0]:
            number2 = note[1]
            try:
                if number2 > number1: 
                    total = number2 - number1
                    time.sleep(0.9)
                print("That is {} half steps".format(total))
            except UnboundLocalError:
                print("That is not a valid entry. Make sure the root note is smaller than the second note")
                return False
                
            

    while True:
        for interval in interval_name:
            if total == interval[1]:
                total = interval[0]
                total1 = interval[2]
                print("The interval between {} and {} is a {}".format(arg, arg2, total))
                
                answer = input("Would you like to know the coincidental partial? (y/n)")
                if answer == 'y':
                    print("The coincidental partial is {}".format(total1))
                    return False
                elif answer == 'n':
                    return False
        

def test_note(arg):
    testN = str(arg)
    index = 1
    for item in notes_ocatve:
        note = item[0]
        index+=1
        if testN == note:
            return True 
        elif testN != note:
            continue 
    print("{} is not a valid note. Please Try again.  ".format(arg))
    return False
        

            
get_piano_notes()
while True:
    run = input("Hello, if you would like to start press r. If you would like to quit, type q.")
    if run == 'q':
        break
    while run == 'r':
        while True:
            note1 = input("Enter a root test note (e.g. C4, Cs4/Df4; s=sharp, f=flat) ")
            result = test_note(note1)
            if result is False:
                break
            elif result is True:
                add_notes(note1)
            elif note1 == 'display':
                display_notes()
                continue
            while True:
                note2 = str(input("Enter a second test note. "))
                if note2 == 'quit':
                    break
                elif note2 == 'display':
                    display_notes()
                    continue
                result2 = test_note(note2)
                if result2 is True:
                    add_notes(note2)
                    break
                elif result is False:
                    continue
                
            intervalStatus = find_interval(note1, note2)
            if intervalStatus is False:
                break
        display_notes()
        main()
        break
            
            



   