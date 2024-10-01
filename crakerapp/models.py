from django.db import models

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    item_number = models.AutoField(primary_key=True)  

    def __str__(self):
        return self.item_name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)  
    email = models.EmailField(blank=True) 
    address = models.TextField()
    order_date = models.DateTimeField(auto_now_add=True) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = (
        ('delivered', 'Delivered'),
        ('not_delivered', 'Not Delivered'), 
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_delivered')

    def __str__(self):
        return f"Order #{self.order_id} by {self.customer_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.item.item_name} (Order #{self.order.order_id})"
    
class FailedLoginAttempts(models.Model):
    device_id = models.CharField(max_length=255, unique=True)
    attempts = models.PositiveBigIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.device_id} - Attempts: {self.attempts}'