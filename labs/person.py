"""
insert doc string
"""
class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def full_name(self,first,last):
        return self.first + " " + self.last