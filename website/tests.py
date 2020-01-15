from django.test import TestCase
from .models import *

# Create your tests here.

class AwardTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.gallery=Award(title='gallery',description='image to be seen',url_link='https://adrianogallery.herokuapp.com/',image='images/bird.jpg')

    def test_instance(self):
        Award.objects.all().delete()
        self.assertTrue(isinstance(self.award_one,Award)) 

    def test_save_method(self):
        
        self.image_one.save_award()
        awards = Award.objects.all()
        self.assertTrue(len(awards) > 0)
        
    def tearDown(self):
        Award.objects.all().delete()

class ProfileTestClass(TestCase):
    
    '''
    This is a class that perform unnittest  behaviour on the Profile Model.
    '''
    
    def setUp(self):
        self.profile_one = Profile(profile_pic='images/mine.jpg',bio='Currently doing datascience in moringa',name="falone")
    
    def test_save_method(self):
        
        self.profile_one.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def tearDown(self):
        Profile.objects.all().delete()

 
    