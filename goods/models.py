from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=70)
    img = models.BinaryField()
    is_active = models.BooleanField(null=True)