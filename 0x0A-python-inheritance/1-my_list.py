#!/usr/bin/python3
"""MyList Simple list subclass"""


class MyList(list):
    """MyList is a subclass of the list class"""

    def print_sorted(self):
        """Prints a sorted copy of the list instance"""

        print(sorted(self))
