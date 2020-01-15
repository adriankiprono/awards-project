from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Award(models.Model):
    title=models.CharField(max_length =60)
    description=models.TextField()
    url_link=models.CharField(max_length =100)
    profile =models.ForeignKey("Profile",on_delete=models.CASCADE,default='now')
    image=models.ImageField(upload_to= 'images/',default='image')

    @classmethod
    def search_by_title(cls,search_term):
        awards = cls.objects.filter(title__icontains=search_term)
        return awards

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField(max_length= 100)
    profile_pic= models.ImageField(upload_to= 'avatar/',default='image2')

    def __str__(self):
        return self.name


