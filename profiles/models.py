from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model): #it need to add something else
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) #maybe will delete
    name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../profile_img_z4mi3b'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"
