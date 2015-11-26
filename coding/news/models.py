from django.db import models


# Create your models here.
class SignUp(models.Model):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    time_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    time_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email
