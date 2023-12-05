"""
person.py
"""
class Person:
    """
    insert docstring
    """
    def __init__(self, first, last):
        """
        doc string
        """
        self.first = first
        self.last = last

    def full_name(self):
        """
        doc string
        """
        return self.first + " " + self.last

    def formal_name(self, honorific):
        """
        formal_name
        """
        return honorific + " " + self.full_name()
        