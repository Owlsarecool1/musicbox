import musicbox


# list of tuples holding notes+integers
notes = (("C", 60),
         ("D", 62),
         ("E", 64),
         ("F", 65),
         ("G", 67),
         ("A", 69),
         ("B", 71))
Major_Intervals=[2,2,1,2,2,2,1]
Minor_Intervals=[2,1,2,2,1,2,2]
# Sets import of musicbox
# to use later
my_music = musicbox.MusicBox()

# Gets letters of note
notes_in_list = [x[0] for x in notes]





# Turns note given into integer
def note_to_int(note):

    octave = note.rfind("^")+1
    for letter in notes:
        if letter[0] == note[octave]:
            letter_number=letter[1]
    if len(note[octave:])== 2:
        if note[octave+1] == "#":
            sharp_or_flat =1
        elif note[octave+1]=="b":
            sharp_or_flat=-1
    else:
        sharp_or_flat=0
    list_to_return=letter_number+12*octave+sharp_or_flat

    return  list_to_return



# prints out the menu
def print_menu():
    print("Main Menu:\n"
          "1. Play Song\n"
          "2. Play scale\n"
          "3. Quit")


# Gets the users option at menu screen
def get_menu_choice():
    decision = int(input("Make a selection: "))
    while decision > 3 or decision <= 0:
        print("Please enter a valid option")
        decision = int(input("Make a selection: "))
    return decision


# Get's notes from user
# Used if else for invalid note
def get_scale():
    scale_name = str(input("Please input a scale:\n"))
    while ('major' not in scale_name ) and ('minor'not in scale_name):
        scale_name=str(input("Enter scale name:\n"))
    sep=scale_name.split(" ")
    scale_name = [note_to_int((sep[0])),(sep[1])]
    return scale_name



# Plays notes after converting to int
def scale_to_ints(scale):
    notes = [scale[0]]
    if scale[1] == "major":
        for i in Major_Intervals:
            notes.append(i+notes[-1])
        return notes
    else:
        for i in Minor_Intervals:
            notes.append(i+notes[-1])
        return notes



# put  together
def menu_play_scale():
    c = get_scale()
    f = scale_to_ints(c)
    for i in f:
        my_music.play_note(i, 500)
    return


# Get's name of text file from user as string
def get_song_file():
    song_file = input("Please enter a the song file name including the extension: ")
    return song_file


# Play the song file given by the user
def play_song(file):
    # Opens file and reads the lines
    for line in open(file):
        split = line.split(' ')

        # Variable for when notes have a # or b
        suffix = split[0]

        # lines starts with //, it's skipped
        if line.startswith("//"):
            continue

        # variable gets duration from every note and chord in the given files
        duration = int(split[-1].strip('"').strip('\n'))

        # Used for seperate lines with single notes
        if len(split) > 2:
            chord_notes = []
            for x in split:
                chord_checker = x.strip('^#b')
                if chord_checker.isalpha():
                    chords = note_to_int(x)
                    chord_notes.append(chords)
            my_music.play_chord(chord_notes, duration)

        # used for the lines with single notes
        else:
            # Used only when note is vanilla(without flat or sharp)

            if split[0] in notes_in_list:
                og_note = note_to_int(split[0])

                my_music.play_note(og_note, duration)

            #  figures out how many octaves
            # raised by
            elif split[0].find('^') == 0:
                octave_increase = note_to_int(split[0])
                my_music.play_note(octave_increase, duration)

            # These next two elif statements are used when the note
            # has a suffix
            # This one is used when it's a sharp note
            elif suffix[-1] == '#':
                sharp_note = note_to_int(split[0])
                my_music.play_note(sharp_note, duration)

            #  used when it's a flat note
            elif suffix[-1] == 'b':
                flat = note_to_int(split[0])
                for number in flat:
                    my_music.play_note(number, duration)

            # invalid notes are treated as a pause
            elif split[0] not in notes:
                my_music.pause(duration)


def menu_play_song():
    song = get_song_file()
    play_song(song)


# define main
def main():
    menu_choice = 0
    while menu_choice != 3:
        print_menu()
        menu_choice = get_menu_choice()
        if menu_choice == 1:
            menu_play_song()
        if menu_choice == 2:
            menu_play_scale()
    quit()


main()
my_music.close()