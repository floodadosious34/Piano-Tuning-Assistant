import sys
import time
import re
import requests

#API endpoint for free Kanye west quote generator
kanye_url='https://api.kanye.rest/'
kanye_text='https://api.kanye.rest?format=text/'


response = requests.get(kanye_url)

# Tuple for listing out notes in all octaves
notes_ocatve = [
    ("A0", 1),
    ("As0", 2),
    ("Bf0", 2),
    ("B0", 3),
    ("C1", 4),
    ("Cs1", 5),
    ("Df1", 5),
    ("D1", 6),
    ("Ds1", 7),
    ("Ef1", 7),
    ("E1", 8),
    ("F1", 9),
    ("Fs1", 10),
    ("Gf1", 10),
    ('G1', 11),
    ("Gs1", 12),
    ("Af1", 12),
    ("A1", 13),
    ("As1", 14),
    ("Bf1", 14),
    ("B1", 15),
    ("C2", 17),
    ("Cs2", 18),
    ("Df2", 18),
    ("D2", 19),
    ("Ds2", 20),
    ("Ef2", 20),
    ("E2", 21),
    ("F2", 22),
    ("Fs2", 23),
    ("Gf2", 23),
    ("G2", 24),
    ("Gs2", 25),
    ("Af2", 25),
    ("A2", 26),
    ("As2", 27),
    ("Bf2", 27),
    ("B2", 28),
    ("C3", 29),
    ("Cs3", 30),
    ("Df3", 30),
    ("D3", 31),
    ("Ds3", 32),
    ("Ef3", 32),
    ("E3", 33),
    ("F3", 34),
    ("Fs3", 35),
    ("Gf3", 35),
    ('G3', 36),
    ("Gs3", 37),
    ("Af3", 37),
    ("A3", 38),
    ("As3", 39),
    ("Bf3", 39),
    ("B3", 40),
    ("C4", 41),
    ("Cs4", 42),
    ("Df4", 42),
    ("D4", 43),
    ("Ds4", 44),
    ("Ef4", 44),
    ("E4", 45),
    ("F4", 46),
    ("Fs4", 47),
    ("Gf4", 47),
    ('G4', 48),
    ("Gs4", 49),
    ("Af4", 49),
    ("A4", 50),
    ("As4", 51),
    ("Bf4", 51),
    ("B4", 52),
    ("C5", 53),
    ("Cs5", 54),
    ("Df5", 54),
    ("D5", 55),
    ("Ds5", 56),
    ("Ef5", 56),
    ("E5", 57),
    ("F5", 58),
    ("Fs5", 59),
    ("Gf5", 59),
    ("G5", 60),
    ("Gs5", 61),
    ("Af5", 61),
    ("A5", 62),
    ("As5", 63),
    ("Bf5", 63),
    ("B5", 64),
    ("C6", 65),
    ("Cs6", 66),
    ("D6", 67),
    ("Ds6", 68),
    ("Ef6", 69),
    ("E6", 70),
    ("F6", 71),
    ("Fs6", 72),
    ("Gf6", 72),
    ('G6', 73),
    ("Gs6", 74),
    ("Af6", 74),
    ("A6", 75),
    ("As6", 76),
    ("Bf6", 76),
    ("B6", 77),
    ("C7", 78),
    ("Cs7", 79),
    ("Df7", 79),
    ("D7", 80),
    ("Ds7", 81),
    ("Ef7", 81),
    ("E7", 82),
    ("F7", 83),
    ("Fs7", 84),
    ("Gf7", 84),
    ("G7", 85),
    ("Gs7", 86),
    ("Af7", 86),
    ("A7", 87),
    ("As7", 88),
    ("Bf7", 88),
    ("B7", 89),
    ("C8", 90)
]


# Tuple for listing all intervals and coincident partials
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


# List that populates with selectd notes
selected_notes = []

# Adds selected notes to selected_notes list
def add_notes(arg):
    note = arg
    selected_notes.append(note)
  

# Starts the program
def get_piano_notes():
    welcome_note =  """



    >>>>>>> Welcome to the Piano Tuning Assistant! <<<<<<<
    >>>>>>>>>>>>>>> Designed by J. Flood <<<<<<<<<<<<<<<<<
    >>>>>>> Enter 'DISPLAY' to show selected notes <<<<<<<




    """
    print(welcome_note)
    while True:
        run = input("Hello, if you would like to start press r. If you would like to quit, type q.")
        if run == 'r':
            return run
            break
        elif run == 'q':
            return run
            break
        else:
            pass


# Displays selected notes on command
def display_notes():
    answer = input("Would you like to see the notes you chose? y/n")
    if answer == 'y':
        for note in selected_notes:
            print(note)
    elif answer == 'n':
        pass


# Finds interval between the two selected notes
def find_interval(arg, arg2):
    for note in notes_ocatve:
        if arg == note[0]:
            number1 = note[1]
        if arg2 == note[0]:
            number2 = note[1]
            try:
                if number2 > number1: 
                    total = number2 - number1
                    time.sleep(0.9)
                print("That is {} half steps".format(total))
                return total
            except UnboundLocalError: #checks if the notes is in the wrong order and gives a -x result
                print("That is not a valid entry. Make sure the root note is smaller than the second note")
                return False
                
            
    # Looks for interval name based on result from previous loop
def find_interval_name(arg, arg2, arg3):
    total = arg3
    if total <= 28:
        for interval in interval_name:
            if total == interval[1]:
                total = interval[0]
                total1 = interval[2]
                print("The interval between {} and {} is a {}".format(arg, arg2, total))                    
                answer = input("Would you like to know the coincidental partial? (y/n)")
                if answer == 'y':
                    print("The coincidental partial is {}".format(total1))
                    pass
                elif answer == 'n':
                    pass
    else:
        print("Those notes cannot be tested")

# Test to see if the inputed notes are actually in the list of predetermined notes
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


def start():
    answer = input("Would you like to start again? y/n  ")
    if answer == 'y':
        master_function()
    elif answer == 'n':
        print("Thank You for using the Piano Tuning Assistant. Here is a parting quote from Mr. Kanye West!")
        print(response.json()['quote'])
        quit

          
# Master loop for the program
def master_function():
    result = get_piano_notes()
    if result == 'r':
        note1 = get_note_1()
        note2 = get_note_2()
        interval_total = find_interval(note1, note2)
        find_interval_name(note1, note2, interval_total)
        display_notes()
        start()
    elif result == 'q':
        print("Thank You for using the Piano Tuning Assistant. Here is a parting quote from Mr. Kanye West!")
        print(response.json()['quote'])
        quit



def get_note_1():
    while True:
        note1 = input("Enter a root test note (e.g. C4, Cs4/Df4; s=sharp, f=flat) ")
        result = test_note(note1)
        if result is False:
            pass
        elif result is True:
            add_notes(note1)
            return note1

        
def get_note_2():
    while True:
        note2 = input("Enter a second test note. ")
        result2 = test_note(note2)
        if result2 is False:
            pass
        elif result2 is True:
            add_notes(note2)
            return note2
    

    
master_function()