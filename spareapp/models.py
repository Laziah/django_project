from django.db import models
from django.utils import timezone

# Import necessary modules from Django

# Create your models here.

class Category(models.Model):
    # Define a model class named Category
    name = models.CharField(max_length=50, null=False, blank=False)
    # Define a field 'name' which stores the category name as a character string
    
    def __str__(self):
        return self.name
    # Define a method to return the name of the category when the model instance is printed

class Product(models.Model):
    # Define a model class named Product
    Category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    # Create a foreign key relationship to the Category model for categorizing products
    date_of_arrival = models.DateField(default=timezone.now)
    # Create a field for the date of arrival with the default value set to the current time
    item_name = models.CharField(max_length=50, null=False, blank=False)
    item_orgin = models.CharField(max_length=50, null=False, blank=False)
    total_quantity = models.IntegerField(default=0, null=False, blank=False)
    issued_quantity = models.IntegerField(default=0, null=False, blank=False)
    received_quantity = models.IntegerField(default=0, null=False, blank=False)
    unit_price = models.IntegerField(default=0, null=False, blank=False)
    # Define fields for various attributes of a product
    
    def __str__(self):
        return self.item_name
    # Define a method to return the name of the product when the model instance is printed

# more models (sales)

class Sale(models.Model):
    # Define a model class named Sale for recording sales transactions
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    # Create a foreign key relationship to the Product model for associating a product with a sale
    quantity = models.PositiveIntegerField(default=0, null=False, blank=False)
    issued_to = models.CharField(max_length=100, null=False, blank=False)
    amount_received = models.PositiveIntegerField(default=0, null=False, blank=False)
    unit_price = models.PositiveIntegerField(default=0, null=False, blank=False)
    branch_name = models.CharField(max_length=100, null=False, blank=False)
    customer_location = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=100, null=False, blank=False)
    # Define fields for various attributes of a sale transaction
    
    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)
    # Define a method to calculate the total amount of a sale transaction
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    # Define a method to calculate the change amount for a sale transaction
    
    def __str__(self):
        return self.item.item_name
    # Define a method to return the name of the item being sold when the model instance is printed
