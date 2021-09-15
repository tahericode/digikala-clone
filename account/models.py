from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to = 'users/%Y/%m/%d', blank = True , null = True)
    def __str__(self):
        return 'profile for user'.format(self.user.username)
    