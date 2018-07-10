from django.test import TestCase
from .models import Editor,Article,tags


# Create your tests here.
class EditorTestClass(TestCase):
    # Set up method
    def SetUp(self):
        self.elvis= Editor(first_name = 'elvis', last_name = 'Amuni', email = 'elvisamuni22@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.elvis,Editor))
