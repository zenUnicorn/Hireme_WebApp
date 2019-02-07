from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.EmailField()
    skill = models.CharField(max_length=200)
    

    #additional classes
    twitter_address = models.URLField(blank=True)
    slack_address = models.URLField(blank=True)
    skype_address = models.URLField(blank=True) 
    github_repo = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_image',blank=True)
    

    def get_absolute_url(self):
        return reverse("detail",kwargs={'pk':self.pk})
   
    def __str__(self):
        return self.user.username 