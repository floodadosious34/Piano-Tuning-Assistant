def get_piano_notes():
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    
    
try:
    note1 = input("Pick a root note from A-G ")
    note2 = input("Pick a note you want to test against the root note. ")
except ValueError:
    print("That is not a valid note. Please try again")
else:
    print("You chose {} and {}, is this correct?".format(note1, note2))

get_piano_notes()

