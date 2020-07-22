from django.db import models
import datetime
from login.models import User


class ItemManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        # Confirm size
        if len(postData['size']) < 3:
            errors['size'] = 'Size must be at least 3 characters'

        # Confirm crust
        if len(postData['crust']) < 3:
            errors['crust'] = 'Crust must be at least 3 characters'

        # Confirm toppings
        if len(postData['toppings']) < 3:
            errors['crust'] = 'Toppings must be at least 3 characters'

        return errors


class Order(models.Model):
    method = models.CharField(max_length=255)
    order_total = models.DecimalField(max_digits=7, decimal_places=2)
    taxes = models.DecimalField(max_digits=7, decimal_places=2)
    created_by = models.ForeignKey(
        User, related_name='orders_placed', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Items(models.Model):
    size = models.CharField(max_length=255)
    crust = models.CharField(max_length=255)
    toppings = models.CharField(max_length=255)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    order = models.ForeignKey(
        Order, related_name='has_items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
