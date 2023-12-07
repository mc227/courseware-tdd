"""module docstring"""
import unittest
from textlib import BodyOfText

test_string = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Cursus mattis molestie a iaculis at erat pellentesque. Cursus sit amet dictum sit amet justo donec enim. Augue neque gravida in fermentum. Lectus sit amet est placerat in. Vitae proin sagittis nisl rhoncus. Ultrices neque ornare aenean euismod elementum nisi quis. Potenti nullam ac tortor vitae purus faucibus ornare suspendisse sed. Mattis aliquam faucibus purus in massa. A condimentum vitae sapien pellentesque. Ultricies mi eget mauris pharetra et ultrices neque ornare aenean. Ac feugiat sed lectus vestibulum mattis. Laoreet non curabitur gravida arcu ac tortor dignissim convallis.

Egestas diam in arcu cursus euismod. Ut porttitor leo a diam sollicitudin tempor id eu. Netus et malesuada fames ac turpis egestas maecenas pharetra. Vestibulum morbi blandit cursus risus at ultrices mi tempus. Sed euismod nisi porta lorem mollis. In aliquam sem fringilla ut morbi tincidunt. Elementum curabitur vitae nunc sed. Id cursus metus aliquam eleifend mi in nulla. Ante in nibh mauris cursus mattis molestie a iaculis. Tristique senectus et netus et malesuada.

Mattis pellentesque id nibh tortor id aliquet lectus proin nibh. Potenti nullam ac tortor vitae purus. Integer quis auctor elit sed vulputate. In fermentum posuere urna nec. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Odio tempor orci dapibus ultrices in. Turpis egestas maecenas pharetra convallis. Tempor orci dapibus ultrices in iaculis nunc sed augue lacus. Facilisi cras fermentum odio eu feugiat. Elit pellentesque habitant morbi tristique senectus et. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Gravida cum sociis natoque penatibus. Blandit libero volutpat sed cras ornare arcu dui vivamus. Auctor neque vitae tempus quam. Tincidunt ornare massa eget egestas purus. Mauris augue neque gravida in fermentum et sollicitudin. Amet cursus sit amet dictum. Scelerisque viverra mauris in aliquam sem fringilla ut morbi. Egestas erat imperdiet sed euismod nisi porta lorem mollis. Platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim."""

class TestBodyOfText(unittest.TestCase):
    """class docstring"""
    def test_empty_story(self):
        """function or method docstring"""
        body_of_text = BodyOfText("")
        self.assertEqual(body_of_text.num_paragraphs(), 0)
        self.assertEqual(body_of_text.paragraphs(), [])

    def test_single_paragraph(self):
        """function docstring"""
        body_of_text = BodyOfText("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed risus pretium quam vulputate dignissim suspendisse in est. Eu lobortis elementum nibh tellus molestie. Urna neque viverra justo nec ultrices. Cum sociis natoque penatibus et magnis dis. Maecenas sed enim ut sem viverra aliquet. Pulvinar pellentesque habitant morbi tristique senectus et. Posuere ac ut consequat semper viverra nam. Eros in cursus turpis massa tincidunt dui ut. Egestas pretium aenean pharetra magna ac placerat. Proin sed libero enim sed. Gravida dictum fusce ut placerat orci nulla pellentesque dignissim enim. Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Et odio pellentesque diam volutpat commodo sed. Nisl pretium fusce id velit ut tortor pretium viverra suspendisse.""")
        self.assertEqual(body_of_text.num_paragraphs(),1)
        self.assertEqual(body_of_text.paragraphs(), [])

    def test_several_paragraphs(self):
        """function docstring"""
        body_of_text = BodyOfText(test_string)
        self.assertEqual(body_of_text.num_paragraphs(), 3)
        self.assertEqual(body_of_text.paragraphs(), [])

# Part of Powerful Python Academy. Copyright MigrateUp LLC. All rights reserved.
