from django.db import models
from django.contrib.auth.models import User
from carmanager.cars.models import CarItem


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def add_item(self, car_item):
        cart_item, created = CartItem.objects.get_or_create(
            cart=self, car_item=car_item
        )
        return cart_item

    def remove_item(self, car_item):
        CartItem.objects.filter(cart=self, car_item=car_item).delete()

    def clear_cart(self):
        self.items.all().delete()

    def total_price(self):
        return sum(item.car_item.price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    car_item = models.ForeignKey(CarItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.car_item.car.model} in cart {self.cart.id}"

    def item_total_price(self):
        return self.car_item.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def create_order_from_cart(self, cart):
        for item in cart.items.all():
            OrderItem.objects.create(
                order=self,
                car_item=item.car_item,
                price=item.car_item.price,
            )
        cart.clear_cart()


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="order_items", on_delete=models.CASCADE
    )
    car_item = models.ForeignKey(CarItem, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car_item.car.model} in order {self.order.id}"
