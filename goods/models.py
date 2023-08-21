from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=70,
                            verbose_name="Сategory",
                            help_text="Enter a сategory title")
    img = models.BinaryField()
    is_active = models.BooleanField(null=True)
    def __str__(self):
        return {self.name}
class goods(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Good",
                            help_text="Enter a good title")
    categories = models.ForeignKey(categories,
                                   on_delete=models.PROTECT,
                                   limit_choices_to={"is_active": True})
    def __str__(self):
        return f'{self.categories.name}: {self.name}'