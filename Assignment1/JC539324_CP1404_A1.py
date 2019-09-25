"""
CP1404 Assignment 1 2019
Abhay Anil
Started 16/8/2019
Travel Tracker: Opens a list of places and allows the user to either, look at places to visit, look at visited places,
add new places to the list and marks a place as visited.

Pseudocode:

function load_places()
    create blank list called places list
    open file using csv reader
    for rows in csv file
        add each row to the blank places list
    sort places_list according to column 2 in ascending order
    return places list
function display_visited_places()
    create blank list called visited_list
    for places in range from zero to length of initial places list
        if within initial places, referencing a list within a list, check the fourth column and see if the string 'v' is present and add the place to the visited list from the initial places list
        if len of visited_list is equal to zero(therfore a empty list is present)
        print No visited places
    else:
        for completed in range from zero to length of visited_list
        print formatted string with completed, visited_list zero, visited_list one, visited_list two
"""

import csv

def main():
    """
    Travel Tracker program,
    determine travel list based on visited places, unvisited places and any new places which wish to visit in the future
    """
    places_list = load_places()

    print("Travel Tracker 1.0 - Abhay Anil \n{} Places loaded from places.csv".format(len(places_list)))
    menu = "Menu: \nL - List all places\nV - List visited places\nN - List unvisited places\nA - Add new place\n" \
           "M - Mark an place as visited\nQ - Quit"
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            all_places(places_list)

        elif choice == "V":
            display_visited_places(places_list)

        elif choice == "N":
            display_unvisited_places(places_list)

        elif choice == "A":
            places_list = add_new_place(places_list)

        elif choice == "M":
            visited_list = display_unvisited_places(places_list)
            if len(visited_list) != 0:
                mark_place_as_visited(visited_list)

        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ").upper()
    print("{} Places saved to places.csv\nThank You :D".format(len(places_list)))

    save_place(places_list)

def all_places(places_list):
    """Display full places list"""
    full_list = []
    for place in range(0, len(places_list)):
        full_list.append(places_list[place])
    if len(full_list) == 0:
        print("No places in list")
    else:
        for number in range(0, len(full_list)):
            print("{} {} in {} (Priority {})".format(number, full_list[number][0], full_list[number][1],
                                         full_list[number][2]))
    return full_list


def mark_place_as_visited(visited_list):
    """ get details for marking place; error checking places specified to be marked ; print marked place"""
    print("Enter the number of place to be added to visited list ")
    while True:
        try:

            specify_number_of_place_to_be_marked = int(input(">>> "))

            if specify_number_of_place_to_be_marked >= 0 and specify_number_of_place_to_be_marked < len(visited_list):
                break
            else:
                print("Invalid place number ")
        except ValueError:
            print("Invalid input; enter a number")
    visited_list[specify_number_of_place_to_be_marked][3] = 'v'
    print("{} marked as visited".format(visited_list[specify_number_of_place_to_be_marked][0]))


def add_new_place(places_list):
    """ create new places list; specify each column with inputs while error checking ; add new place to places list """
    new_place = [0, '0', 0, 0]
    new_place[3] = 'n'
    new_place[0] = str(input("Place name: ").strip())
    new_place[1] = str(input("Country: ").strip())
    while new_place[0] == "":
        print("Input cannot be blank")
        new_place[0] = str(input("Place name: ").strip())
    while new_place[1] == "":
        print("Input cannot be blank")
        new_place[1] = str(input("Country: ").strip())
    else:
        while True:
            try:
                new_place[2] = str(input("Priority: "))
                if int(new_place[2]) >= 1 and int(new_place[2]) <= 3:
                    break
                else:
                    print("Priority must be 1, 2 or 3")
            except ValueError:
                print("Invalid input; enter a valid number")
    print("{} in {} (priority {}) added to unvisited list".format(new_place[0], new_place[1], new_place[2]))
    places_list.append(new_place)
    places_list = sorted(places_list, key=lambda places_list: places_list[2])
    return places_list


def save_place(places_list):
    """ using the csv writer command and overwrite exsisting items.csv file """
    save_place = csv.writer(open("places.csv", 'w', newline=''))
    for place in places_list:
        save_place.writerow(place)

def display_unvisited_places(places_list):
    """ create blank list for unvisited places, go through places list looking for unvisited places saving to unvisited list; check a empty list isn't present;
    """
    unvisited_list = []
    for un_list in range(0, len(places_list)):
        if places_list[un_list][3] == 'n':
            unvisited_list.append(places_list[un_list])
    if len(unvisited_list) == 0:
        print("No places to visit")
    else:
        for unvisited in range(0, len(unvisited_list)):
            print("{} {} in {} (Priority {})".format(unvisited, unvisited_list[unvisited][0],
                                                   unvisited_list[unvisited][1], unvisited_list[unvisited][2]))
    return unvisited_list

def display_visited_places(places_list):
    """ create blank list for visited places and go through places list looking for
    visited places saving it to visited list and check a empty list isn't present;
    """
    visited_list = []
    for place in range(0, len(places_list)):
        if places_list[place][3] == 'v':
            visited_list.append(places_list[place])
    if len(visited_list) == 0:
        print("No visited places")
    else:
        for number in range(0, len(visited_list)):
            print("{} {} in {} (Priority {})".format(number, visited_list[number][0], visited_list[number][1], visited_list[number][2]))
    return visited_list


def load_places():
    """ using the csv reader command open places.csv file and read into places list """
    places_list = []
    file_open = csv.reader(open("places.csv"))
    for row in file_open:
        places_list.append(row)
    places_list = sorted(places_list, key=lambda places_list: places_list[2])
    return places_list


main()