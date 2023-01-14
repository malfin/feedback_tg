from django.db import models
from django.core.validators import RegexValidator


class Feedback(models.Model):
    first_name = models.CharField(max_length=256)
    phone_regex = RegexValidator(regex=r'[0-9]$', message='Допускается до 15 цифр')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.email
