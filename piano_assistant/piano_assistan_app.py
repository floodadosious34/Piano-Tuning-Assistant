import sys
import time


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

def find_interval(arg, arg2):
        for note in notes_ocatve:
            if str(arg) == note[0]:
                number1 = note[1]
            if str(arg2) == note[0]:
                number2 = note[1]
                total = number2 - number1
                time.sleep(0.9)
        print("That is {} half steps".format(total))

            
get_piano_notes()
while True:
    note1 = input("Enter a root test note (e.g. C4, Cs4/Df4; s=sharp, f=flat). ")
    if note1 == 'QUIT':
        break
    elif note1 == 'DISPLAY':
        display_notes()
        continue
    

    add_notes(note1)

    note2 = input("Enter a second test note. ")
    if note2 == 'QUIT':
        break
    elif note2 == 'DISPLAY':
        display_notes()
        continue
    

    add_notes(note2)
    display_notes()
    find_interval(note1, note2)