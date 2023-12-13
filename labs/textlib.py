"""textlib.py"""
import re

class BodyOfText:
    """class docstring"""
    def __init__(self, text):
        if text == "":
            raise ValueError("BodyOfText input cannot be blank")
        self.text = text

    def num_paragraphs(self):
        """function or method docstring"""
        if self.text == "":
            return 0
        else:
            return self.text.count("\n\n") + 1

    def paragraphs(self):
        """Stub method to return a list strings.
        These strings represent a paragraph"""
        return [paragraph.strip() for paragraph in self.text.split("\n\n")]

    def wordcounts(self):
        """
        `wordcounts` counts how many times each word occurs.

        The method returns a dictionary mapping the lower-cased word to the number of
        occurrences.
        Case and punctuation are ignored
        """
        # Use regex to extract words and remove punctuation
        words = re.findall(r'\b\w+\b', self.text.lower())

        # Count occurrences using a dictionary
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

        return word_counts

if __name__ == "__main__":
    body = BodyOfText("")
