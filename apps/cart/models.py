from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from datetime import datetime

from apps.product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        cart = Cart.objects.create(user=instance)
        cart.save()


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))

    def __str__(self):
        return str(self.cart.user) + " - " + str(self.product)
    #
    # def total_price(self):
    #     return self.quantity * self.unit_price
    #
    # total_price = property(total_price)
