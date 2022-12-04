from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class people(models.Model):
    Email = models.EmailField(null=False)
    password = models.TextField(null=False, max_length=26)
    user_name = models.CharField(null=False, unique=True, max_length=30)
    first_name = models.CharField(max_length=100, help_text='First Name')
    last_name = models.CharField(max_length=100, help_text='Last Name')


class Poll(models.Model):
    user = models.TextField(max_length=30)
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count


from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
