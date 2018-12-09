"""
Name :              Myo Min Htwe
Student ID:         13644372
Date:               9/12/2018
Program details:    This programme shows a list of song where a user can learn and track the songs
                    they have completed learning.
GitHub:
"""


from operator import itemgetter  # importing itemgetter function from operator module for sorting
filename = "songs.csv"  # assigning a variable name to csv file


def menu():
    print("""Menu:
L - List songs
A - Add new songs
C - Complete a song
Q - Quit""")
    list_of_choice = "LACQ"  # List of choice
    choice = input().upper()  # Asking user to input and make it upper case
    while choice not in list_of_choice:
        print("Invalid menu choice")
        choice = input().upper()
    return choice  # Return the menu input


"""
function load_song
    song_list = list
    in_file = open songs.csv (r)
    for line in in_file:
        remove white space
        next_list = split line for ","
        song_list= append next
    return song_list
"""


def load_song():  # this function loads the song file
    song_list = [] # save list of song
    in_file = open(filename, 'r')  # 'r' argument is to read the file
    for line in in_file:
        line = line.strip("\n")  # remove white space
        next_list = line.split(",")  # to make the line string into list
        song_list.append(next_list)
    in_file.close()  # to close #
    return song_list  # return Song_list



def show_songs(song_list): # this function shows formatted list of songs
    count = 0  # to start the count from zero
    for i in range(len(song_list)):  # start the loop with variable i
        if song_list[i][3] == "y":
            count += 1                 # number counting
            star = "*"               # adding * next to the complete song list
        else:
            star = " "               # adding blank next to the incomplete song list
        print(" ", str(i) + ".", star,"", end=" ")  #printing '.' and '*'
        for j in range(2):    # loop for the list of the song with variable j
            if j == 1:
                dash = "-"  # adding '-' next to 1st index
            else:
                dash = ""  # adding blank next to other indices
            print(dash, "{:30}".format(song_list[i][j]), end=" ")
        print("({:4})".format(song_list[i][-2]))
    print(len(song_list) - count, "songs learned,", count, "songs still to learn")  #printing songs learned and number of songs need to learn


"""
function complete_song(song_list)
    count = 0
    for i in range(length(song_list)):
        if song_list[i][3]=="y":
            count += 1
    learn_number = get_integer("Enter the number of song to mark as learned: ")
    if song_list[song_number][3] == "n" then
        print("You have already learned", song_list[learn_number][0])
    else then
        song_list[learn_number][3] = "n"
        print(song_list[learn_number][0], "by", song_list[learn_number][1], "learned")
    return song_list
"""


def complete_song(song_list): # this function marks the song as learned
    count = 0  # to start the count from zero
    for i in range(len(song_list)):  # start the loop with variable i
        if song_list[i][3] == "y":
            count += 1  # number counting
    if count ==0:
        print("No more songs to learn!")

    learn_number = count_number("Enter the number of song to mark as learned\n>>> ")  # User input song number
    if song_list[learn_number][3] == "n":  #If index 3 is 'n', print already learned
        print("You have already learned", song_list[learn_number][0])
    else:
        song_list[learn_number][3] = "n"  # If index 3 is not yet 'n', it will be assigned as 'n'
        print(song_list[learn_number][0], "by", song_list[learn_number][1], "learned")
        return song_list


def add_new_song():  # the functions new songs to the songs.csv
    new_song = [] #Save new song as list
    title = check_string("Title: ") # Title input
    artist = check_string("Artist: ") # Artist input
    year = str(check_year("Year: "))  # Year input
    new_song.append(title)
    new_song.append(artist)
    new_song.append(year)
    new_song.append("y")
    print(title, "by", artist, "({:4})".format(year), "added to song list")  # print added song list
    return new_song


def check_string(prompt):   #this function check string inputs
    string_input = input(prompt)
    while len(string_input) == 0:
        print("Input can not be blank")
        string_input = input(prompt)
    return string_input.title()


def count_number(prompt):  #this function check the song number entered
    while True:
        try:
            input_number = int(input(prompt))
            if input_number < 0:
                print("Number must be >= 0")
            elif input_number >= 7:
                print("Song number not in the list")
            else:
                return input_number
        except ValueError:
            print("Invalid input; enter a valid number")


def check_year(prompt): #this function check the year entered in new added song
    while True:
        try:
            input_number = int(input(prompt))
            if input_number < 0:
                print("Number must be >= 0")
            else:
                return input_number
        except ValueError:
            print("Invalid input; enter a valid number")


def save_songs(song_list):   # this function saves final file
    final_file = open(filename, 'w')    # argument 'w' will overwrite the whole program in list
    for i in range(len(song_list)):
        if i != 0:
            print("\n", end="", file=final_file)
        for j in range(len(song_list[i])):
            final_file.write(song_list[i][j])  # write the arranged data into the songs.csv
            if j != 3:
                print(",", end="", file=final_file)  # the message that show the confidential note
    final_file.close()  # close the songs.csv file


def main():
    print("Songs To Learn 1.0 - by Myo Min Htwe ")
    song_list = load_song()  # invoking load_song function
    print(len(song_list), "songs loaded")  # shows the number of songs in songs.csv
    choice = menu()  # invoking menu function
    while choice != "Q":
        song_list.sort(key=itemgetter(1, 0))
        if choice == "C":  # 'C' invokes complete_song function
            complete_song(song_list)
        elif choice == "A":  # 'A' invokes add_new_song function
            add_new_song()
        else:  # 'L' invokes show_songs function
            show_songs(song_list)
        choice = menu()
    save_songs(song_list)  # 'Q' invokes save_songs function
    print(len(song_list), "songs saved to", filename, "\nHave a nice day :)")


if __name__ == '__main__':
    main()

