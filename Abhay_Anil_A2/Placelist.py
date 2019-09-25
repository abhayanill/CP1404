"""Abhay Anil JC539324 CP1404 Assignment 2"""
"""Travel Tracker 2.0"""

from kivy.app import App  # Import relevant kivy function
from kivy.lang import Builder
from kivy.uix.button import Button
from Places import Place
import operator  # import the operator
import csv  # import the csv file


class Placelist(App):
    def build(self):  # Create the main widget for Kivy program
        self.file_opener = open("Places.csv")  # Open the file
        self.file_reader = csv.reader(self.file_opener)  # Read the file

        self.place = sorted(self.file_reader, key=operator.itemgetter(2))  # Sorting the places with priority

        self.title = "Travel Tracker 2.0-AbhayAnil"  # Main widget title
        self.root = Builder.load_file("list.kv")  # Load the kivy file
        self.required_mark()  # Set the default state for places list (Required list)
        return self.root

    def required_mark(self):  # Function for required list and mark items to the completed (required button)
        count = 0

        self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets

        required_list = sorted(self.place, key=operator.itemgetter(2))  # Sorting the list with priority

        self.root.ids.status_label.text = "Click places to mark them as completed"  # Prompt at status label

        for place in required_list:  # using for loop to separate to sorted file
            if "r" in place[3]:  # When "r" in places 3, then count, calculate and add the button of required places
                temp_button = Button(text=place[0], background_color=[count - 0, 0, 0, 3])  # Setting the button text and background color
                temp_button.place = place
                temp_button.bind(on_release=self.handle_mark)  # Setting when user click the button
                self.root.ids.entriesBox.add_widget(temp_button)  # Add widgets for each required place
                count += 1
        if count == 0:  # If total count = 0, then means no required places
            self.root.ids.top_label.text = "No unvisited places"  # Show the prompt at the top label
            self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets
        else:
            self.root.ids.top_label.text = "{} places yet to visit".format(count)

    def handle_mark(self, instance):  # Function when user click the button of the required place (Each required button)
        place = instance.text
        instance.place[3] = "c"  # Using "c" instead of "r" in the list when user chooses the place
        self.root.ids.status_label.text = (
            "{}, {}, Priority: {} marked as completed".format(instance.place[0], instance.place[1], instance.place[2]))# Show the marked places at the status label

    def completed(self):  # Function for the completed places (Completed button)
        count = 0

        self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets

        completed_list = sorted(self.place, key=operator.itemgetter(2))

        for place in completed_list:  # using for loop to separate to sorted file
            if "c" in place[3]:  # When "c" in place 3, then count, calculate and add the button of completed places
                temp_button = Button(text=place[0],background_color=[count - 0, 3, 1, 1])  # Setting the button text
                temp_button.place = place
                temp_button.bind(on_release=self.handle_completed)  # Setting when user click the button
                self.root.ids.entriesBox.add_widget(temp_button)  # Add widgets for each completed places
                count += 1
        if count == 0:  # If total count = 0, then means no completed places
            self.root.ids.top_label.text = "No visited places"  # Show the prompt at the top label
            self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets
        else:
            self.root.ids.top_label.text = "{} places visited".format(count)

    def handle_completed(self, instance):  # Function when user click the button of the completed places (Each completed button)
        self.root.ids.status_label.text = "{}, {}, Priority: {} (Visited)".format(instance.place[0], instance.place[1], instance.place[2])
        # Show the detail of the completed places at the status label

    def handle_add(self):  # Function for adding new item  (Add item button)
        place_name = self.root.ids.input_place.text  # Let user enter the place name
        country = self.root.ids.input_country.text  # Let user enter the name of country
        priority = self.root.ids.input_priority.text  # Let user enter the priority of place

        if place_name == "" or country == "" or priority == "":  # If any field is blank, show error prompt
            self.root.ids.status_label.text = "All fields must be completed"
        else:
            try:  # Using exception let user enter valid number
                priority = int(self.root.ids.input_priority.text)
            except ValueError:
                self.root.ids.status_label.text = "Please enter a valid number"
            else:
                if priority != 1 and priority != 2 and priority != 3:
                    self.root.ids.status_label.text = "Priority must be 1, 2 or 3"
                else:
                    new_place = [place_name, country, str(priority), "r"]  # Create a list with new place
                    self.place.append(new_place)  # Appending the new list to the place list
                    add_place = Place(place_name, country, priority)
                    self.root.ids.status_label.text = str(add_place)
                    # show the added place at the status label
                    self.root.ids.input_place.text = ""
                    self.root.ids.input_country.text = ""
                    self.root.ids.input_priority.text = ""
                    # Clear whole input box after the new place is added to the list
        # Error check

    def handle_clear(self):  # Function for clear whole input box (Clear button)
        self.root.ids.input_place.text = ""
        self.root.ids.input_country.text = ""
        self.root.ids.input_priority.text = ""

    def save_place(self):  # Function for saving completed place to the file (Save place button)
        file_writer = open("Places.csv", "a")  # Open the file with the correct format
        count = 0

        for place in self.place:  # Find the completed place and save to the csv file
            if "c" in place[3]:
                count += 1
                if count == 1:
                    file_writer2 = open("Places.csv", "w")
                    file_writer2.writelines(place[0] + "," + place[1] + "," + place[2] + "," + "c")
                    file_writer2.close()
                else:
                    file_writer.writelines("\n" + place[0] + "," + place[1] + "," + place[2] + "," + "c")
            else:
                file_writer.writelines("")
        if count == 0:
            file_writer2 = open("Places.csv", "w")
            file_writer2.close()

        for place in self.place:  # Find the completed place and save to the csv file
            if "r" in place[3]:
                count += 1
                if count == 1:
                    file_writer2 = open("Places.csv", "w")
                    file_writer2.writelines(place[0] + "," + place[1] + "," + place[2] + "," + "r")
                    file_writer2.close()
                else:
                    file_writer.writelines("\n" + place[0] + "," + place[1] + "," + place[2] + "," + "r")
            else:
                file_writer.writelines("")
        if count == 0:
            file_writer2 = open("Places.csv", "w")
            file_writer2.close()

        self.root.ids.status_label.text = "{} places saved to Places.csv. Happy Travelling :)".format(count)
        # Display how many Places which add to the file at the status label
        file_writer.close()
        # Close the file


Placelist().run()
