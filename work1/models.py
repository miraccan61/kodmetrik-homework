
from django.db import models

# Create your models here.
class FormBuilder(models.Model):
    hash_id = models.CharField(max_length=50)
    formData = models.TextField()

    def __str__(self):
        return self.hash_id