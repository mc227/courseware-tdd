class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def full_name(self):
        return f"{self.first} {self.last}"

    def formal_name(self,title):
        return f"{title} {self.first} {self.last}"