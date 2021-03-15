import sys
import time
import re


notes_ocatve = (
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
    ("G4", 8),
    ("Gs4", 9),
    ("Af4", 9),
    ("A4", 10),
    ("As4", 11),
    ("Bf4", 11),
    ("B4", 12),
    ("C5", 13),
)

interval_name = (
    ("1st", 1, "n/a"),
    ("2nd", 2, "n/a"),
    ("-3rd", 3, "n/a"),
    ("3rd", 4, "5:4"),
    ("4th", 5, "4:3"),
    ("b5th", 6, "n/a"),
    ("5th", 7, "n/a"),
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
    ("15th/double octave", 24),
    ("b16th", 25, "n/a"),
    ("16th", 26, "n/a"),
    ("b17th", 27, "n/a"),
    ("17th", 28, "5:1")
)


selected_notes = []

def add_notes(notes):
    selected_notes.append(notes)
    print("You added {}".format(notes))

def get_piano_notes():
    print("""



    >>>>>>> Welcome to the Piano Tuning Assistant! <<<<<<<
    >>>>>>> Enter 'QUIT' to exit the program. <<<<<<<<<<<<
    >>>>>>> Enter 'DISPLAY' to show selected notes <<<<<<<




    """)

def display_notes():
    print("Here are the notes you chose.")
    for note in selected_notes:
        print(note)


# def get_partial():
#     answer = input("Would you like to know the partial? (y/n")
#     if answer == 'y':
#         print("The coincident partial is {}".format(total))


def find_interval(arg, arg2):
        for note in notes_ocatve:
            if str(arg) == note[0]:
                number1 = note[1]
            if str(arg2) == note[0]:
                number2 = note[1]
                total = number2 - number1
                time.sleep(0.9)
        print("That is {} half steps".format(total))

        for interval in interval_name:
            if total == interval[1]:
                total = interval[0]
                print("The interval between {} and {} is a {}".format(arg, arg2, total))

        answer = input("would you like to know the coincidental partial? (y/n)")
        total = interval[2]
        if answer == 'n':
            pass
        elif answer == 'y':
            print("The coincidental partial is {}".format(total))
       


        

            
get_piano_notes()
while True:
    note1 = input("Enter a root test note (e.g. C4, Cs4/Df4; s=sharp, f=flat) ")
    if note1 == 'quit':
        break
    elif note1 == 'display':
        display_notes()
        continue

    add_notes(note1)

    note2 = input("Enter a second test note. ")
    if note2 == 'quit':
        break
    elif note2 == 'display':
        display_notes()
        continue
    

    add_notes(note2)
    find_interval(note1, note2)
   