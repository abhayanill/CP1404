"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
# entered_number = 0 seems unesscary ?
while not finished:
    try:
        # TODOs completed below
        entered_number = int(input("Enter an integer value: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")

print("Valid result is:", entered_number)