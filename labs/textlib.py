"""module docstring"""
class BodyOfText:
    """class docstring"""
    def __init__(self, text):
        self.text = text
    def num_paragraphs(self):
        """function or method docstring"""
        if self.text == "":
            return 0
        elif self.text.count("\n\n") == 0:
            return 1
        else:
            return self.text.count("\n\n")+1

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.

if __name__ == "__main__":
    bodyOfText = BodyOfText("""Lorem ipsum dolor sit amet, consectetur \
adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore \
magna aliqua. Sed risus pretium quam vulputate dignissim suspendisse \
in est. Eu lobortis elementum nibh tellus molestie. Urna neque viverra \
justo nec ultrices. Cum sociis natoque penatibus et magnis dis. Maecenas \
sed enim ut sem viverra aliquet. Pulvinar pellentesque habitant morbi \
tristique senectus et. Posuere ac ut consequat semper viverra nam. \
Eros in cursus turpis massa tincidunt dui ut. Egestas pretium \
aenean pharetra magna ac placerat. Proin sed libero enim sed. \
Gravida dictum fusce ut placerat orci nulla pellentesque \
dignissim enim. Dapibus ultrices in iaculis nunc sed augue \
lacus viverra vitae. Et odio pellentesque diam volutpat \
commodo sed. Nisl pretium fusce id velit ut tortor \
pretium viverra suspendisse.""")

    print(bodyOfText.num_paragraphs())
