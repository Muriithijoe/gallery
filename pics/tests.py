from django.test import TestCase
from .models import Editor,Location,categories,Photo

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

class PhotoTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_category = categories(name = 'testing')
        self.new_category.save()

        self.new_photo= Photo(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_photo.save()

        self.new_photo.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Location.objects.all().delete()
        categories.objects.all().delete()
        Photo.objects.all().delete()
