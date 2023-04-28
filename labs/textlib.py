class BodyOfText:
    def __init__(self, text):
        if text == "":
            raise ValueError
        self.text = text
    def num_paragraphs(self):
        return -1

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.

# if __name__ == "__main__":
#     foo = BodyOfText("")
#     print(foo.text)