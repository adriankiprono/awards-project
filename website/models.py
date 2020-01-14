from django.db import models

# Create your models here.
class Award(models.Model):
    title=models.CharField(max_length =60)
    description=models.TextField()
    url_link=models.CharField(max_length =100)
    profile =models.ForeignKey("Profile",on_delete=models.CASCADE,default='now')

    @classmethod
    def search_by_title(cls,search_term):
        award = cls.objects.filter(title__icontains=search_term)
        return award

    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField(max_length= 100)

    def __str__(self):
        return self.name


