
import musicbox
NOTES = [("C", 60),("D", 62), ("E", 64),("F", 65),("G", 67), ("A", 69), ("B", 71)]
MINOR_INTERVALS = [2, 2, 1, 2, 2, 2, 1]
MAJOR_INTERVALS = [2, 1, 2, 2, 1, 2, 2]
ACCENTS = ['b', '#']
OCTAVE = 12
my_music = musicbox.MusicBox()
notes_in_list = [x[0] for x in NOTES]

# Gets the integers of the note from the list of tuples
values_in_list = [x[1] for x in NOTES]
def note_to_int(note):

    # A constant variable used to raise a note when ^ is present
    octave = 12

    # Empty list which then holds the integers given, later returned
    list_to_return = []

    # Checker strips the note of any flats, sharps, or octave raises in
    # order to check if the note is actually a note
    checker = note.strip('^#b')

    if checker in notes_in_list:
        if note.find('^') == 0:
            # This finds out by how many octaves to raise the note
            octave_raise = (note.rfind("^") + 1) * octave

            if note[-1] == '#':
                location = notes_in_list.index(checker)
                value = values_in_list[location] + 1
                final_value = octave_raise + value
                list_to_return.append(final_value)

            elif note[-1] == 'b':
                location = notes_in_list.index(checker)
                value = values_in_list[location] - 1
                final_value = octave_raise + value
                list_to_return.append(final_value)

            else:
                location = notes_in_list.index(checker)
                value = values_in_list[location]
                final_value = value + octave_raise
                list_to_return.append(final_value)

        # Used if the note is vanilla
        elif note in notes_in_list:
            location = notes_in_list.index(checker)
            value = values_in_list[location]
            list_to_return.append(value)

        # Used if note has a sharp or flat
        elif note[-1] == '#':
            location = notes_in_list.index(checker)
            value = values_in_list[location] + 1
            list_to_return.append(value)

        elif note[-1] == 'b':
            location = notes_in_list.index(checker)
            value = values_in_list[location] - 1
            list_to_return.append(value)

    return list_to_return


def print_menu():
        print("Main Menu: \n 1. Play Scale \n 2. Play Song \n 3. Quit")

def get_menu_choice():
    selection = int(input("Please enter a selection: "))
    while selection < 1 or selection > 3:
        selection = int(input("Please enter a selection: "))
    return selection

def get_scale():
    scale = str(input("enter scale name"))
    while ("minor" not in scale) and ("major" not in scale):
        scale = str(input("enter scale name"))
    seperated = scale.split(" ")
    scale = [note_to_int(seperated[0]), (seperated[1])]
    return scale
def scale_to_ints(scale):
    if scale[1] == "major":
        major_list=[scale[0]]
        scalae=scale[0]
        for i in MAJOR_INTERVALS:
            scalae += i
            major_list.append(scalae)
        return major_list
def menu_play_scale():
    a = get_scale()
    b = scale_to_ints(a)
    for i in b:
        my_music.play_note(i, 500)
    return
def get_song_file():
    song_file = input("enter a song file name including the extensions")
    return song_file

def play_song(file):
    # Opens up the file and reads the lines
    for line in open(file):
        split = line.split(' ')

        # Variable is used when notes have a # or b
        find_suffix = split[0]

        # If the lines starts with //, it's skipped
        if line.startswith("//"):
            continue

        # This variable gets the duration from every note and chord in the given files
        duration = int(split[-1].strip('"').strip('\n'))

        # Used for seperate lines with single notes to multiple
        if len(split) > 2:
            chord_notes = []
            for x in split:
                chord_checker = x.strip('^#b')
                if chord_checker.isalpha():
                    chords = note_to_int(x)
                    chord_notes += chords
            my_music.play_chord(chord_notes, duration)

        # This else section is used for the lines with single notes
        else:
            # Used only when note is vanilla
            # Ex. C, G, B
            if split[0] in notes_in_list:
                og_note = note_to_int(split[0])
                for number in og_note:
                    my_music.play_note(number, duration)

            # If the note has a ^ at the beginning, figures out how many octaves
            # it was raised by
            elif split[0].find('^') == 0:
                octave_increase = note_to_int(split[0])
                for number in octave_increase:
                    my_music.play_note(number, duration)

            # These next two elif statements are used when the note
            # has a suffix
            # This one is used when it's a sharp note
            elif find_suffix[-1] == '#':
                sharp_note = note_to_int(split[0])
                for number in sharp_note:
                    my_music.play_note(number, duration)

            # This one is used when it's a flat note
            elif find_suffix[-1] == 'b':
                flat_note = note_to_int(split[0])
                for number in flat_note:
                    my_music.play_note(number, duration)

            # If there are invalid notes, they are treated as a pause
            elif split[0] not in NOTES:
                my_music.pause(duration)

def menu_play_song():
    song = get_song_file()
    play_song(song)




def main():
    print_menu()
    menu_choice = get_menu_choice()
    if menu_choice == 1:
        menu_play_song()
    if menu_choice == 2:
        menu_play_scale()
    if menu_choice == 3:
        quit
main()
my_music.close()
