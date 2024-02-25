from django.db import models

# Create your models here.

class user_details(models.Model):
    name = models.CharField(max_length = 100)
    bio = models.TextField()
    phone_no = models.CharField(max_length = 50)
    boolean_field = models.BooleanField()
    date_time_field = models.DateTimeField()
    email_field = models.EmailField()

    def __str__(self):
        return self.name