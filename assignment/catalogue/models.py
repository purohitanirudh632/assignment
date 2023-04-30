from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=120)

    class Meta:
        db_table = "category"

    def __str__(self) -> str:
        return self.title



class Item(models.Model):
    title = models.CharField(max_length=120)
    is_available = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    image = models.ImageField(upload_to="./media/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name = "items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, help_text="Prices are in dollars")

    class Meta:
        db_table = "item"

    def __str__(self):
        return self.title

