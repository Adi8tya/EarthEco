from django.db import models

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def _str_(self):
        return f'Cart of {self.user.username}'

    def total_price(self):
        cart_items = self.cartitem_set.all()
        total = sum(item.product.price * item.quantity for item in cart_items)
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return f'{self.quantity} of {self.product.name}'


class Order(models.Model):
    PENDING = 'P'
    SHIPPED = 'S'
    DELIVERED = 'D'
    CANCELLED = 'C'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    items = models.ManyToManyField(Product, through='OrderItem')

    @property
    def total(self):
        return sum(item.quantity * item.product.price for item in self.orderitem_set.all())

    def _str_(self):
        return f'Order #{self.id} by {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def _str_(self):
        return f'{self.quantity} of {self.product.name}'