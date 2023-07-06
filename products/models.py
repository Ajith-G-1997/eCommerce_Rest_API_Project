from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price= models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_name
