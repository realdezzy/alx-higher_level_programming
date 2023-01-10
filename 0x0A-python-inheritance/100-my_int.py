#!usr/bin/python3
"""MyInt equality reverser"""


class MyInt(int):
    """Implements reverse of equality operation"""

    def __eq__(self, value):
        """compares equality"""

        return not super().__eq__(value)

    def __ne__(self, value):
        """Not equal comparison"""

        return not super().__ne__(value)
