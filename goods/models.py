from django.db import models

# Create your models here.
class categories(models.Model):
    name = models.CharField(max_length=70,
                            verbose_name="Сategory",
                            help_text="Enter a сategory title")
    description = models.TextField(max_length=3000,
                                   verbose_name="Сategory description",
                                   help_text="Must contain only 3000 characters")
    img = models.BinaryField()
    is_active = models.BooleanField(null=True)
    def __str__(self):
        return {self.name}
    class Meta:
        verbose_name = 'Сategory'
        verbose_name_plural = 'Categories'
        ordering = ['-is_active', 'name']
class goods(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Good",
                            help_text="Enter a good title")
    categories = models.ForeignKey(categories,
                                   on_delete=models.PROTECT,
                                   limit_choices_to={"is_active": True})
    description = models.TextField(max_length=3000,
                                   verbose_name="Good description",
                                   help_text="Must contain only 3000 characters")
    img = models.BinaryField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(null=True)
    def __str__(self):
        return f'{self.categories.name}: {self.name}'
    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'
        ordering = ['-is_active', 'name']