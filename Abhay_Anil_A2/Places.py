class Place:
    def __init__(self, place="", country="", priority=0):
        self.place = place
        self.country = country
        self.priority = priority

    def __str__(self):
        return "{}, ${} (priority {}) added to shopping list".format(self.place, self.country, self.priority)
