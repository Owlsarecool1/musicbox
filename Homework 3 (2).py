import musicbox


# The list of tuples holding the notes and integers
NOTES = [("C", 60),("D", 62), ("E", 64), ("F", 65), ("G", 67), ("A", 69), ("B", 71)]
MAJOR_INTERVALS = [2,2,1,2,2,2,1]
MINOR_INTERVALS = [2,1,2,2,1,2,2]
# Sets the import of musicbox to variable in order
# to be used later on to play the notes
my_music = musicbox.MusicBox()

# Gets the letters of the note from the list of tuples
list_notes = [x[0] for x in NOTES]

# Turns the note given into the correct integer
def note_to_int(note):

    octave_number = note.rfind("^")+1
    for let in NOTES:
        if let[0] == note[octave_number]:
            num = let[1]
    if len(note[octave_number:]) == 2:
        if note[octave_number+1] == "#":
            flat_orsharp = 1
        elif note[octave_number + 1] == "b":
            flat_orsharp = -1
    else:
        flat_orsharp = 0
    return_list = (num + 12 * octave_number + flat_orsharp)

    return return_list



# Just prints out the menu, nothing special
def print_menu():
    print("Main Menu: \n 1. Play Scale \n 2. Play Song \n 3. Quit")


# Gets and validates the users option at menu screen
def get_menu_choice():
    selection = int(input("Make a selection: "))
    while (selection < 1) or (selection > 3):
        print("Please enter a valid option")
        selection = int(input("Make a selection: "))
    return selection


# Get's the notes from the user
# Used if else for the invalid note ex. P
def get_scale():
    scale = str(input("Please input a scale:\n"))
    while ("minor" not in scale ) and ("major"not in scale):
        scale=str(input("Enter scale name:\n"))
    separated = scale.split(" ")
    scale = [note_to_int((separated[0])), (separated[1])]
    return scale



# Plays the notes after getting the int
def scale_to_ints(scale):
    if scale[1] == "major":
        notes = [scale[0]]
        for i in MAJOR_INTERVALS:
            notes.append(i+notes[-1])
        return notes
    else:
        notes = [scale[0]]
        for i in MINOR_INTERVALS:
            notes.append(i+notes[-1])
        return notes



# Glues everything together in order to play notes
def menu_play_scale():
    g_s = get_scale()
    s_to_i = scale_to_ints(g_s)
    for i in s_to_i:
        my_music.play_note(i, 500)
    return


# Get's the name of the text file from the user as a string
def get_song_file():
    song_file = input("Please enter a the song file name including the extension: ")
    return song_file


# Play the song file given by the user
def play_song(file):
    # Opens up the file and reads the lines
    for line in open(file):
        separate = line.split(" ")

        # Variable is used when notes have a # or b
        find_suffix = separate[0]

        # If the lines starts with //, it's skipped
        if line.startswith("//"):
            continue

        # This variable gets the duration from every note and chord in the given files
        duration = int(separate[-1].strip('"').strip('\n'))

        # Used for seperate lines with single notes to multiple
        if len(separate) > 2:
            chord_notes = []
            for x in separate:
                chord_checker = x.strip('^#b')
                if chord_checker.isalpha():
                    chords = note_to_int(x)
                    chord_notes.append(chords)
            my_music.play_chord(chord_notes, duration)

        # This else section is used for the lines with single notes
        else:
            # Used only when note is vanilla
            # Ex. C, G, B
            if separate[0] in list_notes:
                note_orig = note_to_int(separate[0])

                my_music.play_note(note_orig, duration)

            # If the note has a ^ at the beginning, figures out how many octaves
            # it was raised by
            elif separate[0].find('^') == 0:
                octave_increase = note_to_int(separate[0])
                my_music.play_note(octave_increase, duration)

            # These next two elif statements are used when the note
            # has a suffix
            # This one is used when it's a sharp note
            elif find_suffix[-1] == '#':
                sharp_note = note_to_int(separate[0])
                my_music.play_note(sharp_note, duration)

            # This one is used when it's a flat note
            elif find_suffix[-1] == 'b':
                flat_note = note_to_int(separate[0])
                for number in flat_note:
                    my_music.play_note(number, duration)

            # If there are invalid notes, they are treated as a pause
            elif separate[0] not in separate:
                my_music.pause(duration)


def menu_play_song():
    song = get_song_file()
    play_song(song)


# This is where all the magic happens ;)
def main():
    while True:
        print_menu()
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            menu_play_scale()
        if menu_choice == 2:
            menu_play_song()
        if menu_choice == 3:
            quit


main()
my_music.close()
    

    


