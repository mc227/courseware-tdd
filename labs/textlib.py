"""textlib.py"""
class BodyOfText:
    """class docstring"""
    def __init__(self, text):
        self.text = text

    def num_paragraphs(self):
        """function or method docstring"""
        if self.text == "":
            return 0
        # elif self.text.count("\n\n") == 0:
        #     return 1
        else:
            return self.text.count("\n\n") + 1

    def paragraphs(self):
        """Stub method to return an empty list"""
        return [paragraph.strip() for paragraph in self.text.split("\n\n")]
